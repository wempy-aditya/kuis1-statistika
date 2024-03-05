import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

# Membaca data dari file CSV
file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
df = pd.read_csv(file_path)

# Mengambil kolom tertentu
# ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']
selected_column = 'Marketcap'  # Ganti dengan nama kolom yang ingin Anda analisis
selected_data = df[selected_column]

# Menghitung statistik deskriptif menggunakan NumPy
mean = np.mean(selected_data)
std_dev = np.std(selected_data)
variance = np.var(selected_data)
median = np.median(selected_data)
range_val = np.ptp(selected_data)
min_val = np.min(selected_data)
max_val = np.max(selected_data)
sum_val = np.sum(selected_data)

# Menghitung kurtosis dan skewness menggunakan SciPy
kurt = kurtosis(selected_data)
skewness = skew(selected_data)

# Menampilkan hasil
print("Mean:", mean)
print("Median:", median)
print("Mode:", selected_data.mode()[0])  # Menggunakan pandas untuk menghitung modus
print("Standard Deviation:", std_dev)
print("Sample Variance:", variance)
print("Kurtosis:", kurt)
print("Skewness:", skewness)
print("Range:", range_val)
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Sum:", sum_val)
print("Count:", len(selected_data))



# import pandas as pd
# from scipy.stats import describe

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'   # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Mengambil kolom tertentu
# selected_columns = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']  # Ganti dengan nama kolom yang ingin Anda analisis
# selected_data = df[selected_columns]

# # Menghitung statistik deskriptif
# desc_stats = describe(selected_data, axis=0)

# # Membuat DataFrame dari hasil
# desc_stats_df = pd.DataFrame(desc_stats._asdict())

# # Menyimpan hasil ke file CSV
# output_file_path = './output_descriptive_stats.csv'  # Ganti dengan nama file CSV keluaran yang diinginkan
# desc_stats_df.to_csv(output_file_path, index=False)

# print(f"Statistik deskriptif disimpan dalam file CSV: {output_file_path}")


# import pandas as pd

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Mengambil kolom tertentu
# selected_columns = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']  # Ganti dengan nama kolom yang ingin Anda analisis
# selected_data = df[selected_columns]

# # Menghitung statistik deskriptif
# desc_stats = selected_data.describe().transpose()

# # Menyimpan hasil ke file CSV
# output_file_path = './output_descriptive_stats.csv'  # Ganti dengan nama file CSV keluaran yang diinginkan
# desc_stats.to_csv(output_file_path)

# print(f"Statistik deskriptif disimpan dalam file CSV: {output_file_path}")
