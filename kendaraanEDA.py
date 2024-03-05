import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
mobil = [413, 601, 604, 681, 694, 468, 570, 698, 657, 457, 602, 533, 535, 560, 494, 521, 573, 552, 555, 601, 498]
motor = [1889, 1990, 2074, 2188, 2574, 2007, 2132, 2800, 2317, 2090, 2344, 2197, 1758, 1956, 2029, 1689, 1997, 2182, 1630, 1898, 1974]
bus = [5, 8, 13, 5, 27, 8, 17, 7, 8, 9, 8, 7, 9, 10, 8, 14, 7, 11, 13, 9, 13]
truk = [23, 60, 37, 73, 35, 18, 53, 25, 31, 61, 31, 34, 39, 36, 15, 38, 25, 13, 33, 15, 8]

# Menempatkan data ke dalam DataFrame
df = pd.DataFrame({
    'mobil': mobil,
    'motor': motor,
    'bus': bus,
    'truk': truk
})

# Statistik deskriptif
desc_stat = df.describe()
print(desc_stat)

# Visualisasi dengan box plot
plt.figure(figsize=(8, 6))
df.boxplot()
plt.title('Box Plot Data Kendaraan')
plt.ylabel('Jumlah Kendaraan')
plt.xlabel('Kendaraan')
plt.show()
