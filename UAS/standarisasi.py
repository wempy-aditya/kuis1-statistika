import pandas as pd
from sklearn.preprocessing import StandardScaler

# Baca data dari file CSV
data = pd.read_csv("Data_UAS_Statistik.csv")

# Kolom-kolom yang akan di-standarisasi
columns_to_standardize = ['Interaction', 'Residences', 'Knowledge', 'Rainfall', 'Humidity', 'Temperature', 'Power']

# Inisialisasi objek StandardScaler
scaler = StandardScaler()

# Lakukan standardisasi pada kolom-kolom yang diinginkan
data[columns_to_standardize] = scaler.fit_transform(data[columns_to_standardize])

# Simpan data setelah standardisasi ke dalam file CSV
data.to_csv("Data_Standarisasi.csv", index=False)

# Tampilkan data setelah standardisasi
print("Data setelah standardisasi:")
print(data.head())
