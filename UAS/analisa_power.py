import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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

# Tampilkan koefisien dan intercept model
print("Koefisien Model:", model.coef_)
print("Intercept Model:", model.intercept_)
