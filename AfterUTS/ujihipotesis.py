# import pandas as pd
# from scipy.stats import ttest_ind
# from datetime import datetime

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

# # Menampilkan hasil
# print(f'T-Statistic: {t_stat}')
# print(f'P-Value: {p_value}')

# # Menentukan daerah kritis pada distribusi t
# alpha = 0.05
# critical_value = -1.96  # untuk alpha/2 pada distribusi t dengan derajat kebebasan yang sesuai

# # Kesimpulan berdasarkan hasil uji
# if p_value < alpha:
#     print("Hipotesis nol ditolak. Terdapat perbedaan signifikan antara harga penutupan pada hari kerja dan akhir pekan.")
# else:
#     print("Tidak cukup bukti untuk menolak hipotesis nol. Tidak terdapat perbedaan signifikan antara harga penutupan pada hari kerja dan akhir pekan.")


# import pandas as pd
# from scipy.stats import t, ttest_ind
# from datetime import datetime
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

# # Menampilkan hasil
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

import pandas as pd
from scipy.stats import t, ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Membaca data dari file CSV
file_path = './coin_Bitcoin.csv'
df = pd.read_csv(file_path)

# Mengonversi kolom Date menjadi tipe data datetime
df['Date'] = pd.to_datetime(df['Date'])

# Menambahkan kolom Day yang berisi hari dari tanggal
df['Day'] = df['Date'].dt.day_name()

# Memisahkan data antara hari kerja (Weekdays) dan akhir pekan (Weekends)
weekdays = df[df['Day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]['Close']
weekends = df[df['Day'].isin(['Saturday', 'Sunday'])]['Close']

# Melakukan uji t untuk dua sampel independen
t_stat, p_value = ttest_ind(weekdays, weekends, equal_var=False)

# Menampilkan hasil uji
print(f'T-Statistic: {t_stat}')
print(f'P-Value: {p_value}')

# Menentukan daerah kritis pada distribusi t
alpha = 0.05
degrees_of_freedom = min(len(weekdays) - 1, len(weekends) - 1)
critical_value = np.abs(t.ppf(alpha / 2, degrees_of_freedom))

# Kesimpulan berdasarkan hasil uji
if p_value < alpha:
    print("Hipotesis nol ditolak. Terdapat perbedaan signifikan antara harga penutupan pada hari kerja dan akhir pekan.")
else:
    print("Tidak cukup bukti untuk menolak hipotesis nol. Tidak terdapat perbedaan signifikan antara harga penutupan pada hari kerja dan akhir pekan.")
    print(f"Daerah Kritis: ({-critical_value}, {critical_value})")

# Visualisasi distribusi harga penutupan pada hari kerja dan akhir pekan
plt.figure(figsize=(10, 6))
sns.histplot(weekdays, kde=True, color='blue', label='Hari Kerja', alpha=0.5)
sns.histplot(weekends, kde=True, color='orange', label='Akhir Pekan', alpha=0.5)

# Menandai daerah kritis pada distribusi t
plt.axvline(-critical_value, color='red', linestyle='dashed', linewidth=2, label='Daerah Kritis')
plt.axvline(critical_value, color='red', linestyle='dashed', linewidth=2)

plt.title('Distribusi Harga Penutupan pada Hari Kerja dan Akhir Pekan')
plt.xlabel('Harga Penutupan')
plt.ylabel('Frekuensi Normalisasi')
plt.legend()
plt.show()

