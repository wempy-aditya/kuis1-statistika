import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import zscore

# Baca data dari file CSV
data = pd.read_csv("Data_UAS_Statistik.csv")

# Pilih variabel independen (features) dan variabel dependen (target)
X = data[['Interaction', 'Residences', 'Knowledge', 'Rainfall', 'Humidity', 'Temperature']]
y = data['Power']

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model regresi linear
model = LinearRegression()

# Latih model pada data latih
model.fit(X_train, y_train)

# Prediksi daya pada data uji
y_pred = model.predict(X_test)

# Evaluasi performa model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Tampilkan hasil evaluasi
print("Mean Squared Error:", mse)
print("R-squared (R2) Score:", r2)

# Tampilkan koefisien model
print("Koefisien Model:", model.coef_)
print("Intercept Model:", model.intercept_)

# Hitung residual
residual = y_test - y_pred

# Plot histogram residual
plt.hist(residual, bins=20, edgecolor='black')
plt.title('Histogram Residual')
plt.xlabel('Residual')
plt.ylabel('Frekuensi')
plt.show()

# Hitung Z-score untuk residual
z_scores = zscore(residual)

# Tentukan batas Z-score untuk outlier
threshold = 3

# Identifikasi dan tampilkan outlier
outlier_indices = z_scores[abs(z_scores) > threshold].index
print("Outlier Indices:", outlier_indices)
