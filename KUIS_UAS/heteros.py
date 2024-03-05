import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data_cleaned1.csv')  
y_variable = data['SalePrice'] 
X_variables = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']] 

# Menambahkan konstanta untuk model regresi
X_variables = sm.add_constant(X_variables)

# Membuat model regresi
model = sm.OLS(y_variable, X_variables).fit()

# Melakukan uji White (Breusch-Pagan) untuk heteroskedastisitas
het_white_stat, het_white_p_value, het_white_fstat, het_white_p_value_fstat = het_white(model.resid, X_variables)
print(f'White Test Statistic: {het_white_stat}')
print(f'White Test P-value: {het_white_p_value}')

# Visualisasi residual plot untuk mendeteksi pola heteroskedastisitas
plt.figure(figsize=(10, 6))
sns.scatterplot(x=model.fittedvalues, y=model.resid)
plt.title('Residual Plot untuk Deteksi Heteroskedastisitas')
plt.xlabel('Nilai Prediksi')
plt.ylabel('Residuals')
plt.show()

# Interpretasi hasil uji heteroskedastisitas
alpha = 0.05
if het_white_p_value < alpha:
    print('Terdapat bukti yang cukup untuk menolak H0, sehingga data menunjukkan tanda-tanda heteroskedastisitas.')
else:
    print('Tidak ada bukti yang cukup untuk menolak H0, sehingga tidak terdapat tanda-tanda heteroskedastisitas pada data.')


# import numpy as np
# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.stats.diagnostic import het_white
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler

# # Membaca data dari CSV
# data = pd.read_csv('train.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# # Menangani nilai-nilai hilang
# data = data.dropna()  # Menghapus baris yang memiliki nilai-nilai NaN

# # Mengekstrak variabel dependen dan independen
# y_variable = data['SalePrice']  # Gantilah 'nama_variabel_dependen' dengan nama variabel dependen yang sesuai
# X_variables = data[['MSSubClass', 'LotFrontage', 'LotArea']]  # Gantilah dengan variabel-variabel independen yang sesuai

# # Mengatasi nilai infinity (jika ada)
# X_variables.replace([np.inf, -np.inf], np.nan, inplace=True)
# y_variable.replace([np.inf, -np.inf], np.nan, inplace=True)

# # Menangani nilai-nilai hilang setelah mengatasi infinity
# X_variables = X_variables.dropna()
# y_variable = y_variable[X_variables.index]  # Menyesuaikan indeks y_variable dengan indeks X_variables

# # Menambahkan konstanta untuk model regresi
# X_variables = sm.add_constant(X_variables)

# # Membuat model regresi
# model = sm.OLS(y_variable, X_variables).fit()

# # Melakukan uji White (Breusch-Pagan) untuk heteroskedastisitas
# het_white_stat, het_white_p_value, het_white_fstat, het_white_p_value_fstat = het_white(model.resid, X_variables)
# print(f'White Test Statistic: {het_white_stat}')
# print(f'White Test P-value: {het_white_p_value}')

# # Visualisasi residual plot untuk mendeteksi pola heteroskedastisitas
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=model.fittedvalues, y=model.resid)
# plt.title('Residual Plot untuk Deteksi Heteroskedastisitas')
# plt.xlabel('Nilai Prediksi')
# plt.ylabel('Residuals')
# plt.show()

# # Interpretasi hasil uji heteroskedastisitas
# alpha = 0.05
# if het_white_p_value < alpha:
#     print('Terdapat bukti yang cukup untuk menolak H0, sehingga data menunjukkan tanda-tanda heteroskedastisitas.')
# else:
#     print('Tidak ada bukti yang cukup untuk menolak H0, sehingga tidak terdapat tanda-tanda heteroskedastisitas pada data.')

# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.stats.diagnostic import het_white
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Membaca data dari CSV
# data = pd.read_csv('data_cleaned.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# # Mengekstrak variabel dependen dan independen
# y_variable = data['SalePrice']  # Gantilah 'nama_variabel_dependen' dengan nama variabel dependen yang sesuai
# X_variables = data[['MSSubClass', 'LotFrontage', 'LotArea']]  # Gantilah dengan variabel-variabel independen yang sesuai

# # Hapus baris yang memiliki nilai-nilai kosong
# data = data.dropna()

# # Cek apakah masih ada data yang tersisa
# if len(data) < 2:
#     print("Dataset tidak memiliki data yang cukup untuk dianalisis.")
# else:
#     # Menambahkan konstanta untuk model regresi
#     X_variables = sm.add_constant(X_variables)

#     # Membuat model regresi
#     model = sm.OLS(y_variable, X_variables).fit()

#     # Melakukan uji White (Breusch-Pagan) untuk heteroskedastisitas
#     het_white_stat, het_white_p_value, het_white_fstat, het_white_p_value_fstat = het_white(model.resid, X_variables)
#     print(f'White Test Statistic: {het_white_stat}')
#     print(f'White Test P-value: {het_white_p_value}')

#     # Visualisasi residual plot untuk mendeteksi pola heteroskedastisitas
#     plt.figure(figsize=(10, 6))
#     sns.scatterplot(x=model.fittedvalues, y=model.resid)
#     plt.title('Residual Plot untuk Deteksi Heteroskedastisitas')
#     plt.xlabel('Nilai Prediksi')
#     plt.ylabel('Residuals')
#     plt.show()

#     # Interpretasi hasil uji heteroskedastisitas
#     alpha = 0.05
#     if het_white_p_value < alpha:
#         print('Terdapat bukti yang cukup untuk menolak H0, sehingga data menunjukkan tanda-tanda heteroskedastisitas.')
#     else:
#         print('Tidak ada bukti yang cukup untuk menolak H0, sehingga tidak terdapat tanda-tanda heteroskedastisitas pada data.')


# import pandas as pd
# import statsmodels.api as sm
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Membaca data dari CSV
# data = pd.read_csv('data_cleaned1.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# # Pilih variabel dependen dan independen yang akan digunakan untuk model regresi
# y_variable = data['SalePrice']  # Gantilah 'SalePrice' dengan nama variabel dependen yang sesuai
# X_variables = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]  # Gantilah dengan variabel-variabel independen yang sesuai

# # Menambahkan konstanta untuk model regresi
# X_variables = sm.add_constant(X_variables)

# # Membuat model regresi
# model = sm.OLS(y_variable, X_variables).fit()

# # Menghitung residu
# residuals = model.resid

# # Membuat scatter plot antara nilai prediksi dan residu
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=model.fittedvalues, y=residuals)
# plt.title('Residual Plot untuk Deteksi Heteroskedastisitas')
# plt.xlabel('Nilai Prediksi')
# plt.ylabel('Residuals')
# plt.show()

# # Interpretasi hasil visualisasi
# print("Jika pola pada scatter plot menunjukkan adanya pola lebar atau menyempit, ini dapat menunjukkan adanya heteroskedastisitas.")


# import pandas as pd
# import statsmodels.api as sm
# import seaborn as sns
# import matplotlib.pyplot as plt


# train = pd.read_csv('train.csv') 

# ## Plot sizing. 
# fig, (ax1, ax2) = plt.subplots(figsize = (12,8), ncols=2,sharey=False)
# ## Scatter plotting for SalePrice and GrLivArea. 
# sns.scatterplot( x = train.GrLivArea, y = train.SalePrice,  ax=ax1)
# ## Putting a regression line. 
# sns.regplot(x=train.GrLivArea, y=train.SalePrice, ax=ax1)

# ## Scatter plotting for SalePrice and MasVnrArea. 
# sns.scatterplot(x = train.MasVnrArea,y = train.SalePrice, ax=ax2)
# ## regression line for MasVnrArea and SalePrice. 
# sns.regplot(x=train.MasVnrArea, y=train.SalePrice, ax=ax2)
# plt.show()