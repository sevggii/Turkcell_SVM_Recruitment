# 👩‍💻 İşe Alımda Aday Seçimi: SVM ile Başvuru Değerlendirme

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-green.svg)

---

## 🌟 Proje Amacı

Bu proje, bir teknoloji firmasında İnsan Kaynakları ekibinin, yazılım geliştirici pozisyonu için başvuran adayları, **tecrübe yılı** ve **teknik sınav puanı** bilgilerine göre otomatik olarak değerlendirmesini sağlayan bir makine öğrenmesi modelidir. Model, adayın işe alınıp alınmayacağını tahmin eder.

---

## ✨ Etiketleme Kriteri

- **Tecrübe < 2 yıl**  
- **Teknik puan < 60**  

→ Bu şartları sağlayan adaylar: `1` (Başarısız)  
→ Diğer tüm adaylar: `0` (Başarılı)

---

## 🧪 Yöntemler

- 📊 **Veri Üretimi**: `numpy` ile 200 rastgele aday verisi oluşturuldu.
- 🌍 **Etiketleme**: Yukarıdaki kuralla adaylar işaretlendi.
- 🚮 **Ölçekleme**: `StandardScaler` ile normalize edildi.
- 🧠 **Model**: `SVC(kernel='linear')` ile SVM modeli eğitildi.
- 📈 **Görselleştirme**: Karar sınırı `matplotlib` ile çizildi.
- 💬 **Tahmin**: Kullanıcıdan girdi alınıp modelle tahmin yapıldı.
- 🏋️‍♂️ **Değerlendirme**: `accuracy_score`, `confusion_matrix`, `classification_report` ile performans ölçüldü.

---

## 🛠️ Kullanılan Teknolojiler

- Python 3
- numpy
- matplotlib
- scikit-learn
- FastAPI

---

## 🔎 Kurulum & Çalıştırma

```bash
pip install -r requirements.txt
python recruitment_svm.py
```

API başlatmak için:
```bash
uvicorn api:app --reload
```

---

## 📝 Komutla Tahmin

Örnek kullanım:
```python
tahmin_yap(tecrube=2.5, puan=75)  # Beklenen: İşe ALINDI
```

---

## 📊 Model Performansı (Örnek Çıktı)

**Accuracy (Doğruluk)**: %91

**Classification Report:**
```
              precision    recall  f1-score   support
           0       0.94      0.96      0.95        38
           1       0.85      0.80      0.82        12
```

**Confusion Matrix:**
```
[[37  1]
 [ 2 10]]
```

---

## 📸 Karar Sınırı Grafiği

Modelin karar sınırları tecrübe ve puana göre matplotlib ile çizilmiştir.

---

## 🚀 Gelişim Fırsatları

1. 📌 Doğrusal olmayan kernel'larla sınıflandırma (rbf, poly, sigmoid)
2. ⚙️ GridSearchCV ile hiperparametre (C, gamma) ayarı
3. ➕ Daha fazla öznitelik (eğitim, pozisyon, proje sayısı vs.)
4. 🧪 Test verisini çeşitlendirme ve veri artırma

---

## 🔗 Ek Belgeler

- [Faker ile Veri Üretme Notları](Faker_Arastirma.md)
- `input.json`: Gerçek zamanlı test verisi örneği

---

## 👤 Hazırlayan

💖 Sevgi Targay & ChatGPT
Bu proje bir öğrenci emeğidir, *eser miktarda🙂* ChatGPT desteğiyle koddan yoruma her satırı özenle ve sevgiyle hazırlanmıştırr💖🤖

> README ise ChatGPT'nin nazik katkısıyla hazırlanmıştır:  
> “ChatGPT, yapay zeka eğitiminin hakkını verelim!” dedi, belgelemeyi özenle tamamladı. 🤖

