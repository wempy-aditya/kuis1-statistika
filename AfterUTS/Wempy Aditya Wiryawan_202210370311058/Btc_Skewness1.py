# ==========================================
# UJI SKEWNESS SETELAH DILAKUKAN NORMALISASI
# ==========================================


import pandas as pd
from scipy.stats import skew

# Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv' 
# file_path = './BTC_NORMALIZED.csv' 
file_path = './BTC_NORMALIZED_ZSCORE.csv' 
df = pd.read_csv(file_path)

# Daftar nama kolom yang ingin diuji skewness-nya
kolom_uji_skewness = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# Melakukan Uji Skewness pada Kolom Tertentu
skewness_kolom_tertentu = df[kolom_uji_skewness].apply(skew)

# Menampilkan Hasil
print("Skewness pada Kolom Tertentu:")
print(skewness_kolom_tertentu)


# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import skew

# # Membaca data dari file CSV
# # file_path = './coin_Bitcoin.csv' 
# file_path = './BTC_NORMALIZED.csv' 
# df = pd.read_csv(file_path)

# # Daftar nama kolom yang ingin diuji skewness-nya
# kolom_uji_skewness = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Melakukan Uji Skewness pada Kolom Tertentu
# skewness_kolom_tertentu = df[kolom_uji_skewness].apply(skew)

# # Membuat Plot Skewness
# plt.figure(figsize=(10, 6))
# skewness_kolom_tertentu.plot(kind='bar', color='blue')
# plt.title('Uji Skewness pada Kolom di Data Crypto')
# plt.xlabel('NamaKolom')
# plt.ylabel('Skewness')
# plt.show()
