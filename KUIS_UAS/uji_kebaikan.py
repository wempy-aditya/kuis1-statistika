import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('data_cleaned1.csv')  

X = data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]  # variabel independen 
Y = data['SalePrice']  # variabel dependen 

# Tambahkan kolom bias (intercept) ke matriks X
X = sm.add_constant(X)

# Buat model regresi
model = sm.OLS(Y, X).fit()

# Dapatkan nilai R²
r_squared = model.rsquared

# Tampilkan nilai R²
print(f"Nilai R-squared (R²): {r_squared}")
