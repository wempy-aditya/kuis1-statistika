import pandas as pd
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari CSV
data = pd.read_csv('./train.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# Mengekstrak variabel dependen
y_variable = data['SalePrice']  # Gantilah 'nama_variabel_dependen' dengan nama variabel dependen yang sesuai

# Uji Normalitas dengan Shapiro-Wilk
stat, p_value = shapiro(y_variable)

# Menampilkan hasil uji normalitas
print(f'Statistik Uji: {stat}')
print(f'P-value: {p_value}')

# Membuat histogram dan kurva distribusi normal
plt.figure(figsize=(10, 6))

# Histogram
sns.histplot(y_variable, kde=True, color='blue', bins=30)
plt.title('Histogram dan Kurva Distribusi Normal')
plt.xlabel('Nilai Variabel Dependan')
plt.ylabel('Frekuensi')

# Menambahkan kurva distribusi normal
plt.axvline(x=y_variable.mean(), color='red', linestyle='--', label='Mean')
plt.legend()

# Menampilkan plot
plt.show()

# Interpretasi hasil uji normalitas
alpha = 0.05
if p_value > alpha:
    print('Tidak ada bukti yang cukup untuk menolak H0, sehingga data terdistribusi normal.')
else:
    print('Terdapat bukti yang cukup untuk menolak H0, sehingga data tidak terdistribusi normal.')
