# import matplotlib.pyplot as plt

# data = [
#     413, 601, 604, 681, 694, 468, 570, 698, 657, 457, 602, 533, 535, 560, 494, 521, 573, 552, 555, 601, 498
# ]

# plt.figure(figsize=(6, 4))
# plt.boxplot(data)
# plt.title('Box Plot')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt

# data = [
#     1889, 1990, 2074, 2188, 2574, 2007, 2132, 2800, 2317, 2090, 2344, 2197, 1758, 1956, 2029, 1689, 1997, 2182, 1630, 1898, 1974
# ]

# plt.figure(figsize=(6, 4))
# plt.boxplot(data)
# plt.title('Box Plot')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# data = [
#     5, 8, 13, 5, 27, 8, 17, 7, 8, 9, 8, 7, 9, 10, 8, 14, 7, 11, 13, 9, 13
# ]

# plt.figure(figsize=(6, 4))
# plt.boxplot(data)
# plt.title('Box Plot')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# data = [
#     23, 60, 37, 73, 35, 18, 53, 25, 31, 61, 31, 34, 39, 36, 15, 38, 25, 13, 33, 15, 8
# ]

# plt.figure(figsize=(6, 4))
# plt.boxplot(data)
# plt.title('Box Plot')
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

data = [mobil, motor, bus, truk]

plt.figure(figsize=(10, 6))

plt.boxplot(data, labels=['Mobil', 'Motor', 'Bus', 'Truk'])
plt.title('Side by Side Box Plot Kendaraan')
plt.ylabel('Jumlah Kendaraan')
plt.grid(True)
plt.show()
