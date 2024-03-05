# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # Membaca data dari file CSV
# # file_path = './coin_Bitcoin.csv' 
# file_path = './BTC_NORMALIZED.csv'  # Ganti dengan path file CSV hasil normalisasi
# df_normalized = pd.read_csv(file_path)

# # Kolom yang akan divisualisasikan
# columns_to_visualize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Menampilkan plot distribusi normal dengan warna yang berbeda
# plt.figure(figsize=(12, 8))

# # Definisikan warna yang berbeda untuk setiap kolom
# colors = ['g', 'b', 'r', 'c', 'm', 'y']

# for i, column in enumerate(columns_to_visualize):
#     mu, std = norm.fit(df_normalized[column])
    
#     # Menampilkan histogram dengan warna yang berbeda
#     n, bins, patches = plt.hist(df_normalized[column], bins=25, density=True, alpha=0.6, color=colors[i], label=column)
    
#     # Menampilkan kurva distribusi normal sebagai garis
#     xmin, xmax = plt.xlim()
#     x = np.linspace(xmin, xmax, 100)
#     p = norm.pdf(x, mu, std)
#     plt.plot(x, p, 'k', linewidth=2)

# plt.title('Distribusi Normal untuk Kolom Tertentu')
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi Normalisasi')
# plt.legend()
# plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler
# from scipy.stats import norm

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'  # Ganti dengan path file CSV Anda
# df = pd.read_csv(file_path)

# # Kolom yang akan divisualisasikan
# columns_to_visualize = ['High']

# # Inisialisasi MinMaxScaler
# scaler = MinMaxScaler()

# # Menampilkan dua plot sejajar
# fig, axs = plt.subplots(2, figsize=(12, 8), sharex=True)

# # Plot sebelum normalisasi
# axs[0].set_title('Distribusi Sebelum Normalisasi')
# for column in columns_to_visualize:
#     axs[0].hist(df[column], bins=20, density=True, alpha=0.6, label=column)

# # Plot setelah normalisasi
# axs[1].set_title('Distribusi Setelah Normalisasi')
# df_normalized = df.copy()
# df_normalized[columns_to_visualize] = scaler.fit_transform(df[columns_to_visualize])
# for column in columns_to_visualize:
#     axs[1].hist(df_normalized[column], bins=20, density=True, alpha=0.6, label=column)

# # Tambahkan label dan legenda
# axs[1].set_xlabel('Nilai')
# axs[1].set_ylabel('Frekuensi')
# axs[1].legend()

# # Atur layout
# plt.tight_layout()
# plt.show()


# import pandas as pd
# from scipy.stats import t, ttest_ind
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv'
# df = pd.read_csv(file_path)

# # Mengonversi kolom Date menjadi tipe data datetime
# df['Date'] = pd.to_datetime(df['Date'])

# # Menambahkan kolom Day yang berisi hari dari tanggal
# df['Day'] = df['Date'].dt.day_name()

# # Memisahkan data antara hari kerja (Weekdays) dan akhir pekan (Weekends)
# weekdays = df[df['Day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]['Close']
# weekends = df[df['Day'].isin(['Saturday', 'Sunday'])]['Close']

# # Melakukan uji t untuk dua sampel independen
# t_stat, p_value = ttest_ind(weekdays, weekends, equal_var=False)

# # Menampilkan hasil uji
# print(f'T-Statistic: {t_stat}')
# print(f'P-Value: {p_value}')

# # Menentukan daerah kritis pada distribusi t
# alpha = 0.05
# degrees_of_freedom = min(len(weekdays) - 1, len(weekends) - 1)
# critical_value = np.abs(t.ppf(alpha / 2, degrees_of_freedom))

# # Kesimpulan berdasarkan hasil uji
# if p_value < alpha:
#     print("Hipotesis nol ditolak. Terdapat perbedaan signifikan antara harga penutupan pada hari kerja dan akhir pekan.")
# else:
#     print("Tidak cukup bukti untuk menolak hipotesis nol. Tidak terdapat perbedaan signifikan antara harga penutupan pada hari kerja dan akhir pekan.")
#     print(f"Daerah Kritis: ({-critical_value}, {critical_value})")

# # Visualisasi distribusi harga penutupan pada hari kerja dan akhir pekan
# plt.figure(figsize=(10, 6))
# sns.histplot(weekdays, kde=True, color='blue', label='Hari Kerja', alpha=0.5)
# sns.histplot(weekends, kde=True, color='orange', label='Akhir Pekan', alpha=0.5)

# # Menandai daerah kritis pada distribusi t
# plt.axvline(-critical_value, color='red', linestyle='dashed', linewidth=2, label='Daerah Kritis')
# plt.axvline(critical_value, color='red', linestyle='dashed', linewidth=2)

# plt.title('Distribusi Harga Penutupan pada Hari Kerja dan Akhir Pekan')
# plt.xlabel('Harga Penutupan')
# plt.ylabel('Frekuensi Normalisasi')
# plt.legend()
# plt.show()