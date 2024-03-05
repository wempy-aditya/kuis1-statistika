# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import skew, shapiro
# import seaborn as sns

# # Baca data dari file CSV
# data = pd.read_csv("Data_UAS_Statistik.csv")

# # Plot histogram daya
# plt.figure(figsize=(10, 6))
# sns.histplot(data['Power'], bins=20, kde=True)
# plt.title('Histogram Daya')
# plt.xlabel('Daya')
# plt.ylabel('Frekuensi')
# plt.show()

# # Hitung skewness daya
# skewness_power = skew(data['Power'])
# print("Skewness Daya:", skewness_power)

# # Uji normalitas menggunakan Shapiro-Wilk
# stat, p_value = shapiro(data['Power'])
# print(f"Shapiro-Wilk p-value: {p_value}")

# # Plot histogram humidity
# plt.figure(figsize=(10, 6))
# sns.histplot(data['Humidity'], bins=20, kde=True)
# plt.title('Histogram Humidity')
# plt.xlabel('Humidity (%)')
# plt.ylabel('Frekuensi')
# plt.show()

# # Hitung skewness humidity
# skewness_humidity = skew(data['Humidity'])
# print("Skewness Humidity:", skewness_humidity)

# # Uji normalitas menggunakan Shapiro-Wilk
# stat, p_value = shapiro(data['Humidity'])
# print(f"Shapiro-Wilk p-value: {p_value}")

# # Plot histogram rainfall
# plt.figure(figsize=(10, 6))
# sns.histplot(data['Rainfall'], bins=20, kde=True)
# plt.title('Histogram Rainfall')
# plt.xlabel('Rainfall')
# plt.ylabel('Frekuensi')
# plt.show()

# # Hitung skewness rainfall
# skewness_rainfall = skew(data['Rainfall'])
# print("Skewness Rainfall:", skewness_rainfall)

# # Uji normalitas menggunakan Shapiro-Wilk
# stat, p_value = shapiro(data['Rainfall'])
# print(f"Shapiro-Wilk p-value: {p_value}")


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, shapiro
import seaborn as sns

# Baca data dari file CSV
data = pd.read_csv("Data_Standarisasi.csv")

# Plot histogram daya
plt.figure(figsize=(10, 6))
sns.histplot(data['Power'], bins=20, kde=True)
plt.title('Histogram Daya')
plt.xlabel('Daya')
plt.ylabel('Frekuensi')
plt.show()

# Hitung skewness daya
skewness_power = skew(data['Power'])
print("Skewness Daya:", skewness_power)

# Uji normalitas menggunakan Shapiro-Wilk
stat, p_value = shapiro(data['Power'])
print(f"Shapiro-Wilk p-value: {p_value}")

# Plot histogram humidity
plt.figure(figsize=(10, 6))
sns.histplot(data['Humidity'], bins=20, kde=True)
plt.title('Histogram Humidity')
plt.xlabel('Humidity (%)')
plt.ylabel('Frekuensi')
plt.show()

# Hitung skewness humidity
skewness_humidity = skew(data['Humidity'])
print("Skewness Humidity:", skewness_humidity)

# Uji normalitas menggunakan Shapiro-Wilk
stat, p_value = shapiro(data['Humidity'])
print(f"Shapiro-Wilk p-value: {p_value}")

# Plot histogram rainfall
plt.figure(figsize=(10, 6))
sns.histplot(data['Rainfall'], bins=20, kde=True)
plt.title('Histogram Rainfall')
plt.xlabel('Rainfall')
plt.ylabel('Frekuensi')
plt.show()

# Hitung skewness rainfall
skewness_rainfall = skew(data['Rainfall'])
print("Skewness Rainfall:", skewness_rainfall)

# Uji normalitas menggunakan Shapiro-Wilk
stat, p_value = shapiro(data['Rainfall'])
print(f"Shapiro-Wilk p-value: {p_value}")
