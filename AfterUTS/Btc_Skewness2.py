import pandas as pd
from scipy.stats import skew

# Membaca data dari file CSV
file_path = './coin_Bitcoin.csv' 
df = pd.read_csv(file_path)

# Daftar nama kolom yang ingin diuji skewness-nya
kolom_uji_skewness = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# Melakukan Uji Skewness pada Kolom Tertentu
skewness_kolom_tertentu = df[kolom_uji_skewness].apply(skew)

# Menampilkan Hasil Uji Skewness
print("Skewness pada Kolom Tertentu:")
print(skewness_kolom_tertentu)

# Menentukan Kolom yang Perlu Dinormalisasi
kolom_perlu_dinormalisasi = skewness_kolom_tertentu[abs(skewness_kolom_tertentu) > 1].index

print("\nKolom yang Perlu Dinormalisasi:")
print(kolom_perlu_dinormalisasi)
