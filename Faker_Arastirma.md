
🎭 Faker Kütüphanesi ile Gerçekçi Sahte Veri Üretimii

-Faker (yani feyk-sahte) adından da anlaşılacağı gibi sahte ama gerçekçi veriler üretmek için kullanılan bir Python kütüphanesi
-Test verisi, demo içerik, prototip ya da mock veri gerektiğinde hayat kurtarıyor diyebiliriz.

🔹 Örnek Veri Tipleri

👤 Kişisel Bilgiler
- İsim & Soyisim
- E-posta
- Telefon numarası
- Doğum tarihi
- TC Kimlik No

📍 Adres Bilgileri
- Tam adres
- Şehir
- Posta kodu
- Ülke

💼 İş Bilgileri
- Şirket adı
- Meslek
- Departman
- İş unvanı

📅 Tarih & Saat
- Rastgele tarih
- Saat bilgisi
- Timestamp

💡 Faker'ın Avantajları
- Gerçekçi veri üretir → test senaryoları daha anlamlı olur
- Çok dilli destek → global projelerde kullanışlı
- Kolay kullanılır → az kodla çok iş
- Özelleştirilebilir → kendi veri tipini yazabilirsin
- Seed ile tekrar üretilebilir → tutarlılık sağlanır

🚀 Nerelerde Kullanılır?
1. Unit testler
2. Veritabanı demo verileri
3. UI/UX prototipleri
4. Veri analizi örnekleri
5. QA test senaryoları

📦 Kurulum
pip install Faker

📚 Kaynaklar
- https://faker.readthedocs.io/
- https://github.com/joke2k/faker
- https://pypi.org/project/Faker/
"""

# 👩‍💻 Uygulamalı Örnek Kod

from faker import Faker

# Türkçe veriler için
fake = Faker("tr_TR")

# Sabit veri üretimi için seed
Faker.seed(42)

# 👤 Kişisel Bilgiler
print("👤 Kişisel Bilgiler")
print("İsim Soyisim :", fake.name())
print("E-posta      :", fake.email())
print("Telefon      :", fake.phone_number())
print("Doğum Tarihi :", fake.date_of_birth(minimum_age=18, maximum_age=65))
print("TC Kimlik No :", fake.ssn())
print()

# 📍 Adres Bilgileri
print("📍 Adres Bilgileri")
print("Adres         :", fake.address())
print("Şehir         :", fake.city())
print("Posta Kodu    :", fake.postcode())
print("Ülke          :", fake.country())
print()

# 💼 İş Bilgileri
print("💼 İş Bilgileri")
print("Şirket        :", fake.company())
print("Meslek        :", fake.job())
print("Departman     :", fake.bs().title())
print("Pozisyon      :", fake.catch_phrase())
print()

# 📅 Tarih ve Saat
print("📅 Tarih ve Saat")
print("Tarih         :", fake.date())
print("Saat          :", fake.time())
print("Timestamp     :", fake.date_time())
print()

# 🔢 Sayısal Veriler
print("🔢 Sayısal Veriler")
print("Puan          :", fake.random_int(min=0, max=100))
print("ID            :", fake.random_number(digits=5))
print()
