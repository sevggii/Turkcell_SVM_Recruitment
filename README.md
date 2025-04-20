# 🎯 İşe Alımda Aday Seçimi: SVM ile Başvuru Değerlendirme

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-green.svg)

Bu proje, yazılım geliştirici pozisyonu için başvuran adayların tecrübe yılı ve teknik sınav puanına göre işe alınıp alınmamasını tahmin eden bir makine öğrenmesi modeli içerir.

## 📊 Proje Özellikleri

- 🎲 Faker kütüphanesi ile gerçekçi veri üretimi
- 🤖 SVM (Support Vector Machine) ile sınıflandırma
- 📈 Veri ön işleme ve ölçekleme
- 📊 Model performans değerlendirmesi
- 🎨 Karar sınırı görselleştirmesi
- 🌐 FastAPI ile REST API servisi

## 🚀 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

### 1. Model Eğitimi ve Değerlendirme

```bash
python recruitment_svm.py
```

Bu komut şunları yapacak:
- 200 örnek veri üretir
- Modeli eğitir
- Performans metriklerini gösterir
- Karar sınırını görselleştirir

### 2. API Servisi

API servisini başlatmak için:
```bash
uvicorn api:app --reload
```

API'yi test etmek için:
```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"tecrube_yili": 3, "teknik_puan": 75}'
```

## 📝 Model Detayları

### Veri Özellikleri
- **Tecrübe yılı**: 0-10 yıl arası
- **Teknik puan**: 0-100 arası

### Etiketleme Kriteri
- ✅ İşe Alındı (etiket: 0)
  - Tecrübesi 2 yıl veya daha fazla VEYA
  - Teknik puanı 60 veya daha yüksek
- ❌ İşe Alınmadı (etiket: 1)
  - Tecrübesi 2 yıldan az VE
  - Teknik puanı 60'tan düşük

## 🔍 API Endpoints

### GET /
- Ana sayfa mesajı
- API'nin çalışıp çalışmadığını kontrol etmek için

### POST /predict
- Aday değerlendirme tahmini
- İstek gövdesi:
```json
{
    "tecrube_yili": 3,
    "teknik_puan": 75
}
```
- Yanıt:
```json
{
    "prediction": "İşe Alındı",
    "hire_probability": 0.9989,
    "reject_probability": 0.0011
}
```

## 🎯 Geliştirme Alanları

1. 🔄 Farklı kernel'lar ile doğrusal olmayan sınıfları deneme
2. ⚙️ Hiperparametre optimizasyonu (C, gamma)
3. ➕ Daha fazla özellik ekleme
4. 📈 Model performansını artırma

## 📚 Kaynaklar

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Faker Documentation](https://faker.readthedocs.io/)

## 👥 Katkıda Bulunma

1. Bu projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 