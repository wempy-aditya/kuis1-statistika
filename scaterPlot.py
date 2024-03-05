# import matplotlib.pyplot as plt

# data = [
#     413, 601, 604, 681, 694, 468, 570, 698, 657, 457, 602, 533, 535, 560, 494, 521, 573, 552, 555, 601, 498
# ]

# # Menyiapkan indeks untuk sumbu x (indeks data)
# x = list(range(1, len(data) + 1))

# plt.figure(figsize=(8, 5))
# plt.scatter(x, data)
# plt.title('Scatter Plot')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# data = [
#     1889, 1990, 2074, 2188, 2574, 2007, 2132, 2800, 2317, 2090, 2344, 2197, 1758, 1956, 2029, 1689, 1997, 2182, 1630, 1898, 1974
# ]

# # Menyiapkan indeks untuk sumbu x (indeks data)
# x = list(range(1, len(data) + 1))

# plt.figure(figsize=(8, 5))
# plt.scatter(x, data)
# plt.title('Scatter Plot')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt

# data = [
#     5, 8, 13, 5, 27, 8, 17, 7, 8, 9, 8, 7, 9, 10, 8, 14, 7, 11, 13, 9, 13
# ]

# # Menyiapkan indeks untuk sumbu x (indeks data)
# x = list(range(1, len(data) + 1))

# plt.figure(figsize=(8, 5))
# plt.scatter(x, data)
# plt.title('Scatter Plot')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt

# data = [
#     23, 60, 37, 73, 35, 18, 53, 25, 31, 61, 31, 34, 39, 36, 15, 38, 25, 13, 33, 15, 8
# ]

# # Menyiapkan indeks untuk sumbu x (indeks data)
# x = list(range(1, len(data) + 1))

# plt.figure(figsize=(8, 5))
# plt.scatter(x, data)
# plt.title('Scatter Plot')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()


import matplotlib.pyplot as plt

mobil = [
    413, 601, 604, 681, 694, 468, 570, 698, 657, 457, 602, 533, 535, 560, 494, 521, 573, 552, 555, 601, 498
]

motor = [
    1889, 1990, 2074, 2188, 2574, 2007, 2132, 2800, 2317, 2090, 2344, 2197, 1758, 1956, 2029, 1689, 1997, 2182, 1630, 1898, 1974
]

bus = [
    5, 8, 13, 5, 27, 8, 17, 7, 8, 9, 8, 7, 9, 10, 8, 14, 7, 11, 13, 9, 13
]

truk = [
    23, 60, 37, 73, 35, 18, 53, 25, 31, 61, 31, 34, 39, 36, 15, 38, 25, 13, 33, 15, 8
]

# Menghitung panjang setiap data
length = len(mobil)

# Menyiapkan indeks untuk sumbu x (indeks data)
x_mobil = list(range(1, length + 1))
x_motor = list(range(1, length + 1))
x_bus = list(range(1, length + 1))
x_truk = list(range(1, length + 1))

plt.figure(figsize=(10, 6))

# Plotting scatter plot
plt.scatter(x_mobil, mobil, label='Mobil', color='red')
plt.scatter(x_motor, motor, label='Motor', color='blue')
plt.scatter(x_bus, bus, label='Bus', color='green')
plt.scatter(x_truk, truk, label='Truk', color='orange')

plt.title('Scatter Plot Data Kendaraan')
plt.xlabel('Index Data')
plt.ylabel('Jumlah Kendaraan')
plt.legend()
plt.grid(True)
plt.show()
