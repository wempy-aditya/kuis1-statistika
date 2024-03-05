# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Menampilkan beberapa baris pertama dari dataframe
# print(df.head())

# # Memilih kolom yang akan dinormalisasi
# columns_to_normalize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']  # Ganti dengan nama kolom yang ingin Anda normalisasi

# # Inisialisasi MinMaxScaler
# scaler = MinMaxScaler()

# # Melakukan normalisasi untuk kolom-kolom tertentu
# # df[columns_to_normalize] = scaler.df[columns_to_normalize]
# df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# # Menampilkan hasil setelah normalisasi
# print(df)


# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Menampilkan beberapa baris pertama dari dataframe sebelum normalisasi
# print("Sebelum normalisasi:")
# print(df.head())

# # Inisialisasi MinMaxScaler
# scaler = MinMaxScaler()

# # Memilih kolom yang akan dinormalisasi
# columns_to_normalize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Melakukan normalisasi untuk seluruh data dalam dataframe
# df_normalized = df.copy()  # Membuat salinan dataframe agar data asli tidak berubah
# df_normalized[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# # Menampilkan hasil normalisasi
# print("\nSetelah normalisasi:")
# print(df_normalized.head())

# # Menyimpan hasil normalisasi ke file CSV
# output_file_path = './BTC_NORMALIZED.csv'  # Ganti dengan path dan nama file CSV yang diinginkan
# df_normalized.to_csv(output_file_path, index=False)

# print(f"\nHasil normalisasi disimpan dalam file CSV: {output_file_path}")


# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Menampilkan beberapa baris pertama dari dataframe sebelum normalisasi
# print("Sebelum normalisasi:")
# print(df.head())

# # Inisialisasi StandardScaler
# scaler = StandardScaler()

# # Memilih kolom yang akan dinormalisasi
# columns_to_normalize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Melakukan normalisasi untuk seluruh data dalam dataframe
# df_normalized = df.copy()  # Membuat salinan dataframe agar data asli tidak berubah
# df_normalized[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# # Menampilkan hasil normalisasi
# print("\nSetelah normalisasi:")
# print(df_normalized.head())

# # Menyimpan hasil normalisasi ke file CSV
# output_file_path = './BTC_NORMALIZED_ZSCORE.csv'  # Ganti dengan path dan nama file CSV yang diinginkan
# df_normalized.to_csv(output_file_path, index=False)

# print(f"\nHasil normalisasi dengan Z-Score disimpan dalam file CSV: {output_file_path}")



# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Menampilkan beberapa baris pertama dari dataframe sebelum normalisasi
# print("Sebelum normalisasi:")
# print(df.head())

# # Inisialisasi MinMaxScaler
# scaler = MinMaxScaler()

# # Kolom yang akan dinormalisasi
# columns_to_normalize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Melakukan normalisasi untuk setiap kolom secara terpisah
# df_normalized = df.copy()  # Membuat salinan dataframe agar data asli tidak berubah
# for column in columns_to_normalize:
#     df_normalized[column] = scaler.fit_transform(df[[column]])

# # Menampilkan hasil normalisasi
# print("\nSetelah normalisasi:")
# print(df_normalized.head())

# # Menyimpan hasil normalisasi ke file CSV
# output_file_path = './BTC_NORMALIZED_COLUMNWISE.csv'  # Ganti dengan path dan nama file CSV yang diinginkan
# df_normalized.to_csv(output_file_path, index=False)

# print(f"\nHasil normalisasi disimpan dalam file CSV: {output_file_path}")



# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Menampilkan beberapa baris pertama dari dataframe sebelum normalisasi
# print("Sebelum normalisasi:")
# print(df.head())

# # Inisialisasi MinMaxScaler
# scaler = MinMaxScaler()

# # Melakukan normalisasi untuk setiap kolom secara terpisah
# df_normalized = df.copy()  # Membuat salinan dataframe agar data asli tidak berubah
# for column in df.columns[1:]:
#     df_normalized[column] = scaler.fit_transform(df[[column]])

# # Menampilkan hasil normalisasi
# print("\nSetelah normalisasi:")
# print(df_normalized.head())

# # Menyimpan hasil normalisasi ke file CSV
# output_file_path = './BTC_NORMALIZED_COLUMNWISE.csv'  # Ganti dengan path dan nama file CSV yang diinginkan
# df_normalized.to_csv(output_file_path, index=False)

# print(f"\nHasil normalisasi disimpan dalam file CSV: {output_file_path}")


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Membaca data dari file CSV
file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
df = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama dari dataframe sebelum normalisasi
# print("Sebelum normalisasi:")
# print(df.head())

# Inisialisasi MinMaxScaler
scaler = MinMaxScaler()

# Kolom yang akan dinormalisasi
column_to_normalize = 'Low'

# Melakukan normalisasi untuk kolom tertentu
df_normalized = df.copy()  # Membuat salinan dataframe agar data asli tidak berubah
df_normalized[column_to_normalize] = scaler.fit_transform(df[[column_to_normalize]])

# Menampilkan hasil normalisasi
# print("\nSetelah normalisasi:")
# print(df_normalized.head())

# Menyimpan hasil normalisasi ke file CSV
output_file_path = './BTC_NORMALIZED_HIGH.csv'  # Ganti dengan path dan nama file CSV yang diinginkan
df_normalized.to_csv(output_file_path, index=False)

print(f"\nHasil normalisasi disimpan dalam file CSV: {output_file_path}")
