# import pandas as pd
# import numpy as np
# import pingouin as pg

# # Baca data dari file CSV
# data = pd.read_csv("Data_UAS_Statistik.csv")

# # Analisis korelasi
# korelasi_matrix = data.corr()

# # Tampilkan matriks korelasi
# print("Matriks Korelasi:")
# print(korelasi_matrix)

# # Analisis reliabilitas (alpha Cronbach)
# alpha_cronbach = pg.cronbach_alpha(data)
# print("\nAlpha Cronbach:")
# print(alpha_cronbach)


import pandas as pd

# Baca data dari file CSV
data = pd.read_csv("Data_UAS_Statistik.csv")

# Statistika deskriptif daya tertinggi
daya_tertinggi = data['Power'].max()
print("Daya Tertinggi:", daya_tertinggi)

# Statistika deskriptif humidity tertinggi
humidity_tertinggi = data['Humidity'].max()
print("Humidity Tertinggi:", humidity_tertinggi)

# Statistika deskriptif rainfall rata-rata
rainfall_rata_rata = data['Rainfall'].mean()
print("Rainfall Rata-rata:", rainfall_rata_rata)
