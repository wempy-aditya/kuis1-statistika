import pandas as pd
import numpy as np

# Baca data dari file CSV
data = pd.read_csv("Data_UAS_Statistik.csv")

# Statistika deskriptif
deskripsi = data.describe()
print(deskripsi)

# Interpretasi:
# - Daya tertinggi: Lihat nilai maksimum dari kolom "Power".
# - Humidity tertinggi: Lihat nilai maksimum dari kolom "Humidity (%)".
# - Rainfall rata-rata: Lihat nilai rata-rata dari kolom "Rainfall".
