# import pandas as pd
# import statsmodels.api as sm
# import matplotlib.pyplot as plt
# from statsmodels.graphics.tsaplots import plot_acf

# # Membaca data dari CSV
# data = pd.read_csv('train.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# # Pilih variabel dependen dan independen yang akan digunakan untuk model regresi
# y_variable = data['SalePrice']  # Gantilah 'SalePrice' dengan nama variabel dependen yang sesuai
# X_variables = data[['GrLivArea', 'GarageArea']]  # Gantilah dengan variabel-variabel independen yang sesuai

# # Menambahkan konstanta untuk model regresi
# X_variables = sm.add_constant(X_variables)

# # Membuat model regresi
# model = sm.OLS(y_variable, X_variables).fit()

# # Menghitung residu
# residuals = model.resid

# # Membuat correlogram untuk mendeteksi autocorrelation pada residual
# plot_acf(residuals, lags=80)  # Gantilah 'lags' sesuai kebutuhan
# plt.title('Correlogram untuk Autocorrelation pada Residuals')
# plt.xlabel('Lag')
# plt.ylabel('Autocorrelation')
# plt.show()

# # Interpretasi hasil visualisasi
# print("Jika ada garis yang signifikan di luar interval putus-putus biru, ini dapat menunjukkan adanya autocorrelation pada residual.")


# import pandas as pd
# import numpy as np
# import statsmodels.api as sm
# import matplotlib.pyplot as plt

# # Membaca data dari file CSV
# data = pd.read_csv('data_cleaned1.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV Anda

# # Menentukan variabel independen dan dependen
# # Gantilah 'variabel_dependen' dan 'variabel_independen' sesuai dengan nama variabel dalam dataset Anda
# variabel_dependen = data['SalePrice']
# variabel_independen = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]

# # Menambahkan konstanta ke variabel independen
# X = sm.add_constant(variabel_independen)

# # Membuat model regresi
# model = sm.OLS(variabel_dependen, X).fit()

# # Menghitung residu (kesalahan)
# residuals = model.resid

# # Membuat plot residu
# plt.figure(figsize=(8, 4))
# plt.plot(residuals)
# plt.title('Plot Residu')
# plt.xlabel('Observasi')
# plt.ylabel('Residu')
# plt.show()

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('data_cleaned1.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV Anda

# Menentukan variabel independen dan dependen
# Gantilah 'variabel_dependen' dan 'variabel_independen' sesuai dengan nama variabel dalam dataset Anda
variabel_dependen = data['SalePrice']
variabel_independen = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]

# Menambahkan konstanta ke variabel independen
X = sm.add_constant(variabel_independen)

# Membuat model regresi
model = sm.OLS(variabel_dependen, X).fit()

# Menghitung residu (kesalahan)
residuals = model.resid

# Membuat plot residu
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(residuals)
plt.title('Plot Residu')
plt.xlabel('Observasi')
plt.ylabel('Residu')

# Melakukan uji Durbin-Watson
durbin_watson_statistic = sm.stats.stattools.durbin_watson(residuals)

# Menampilkan hasil uji
plt.subplot(1, 2, 2)
plt.text(0.1, 0.9, f'Durbin-Watson Statistic: {durbin_watson_statistic:.2f}', transform=plt.gcf().transFigure)
plt.axis('off')

# Menampilkan plot dan hasil uji
plt.show()

# Interpretasi hasil uji
if durbin_watson_statistic < 1.5:
    print('Indikasi positif autokorelasi (residuals cenderung positif terkorelasi).')
elif durbin_watson_statistic > 2.5:
    print('Indikasi negatif autokorelasi (residuals cenderung negatif terkorelasi).')
else:
    print('Tidak ada indikasi autokorelasi yang signifikan.')
