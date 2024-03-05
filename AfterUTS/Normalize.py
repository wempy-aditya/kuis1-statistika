# from sklearn.preprocessing import MinMaxScaler

# # Data yang akan dinormalisasi
# data = [
#     [413, 601, 604, 681, 694, 468, 570, 698, 657, 457, 602, 533, 535, 560, 494, 521, 573, 552, 555, 601, 498],
#     [1889, 1990, 2074, 2188, 2574, 2007, 2132, 2800, 2317, 2090, 2344, 2197, 1758, 1956, 2029, 1689, 1997, 2182, 1630, 1898, 1974],
#     [5, 8, 13, 5, 27, 8, 17, 7, 8, 9, 8, 7, 9, 10, 8, 14, 7, 11, 13, 9, 13],
#     [23, 60, 37, 73, 35, 18, 53, 25, 31, 61, 31, 34, 39, 36, 15, 38, 25, 13, 33, 15, 8]
# ]

# # Inisialisasi MinMaxScaler
# scaler = MinMaxScaler()

# # Fit dan transform data menggunakan MinMaxScaler
# normalized_data = scaler.fit_transform(data)

# # Hasil normalisasi
# print(normalized_data)


import pandas as pd

# Data yang akan dinormalisasi
data = {
    'mobil': [413, 601, 604, 681, 694, 468, 570, 698, 657, 457, 602, 533, 535, 560, 494, 521, 573, 552, 555, 601, 498],
    'motor': [1889, 1990, 2074, 2188, 2574, 2007, 2132, 2800, 2317, 2090, 2344, 2197, 1758, 1956, 2029, 1689, 1997, 2182, 1630, 1898, 1974],
    'bus': [5, 8, 13, 5, 27, 8, 17, 7, 8, 9, 8, 7, 9, 10, 8, 14, 7, 11, 13, 9, 13],
    'truk': [23, 60, 37, 73, 35, 18, 53, 25, 31, 61, 31, 34, 39, 36, 15, 38, 25, 13, 33, 15, 8]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Normalisasi menggunakan Min-Max Scaling
normalized_df = (df - df.min()) / (df.max() - df.min())

# Hasil normalisasi
print(normalized_df)
