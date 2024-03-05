import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('data_cleaned1.csv')  

X = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]  # variabel independen 
Y = data['SalePrice']  # variabel dependen 

# Tambahkan kolom bias (intercept) ke matriks X
X = sm.add_constant(X)

# Buat model regresi
model = sm.OLS(Y, X).fit()

# Hitung t-statistik dan p-value untuk masing-masing koefisien
t_statistic = model.tvalues
p_values = model.pvalues

# Tampilkan hasil uji parsial regresi
results = pd.DataFrame({'Koefisien': model.params, 't-Statistic': t_statistic, 'P-Value': p_values})
print(results)
