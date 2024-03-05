# import pandas as pd

# # Membaca data dari CSV
# data = pd.read_csv('train.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# # Membersihkan data dari nilai yang hilang
# # data_cleaned = data.dropna()

# # Menyaring hanya variabel numerik
# data_numerical = data.select_dtypes(include=['number'])

# # Menyimpan data yang telah dibersihkan ke dalam file CSV
# data_numerical.to_csv('data_cleaned.csv', index=False)

# # Menampilkan informasi sebelum dan setelah pembersihan
# print(f"Jumlah baris sebelum pembersihan: {len(data)}")
# print(f"Jumlah baris setelah pembersihan: {len(data_numerical)}")

# # Menampilkan beberapa baris pertama dari data yang telah dibersihkan
# print("Beberapa baris pertama dari data yang telah dibersihkan:")
# print(data_numerical.head())


import pandas as pd

# Baca data dari CSV
data = pd.read_csv('data_cleaned.csv')  # Gantilah 'nama_file.csv' dengan nama file CSV yang sesuai

# Hapus nilai 'NA' dari seluruh DataFrame
data_cleaned = data.dropna()

# Hapus nilai 'NA' dari kolom tertentu (misalnya, kolom 'SalePrice')
# data_cleaned = data.dropna(subset=['SalePrice'])

# Simpan DataFrame yang sudah dibersihkan ke file CSV
data_cleaned.to_csv('data_cleaned1.csv', index=False)  # Gantilah 'nama_file_cleaned.csv' dengan nama file yang sesuai
