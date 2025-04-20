'''
Proje Başlığı: "İşe Alımda Aday Seçimi: SVM ile Başvuru Değerlendirme"
Senaryo: Bir teknoloji firmasında insan kaynakları ekibindesiniz. Amacınız, yazılım geliştirici pozisyonu için başvuran adayların tecrübe yılı ve teknik sınav puanına göre işe alınıp alınmamasını tahmin eden bir model geliştirmek.

Veri Özellikleri: Her başvuru için şu bilgiler vardır:
tecrube_yili: Adayın toplam yazılım deneyimi (0–10 yıl arası)
teknik_puan: Teknik sınavdan alınan puan (0–100 arası)

etiket:
1: İşe alınmadı (başarısız aday)
0: İşe alındı (başarılı aday)

Etiketleme Kriteri (kural tabanlı):
Tecrübesi 2 yıldan az ve sınav puanı 60'tan düşük olanlar işe alınmıyor.
'''

import numpy as np #sayılsal işlemlerde kullanılır
import pandas as pd #dataframe oluşturup işlem yapmak amacıyla kullanılır
from faker import Faker #sahte veri üretimi
from sklearn.model_selection import train_test_split #veriyi eğitim ve test olarak bölmek için
from sklearn.preprocessing import StandardScaler # veri ölçekleme
from sklearn.svm import SVC #svm modeli
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report #mdoel değerlendirmesi
import matplotlib.pyplot as plt #grafik çizmek için


#Görevler: Faker ya da random ile en az 200 başvuru verisi üret.
#faker nesnesi oluşturulur
fake = Faker('tr_TR')
def generate_recruitment_data(n_samples=200):

    data = []
    for _ in range(n_samples):
        tecrube_yili = fake.random_int(min=0, max=10)
        teknik_puan = fake.random_int(min=0, max=100)
        

        #Tecrübe ve teknik puana göre yukarıdaki kuralla etiketle.
        if tecrube_yili < 2 and teknik_puan < 60:
            etiket = 1  #işe alınmadı

        else:
            etiket = 0  # işe alındı

        data.append([tecrube_yili, teknik_puan, etiket])


    
    return pd.DataFrame(data, columns=['tecrube_yili', 'teknik_puan', 'etiket'])



#veri setini oluşturalım
df = generate_recruitment_data()
print(f"Üretilen veri sayısı: {len(df)}")
print("\nVeri örneği:")
print(df.head())

#Veriyi eğitim ve test olarak ayır.
print("\n2. Veri Bölme:")
X = df[['tecrube_yili', 'teknik_puan']]
y = df['etiket']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Eğitim seti boyutu: {len(X_train)}")
print(f"Test seti boyutu: {len(X_test)}")

#Veriyi StandardScaler ile ölçekle.
print("\n3. Veri Ölçekleme:")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Ölçekleme tamamlandı")

#SVC(kernel='linear') ile modeli eğit.
print("\n4. Model Eğitimi:")
model = SVC(kernel='linear', probability=True)
model.fit(X_train_scaled, y_train)
print("Model eğitimi tamamlandı")

#Karar sınırını matplotlib ile görselleştir.
def plot_decision_boundary():
    plt.figure(figsize=(10, 6))
    x_min, x_max = X_train_scaled[:, 0].min() - 1, X_train_scaled[:, 0].max() + 1
    y_min, y_max = X_train_scaled[:, 1].min() - 1, X_train_scaled[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_train, alpha=0.8)
    plt.xlabel('Tecrübe Yılı (Ölçeklenmiş)')
    plt.ylabel('Teknik Puan (Ölçeklenmiş)')
    plt.title('SVM Karar Sınırı')
    plt.show()

print("\n5. Karar Sınırı Görselleştirmesi:")
plot_decision_boundary()

#Kullanıcıdan tecrübe ve teknik puan alarak tahmin yap.
def predict_candidate():
    print("\n6. Aday Değerlendirme:")
    try:
        tecrube_yili = float(input("Tecrübe yılı (0-10): "))
        teknik_puan = float(input("Teknik puan (0-100): "))
        
        if not (0 <= tecrube_yili <= 10 and 0 <= teknik_puan <= 100):
            print("Hata: Değerler aralık dışında!")
            return
        
        #veri ölçekleme aşaması
        input_data = scaler.transform([[tecrube_yili, teknik_puan]])
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        result = "İşe Alınmadı" if prediction == 1 else "İşe Alındı"
        print(f"\nTahmin Sonucu: {result}")
        print(f"İşe Alınma Olasılığı: {probability[0]:.2%}")
        print(f"İşe Alınmama Olasılığı: {probability[1]:.2%}")
        
    except ValueError:
        print("Hata: Lütfen geçerli sayısal değerler girin!")

# Kullanıcıdan tahmin için girdi al
predict_candidate()

#accuracy_score, confusion_matrix, classification_report ile başarıyı değerlendir.
print("\n7. Model Performans Değerlendirmesi:")
y_pred = model.predict(X_test_scaled)

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred)) 