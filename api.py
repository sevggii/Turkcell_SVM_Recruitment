from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from recruitment_svm import model, scaler

app = FastAPI(title="İşe Alım SVM API",
             description="SVM tabanlı işe alım aday değerlendirme API'si")

class Candidate(BaseModel):
    tecrube_yili: float
    teknik_puan: float

@app.post("/predict")
async def predict_candidate(candidate: Candidate):
    try:
        # Veriyi ölçekle
        input_data = scaler.transform([[candidate.tecrube_yili, candidate.teknik_puan]])
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        result = "İşe Alınmadı" if prediction == 1 else "İşe Alındı"
        
        return {
            "prediction": result,
            "hire_probability": float(probability[0]),
            "reject_probability": float(probability[1])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "İşe Alım SVM API'sine Hoş Geldiniz"} 