# import pandas as pd

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'
# df = pd.read_csv(file_path)

# # Menampilkan informasi tentang nilai yang hilang sebelum data cleaning
# print("Informasi nilai yang hilang sebelum data cleaning:")
# print(df.isnull().sum())

# # Menangani nilai yang hilang dengan menggantinya menggunakan nilai rata-rata kolom
# df.fillna(df.mean(), inplace=True)

# # Menampilkan informasi tentang nilai yang hilang setelah data cleaning
# print("\nInformasi nilai yang hilang setelah data cleaning:")
# print(df.isnull().sum())

# # Menyimpan hasil data cleaning ke file CSV
# output_file_path = './BTC_DATA_CLEANED.csv'
# df.to_csv(output_file_path, index=False)

# print(f"\nHasil data cleaning disimpan dalam file CSV: {output_file_path}")


import pandas as pd

# Membaca data dari file CSV
file_path = './coin_Bitcoin.csv'
df = pd.read_csv(file_path)

# Memilih hanya kolom-kolom numerik
numeric_columns = df.select_dtypes(include=['number']).columns

# Menampilkan informasi tentang nilai yang hilang sebelum data cleaning
print("Informasi nilai yang hilang sebelum data cleaning:")
print(df[numeric_columns].isnull().sum())

# Menangani nilai yang hilang dengan menggantinya menggunakan nilai rata-rata kolom
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Menampilkan informasi tentang nilai yang hilang setelah data cleaning
print("\nInformasi nilai yang hilang setelah data cleaning:")
print(df[numeric_columns].isnull().sum())

# Menyimpan hasil data cleaning ke file CSV
output_file_path = './BTC_DATA_CLEANED.csv'
df.to_csv(output_file_path, index=False)

print(f"\nHasil data cleaning disimpan dalam file CSV: {output_file_path}")


# https://chat.openai.com/c/dfd8e2a8-1756-4f7e-a758-2d90374fded6