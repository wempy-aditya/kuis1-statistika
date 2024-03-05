# import pandas as pd
# import statsmodels.api as sm

# data = pd.read_csv('data_cleaned1.csv') 
# X = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]   # variabel independen 
# Y = data['SalePrice']  # variabel dependen 
# # Tambahkan kolom bias (intercept) ke matriks X
# X = sm.add_constant(X)
# # Buat model regresi
# model = sm.OLS(Y, X).fit()
# # Hitung uji F-statistik dan p-value
# f_statistic = model.fvalue
# p_value = model.f_pvalue
# # Tampilkan hasil uji simultan regresi
# print(f"Uji Simultan Regresi (F-statistik): {f_statistic}")
# print(f"P-Value: {p_value}")

# # Interpretasi
# if p_value < 0.05:
#     print("Keseluruhan model regresi signifikan secara statistik.")
# else:
#     print("Tidak cukup bukti untuk menolak hipotesis nol. Model regresi mungkin tidak signifikan secara keseluruhan.")


import pandas as pd
import statsmodels.api as sm

# Membaca data dari file CSV
data = pd.read_csv('data_cleaned1.csv') 
X = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]   # variabel independen 
Y = data['SalePrice']  # variabel dependen 

# Menambahkan konstanta untuk model regresi
X = sm.add_constant(X)

# Membuat model regresi
model = sm.OLS(Y, X).fit()

# Melakukan uji simultan regresi (F-test)
f_test = model.f_test("GrLivArea = GarageArea = LotArea = MasVnrArea = TotalBsmtSF = 0")

# Menampilkan hasil uji simultan regresi
print("Hasil Uji Simultan Regresi:")
print(f_test)

# Mencetak summary model regresi
print("\nSummary Model Regresi:")
print(model.summary())