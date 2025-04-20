import numpy as np
import pandas as pd
from faker import Faker
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Faker nesnesi oluştur
fake = Faker('tr_TR')

# Veri üretme fonksiyonu
def generate_recruitment_data(n_samples=200):
    data = []
    
    for _ in range(n_samples):
        tecrube_yili = fake.random_int(min=0, max=10)
        teknik_puan = fake.random_int(min=0, max=100)
        
        # Etiketleme kriteri
        if tecrube_yili < 2 and teknik_puan < 60:
            etiket = 1  # İşe alınmadı
        else:
            etiket = 0  # İşe alındı
            
        data.append([tecrube_yili, teknik_puan, etiket])
    
    return pd.DataFrame(data, columns=['tecrube_yili', 'teknik_puan', 'etiket'])

# Veri setini oluştur
df = generate_recruitment_data()

# Veriyi eğitim ve test setlerine ayır
X = df[['tecrube_yili', 'teknik_puan']]
y = df['etiket']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Veriyi ölçekle
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# SVM modelini eğit
model = SVC(kernel='linear')
model.fit(X_train_scaled, y_train)

# Tahminler
y_pred = model.predict(X_test_scaled)

# Model performansını değerlendir
print("\nModel Performansı:")
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Karar sınırını görselleştir
def plot_decision_boundary():
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

# Karar sınırını çiz
plot_decision_boundary()

# Kullanıcıdan girdi alarak tahmin yapma fonksiyonu
def predict_candidate(tecrube_yili, teknik_puan):
    # Veriyi ölçekle
    input_data = scaler.transform([[tecrube_yili, teknik_puan]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    result = "İşe Alınmadı" if prediction == 1 else "İşe Alındı"
    print(f"\nTahmin Sonucu: {result}")
    print(f"İşe Alınma Olasılığı: {probability[0]:.2%}")
    print(f"İşe Alınmama Olasılığı: {probability[1]:.2%}")

# Örnek tahmin
print("\nÖrnek Tahmin:")
predict_candidate(tecrube_yili=3, teknik_puan=75) 