# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # Menghasilkan data dari distribusi normal
# mean = 0
# std_dev = 1
# size = 1000
# data = np.random.normal(mean, std_dev, size)

# # Membuat histogram distribusi normal
# plt.hist(data, bins=50, density=True, alpha=0.6, color='g')

# # Menambahkan kurva distribusi normal
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mean, std_dev)
# plt.plot(x, p, 'k', linewidth=2)

# # Menambahkan label dan judul
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi Relatif')
# plt.title('Plot Distribusi Normal')

# # Menampilkan plot
# plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # Membaca data dari file CSV
# file_path = './BTC_NORMALIZED.csv' 
# # file_path = './coin_Bitcoin.csv' 
# df = pd.read_csv(file_path)

# # Mengambil data dari kolom tertentu-
# selected_column = 'Marketcap'
# data = df[selected_column]

# # Menentukan parameter distribusi normal
# mean = data.mean()
# std_dev = data.std()

# # Membuat histogram distribusi normal
# plt.hist(data, bins=20, density=True, alpha=0.6, color='g')

# # Menambahkan kurva distribusi normal
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mean, std_dev)
# plt.plot(x, p, 'k', linewidth=2)

# # Menambahkan label dan judul
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi Relatif')
# plt.title(f'Plot Distribusi Normal dari Kolom {selected_column}')

# # Menampilkan plot
# plt.show()

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Membaca data dari file CSV
# file_path = './coin_Bitcoin.csv' 
# # file_path = './BTC_NORMALIZED.csv'  # Ganti dengan path file CSV hasil normalisasi
# df_normalized = pd.read_csv(file_path)

# # Kolom yang akan divisualisasikan
# columns_to_visualize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Menampilkan distribusi normal menggunakan seaborn dan matplotlib
# plt.figure(figsize=(12, 8))

# for column in columns_to_visualize:
#     sns.histplot(df_normalized[column], kde=True, label=column)

# plt.title('Distribusi Normal untuk Kolom Tertentu')
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi')
# plt.legend()
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Membaca data dari file CSV
file_path = './BTC_NORMALIZED.csv'  # Ganti dengan path file CSV hasil normalisasi
df_normalized = pd.read_csv(file_path)

# Kolom yang akan divisualisasikan
# columns_to_visualize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']
columns_to_visualize = ['Low']

# Menampilkan plot distribusi normal
plt.figure(figsize=(12, 8))

for column in columns_to_visualize:
    mu, std = norm.fit(df_normalized[column])
    plt.hist(df_normalized[column], bins=20, density=True, alpha=0.6, color='g', label=column)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)

plt.title('Distribusi Normal untuk Kolom Tertentu')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Normalisasi')
plt.legend()
plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # Membaca data dari file CSV
# file_path = './BTC_NORMALIZED.csv'  # Ganti dengan path file CSV hasil normalisasi
# df_normalized = pd.read_csv(file_path)

# # Kolom yang akan divisualisasikan
# columns_to_visualize = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

# # Menampilkan plot distribusi normal
# plt.figure(figsize=(12, 8))

# # Menggunakan palet warna 'viridis'
# colors = plt.cm.viridis(np.linspace(0, 1, len(columns_to_visualize)))

# for column, color in zip(columns_to_visualize, colors):
#     mu, std = norm.fit(df_normalized[column])
#     plt.hist(df_normalized[column], bins=25, density=True, alpha=0.6, color=color, label=column)
#     xmin, xmax = plt.xlim()
#     x = np.linspace(xmin, xmax, 100)
#     p = norm.pdf(x, mu, std)
#     plt.plot(x, p, color, linewidth=2)

# plt.title('Distribusi Normal untuk Kolom Tertentu')
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi Normalisasi')
# plt.legend()
# plt.show()

