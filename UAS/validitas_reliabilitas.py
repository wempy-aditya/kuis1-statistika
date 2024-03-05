# import pandas as pd
# import statsmodels.api as sm
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from factor_analyzer import FactorAnalyzer

# # Membaca data dari file CSV
# data = pd.read_csv('Data_UAS_Statistik.csv')  # Gantilah 'data.csv' dengan nama file CSV Anda

# # Korelasi antar variabel
# correlation_matrix = data.corr()

# # Tampilkan matriks korelasi
# print("Matriks Korelasi:")
# print(correlation_matrix)

# # Uji Hubungan Antara Variabel 'Interaction' dan 'Power'
# X = data['Interaction']
# Y = data['Power']
# X = sm.add_constant(X)
# model = sm.OLS(Y, X).fit()
# print("\nRingkasan Model Regresi:")
# print(model.summary())

# # Uji Faktor Analisis untuk Validitas dan Reliabilitas
# # Memilih variabel yang akan diuji
# variables_for_factor_analysis = ['Interaction', 'Residences', 'Knowledge', 'Rainfall', 'Humidity', 'Temperature']

# # Membuat matriks faktor analisis
# factor_analyzer = FactorAnalyzer(n_factors=3, rotation='varimax')
# factor_analyzer.fit(data[variables_for_factor_analysis])

# # Tampilkan hasil faktor analisis
# print("\nFaktor Analisis:")
# print(pd.DataFrame(factor_analyzer.loadings_, index=variables_for_factor_analysis))

# # Pisahkan data menjadi data latih dan data uji
# train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# # Melatih model regresi pada data latih
# X_train = train_data[['Interaction', 'Residences', 'Knowledge', 'Rainfall', 'Humidity', 'Temperature']]
# Y_train = train_data['Power']
# model_reg = LinearRegression().fit(X_train, Y_train)

# # Melakukan prediksi pada data uji
# X_test = test_data[['Interaction', 'Residences', 'Knowledge', 'Rainfall', 'Humidity', 'Temperature']]
# Y_pred = model_reg.predict(X_test)

# # Mengukur reliabilitas model regresi
# mse = mean_squared_error(test_data['Power'], Y_pred)
# print("\nMSE (Mean Squared Error):", mse)


import pandas as pd
from factor_analyzer import FactorAnalyzer
from sklearn.preprocessing import StandardScaler
from factor_analyzer.factor_analyzer import calculate_kmo

# Membaca data dari CSV
data = pd.read_csv('Data_UAS_Statistik.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# Memilih kolom untuk analisis faktor
selected_columns = ['Interaction', 'Residences', 'Knowledge', 'Rainfall', 'Humidity', 'Temperature', 'Power']
df = data[selected_columns]

# Standardisasi data
scaler = StandardScaler()
df_standardized = scaler.fit_transform(df)

# Faktor Analisis
factor_analyzer = FactorAnalyzer(n_factors=3, rotation='varimax')
factor_analyzer.fit(df_standardized)

# Korelasi antar variabel
correlation_matrix = df.corr()

# Menghitung KMO (Kaiser-Meyer-Olkin)
kmo_all, kmo_model = calculate_kmo(df_standardized)

# Menampilkan hasil
print("Matriks Korelasi:")
print(correlation_matrix)

print("\nKMO (Kaiser-Meyer-Olkin):", kmo_model)
