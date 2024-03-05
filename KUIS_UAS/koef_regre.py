# import pandas as pd
# import numpy as np

# # Ambil 100 data dan 5 variabel numerik dari DataFrame
# data = pd.read_csv('train.csv')
# selected_data = data.sample(n=100)  # Gantilah 'your_data' dengan nama DataFrame Anda
# # selected_variables = selected_data[['GrLivArea', 'GarageArea', 'LotArea', 'MSSubClass', 'MasVnrArea']]
# selected_variables = selected_data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]

# # Hitung matriks X
# X = np.c_[np.ones(selected_data.shape[0]), selected_variables]

# # Hitung transpos dari matriks X
# X_transpose = X.T

# # Hitung matriks X'X dan X'Y
# XtX = np.dot(X_transpose, X)
# XtY = np.dot(X_transpose, selected_data['SalePrice'])

# # Hitung invers dari matriks X'X
# XtX_inv = np.linalg.inv(XtX)

# # Hitung koefisien regresi
# coefficients = np.dot(XtX_inv, XtY)

# print("Koefisien Regresi:")
# print(coefficients)


import pandas as pd
import numpy as np

# Ambil 1000 data dan 10 variabel numerik dari DataFrame
data = pd.read_csv('data_cleaned1.csv')
selected_data = data.sample(n=1000)  
selected_variables = selected_data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'EnclosedPorch', 'TotalBsmtSF', 'WoodDeckSF', 'OpenPorchSF', '1stFlrSF', '2ndFlrSF']]

# Hitung matriks X
X = np.c_[np.ones(selected_data.shape[0]), selected_variables]
# Hitung transpos dari matriks X
X_transpose = X.T
# Hitung matriks X'X dan X'Y
XtX = np.dot(X_transpose, X)
XtY = np.dot(X_transpose, selected_data['SalePrice'])
# Hitung invers dari matriks X'X
XtX_inv = np.linalg.inv(XtX)
# Hitung koefisien regresi
coefficients = np.dot(XtX_inv, XtY)

print("Koefisien Regresi:")
print(coefficients)

# import pandas as pd
# import numpy as np

# # Ambil 100 data dan 5 variabel numerik dari DataFrame
# data = pd.read_csv('data_cleaned1.csv')
# selected_data = data.head(100)  
# selected_variables = selected_data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]

# # Hitung matriks X
# X = np.c_[np.ones(selected_data.shape[0]), selected_variables]
# # Hitung transpos dari matriks X
# X_transpose = X.T
# # Hitung matriks X'X dan X'Y
# XtX = np.dot(X_transpose, X)
# XtY = np.dot(X_transpose, selected_data['SalePrice'])
# # Hitung invers dari matriks X'X
# XtX_inv = np.linalg.inv(XtX)
# # Hitung koefisien regresi
# coefficients = np.dot(XtX_inv, XtY)

# print("Koefisien Regresi:")
# print(coefficients)

# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import StandardScaler

# # Ambil 100 data dan 5 variabel numerik dari DataFrame
# data = pd.read_csv('train.csv')
# selected_data = data.sample(n=100)  # Gantilah 'your_data' dengan nama DataFrame Anda
# selected_variables = selected_data[['GrLivArea', 'GarageArea', 'LotArea', 'MasVnrArea', 'TotalBsmtSF']]

# # Normalisasi variabel-variabel numerik
# scaler = StandardScaler()
# selected_variables_normalized = scaler.fit_transform(selected_variables)

# # Tambahkan kolom bias (intercept)
# X = np.c_[np.ones(selected_data.shape[0]), selected_variables_normalized]

# # Hitung transpos dari matriks X
# X_transpose = X.T

# # Hitung matriks X'X dan X'Y
# XtX = np.dot(X_transpose, X)
# XtY = np.dot(X_transpose, selected_data['SalePrice'])

# # Hitung invers dari matriks X'X
# XtX_inv = np.linalg.inv(XtX)

# # Hitung koefisien regresi
# coefficients = np.dot(XtX_inv, XtY)

# print("Koefisien Regresi setelah Normalisasi:")
# print(coefficients)
