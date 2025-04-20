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
#fake = Faker('tr_TR')

np.random.seed(42) #her seferinde aynı verileri kullanmak için seed komutu kulanılır
#veri üretimi
def generate_recruitment_data(n_samples=200):
    data = []
    for _ in range(n_samples):
        tecrube_yili = np.random.randint(0, 11)  #0-10 arası
        teknik_puan = np.random.randint(0, 101)  # 0-100 arası
        
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
    
    #orijinal değerler üzerinden
    x_min, x_max = X['tecrube_yili'].min() - 0.5, X['tecrube_yili'].max() + 0.5
    y_min, y_max = X['teknik_puan'].min() - 5, X['teknik_puan'].max() + 5
    

    #grid gösterimi
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                        np.arange(y_min, y_max, 1))
    
    #grid ölçeklenmesi
    grid_scaled = scaler.transform(np.c_[xx.ravel(), yy.ravel()])
    
    
    # Tahmin yap
    Z = model.predict(grid_scaled)
    Z = Z.reshape(xx.shape)
    
    # Grafiği çiz
    plt.contourf(xx, yy, Z, alpha=0.4)
    
    # Orijinal veri noktalarını çiz
    plt.scatter(X['tecrube_yili'], X['teknik_puan'], c=y, alpha=0.8)
    
    plt.xlabel('Tecrübe Yılı')
    plt.ylabel('Teknik Puan')
    plt.title('SVM Karar Sınırı')
    
    # Eksenleri düzenle
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    
    # Kriter çizgilerini ekle
    plt.axvline(x=2, color='r', linestyle='--', alpha=0.3)
    plt.axhline(y=60, color='r', linestyle='--', alpha=0.3)
    
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

#Gelişim Alanları: Kernel değiştirerek doğrusal olmayan sınıfları da deneme
print("\n8. Farklı Kernel'ların Karşılaştırması:")
kernels = ['linear', 'rbf', 'poly', 'sigmoid']

kernel_scores = {}



plt.figure(figsize=(15, 10))
for i, kernel in enumerate(kernels, 1):
    print(f"\n{kernel.upper()} Kernel:")
    
    kernel_model = SVC(kernel=kernel, probability=True)
    kernel_model.fit(X_train_scaled, y_train)
    
    y_pred_kernel = kernel_model.predict(X_test_scaled)
    score = accuracy_score(y_test, y_pred_kernel)
    kernel_scores[kernel] = score
    print(f"Accuracy: {score:.4f}")
    
    plt.subplot(2, 2, i)


    
    x_min, x_max = X['tecrube_yili'].min() - 0.5, X['tecrube_yili'].max() + 0.5
    y_min, y_max = X['teknik_puan'].min() - 5, X['teknik_puan'].max() + 5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                        np.arange(y_min, y_max, 1))
    
    grid_scaled = scaler.transform(np.c_[xx.ravel(), yy.ravel()])
    Z = kernel_model.predict(grid_scaled)
    Z = Z.reshape(xx.shape)


    
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X['tecrube_yili'], X['teknik_puan'], c=y, alpha=0.8)
    

    plt.xlabel('Tecrübe Yılı')
    plt.ylabel('Teknik Puan')
    plt.title(f'Kernel: {kernel}\nAccuracy: {score:.4f}')
    
    plt.axvline(x=2, color='r', linestyle='--', alpha=0.3)
    plt.axhline(y=60, color='r', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()



#enn iyi kernelin bulunup yazdırılması
best_kernel = max(kernel_scores, key=kernel_scores.get)
print(f"\nEn iyi performans gösteren kernel: {best_kernel}")
print("\nTüm kernel performansları:")
for kernel, score in kernel_scores.items():
    print(f"{kernel}: {score:.4f}") 