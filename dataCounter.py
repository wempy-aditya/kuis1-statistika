# from collections import Counter

# data = [
#     41, 20, 19, 22, 41, 36, 18, 29, 18, 20, 19, 19, 20, 19, 36, 26, 20, 22, 21, 37, 31, 27, 28, 25, 20, 36, 33, 42, 37, 38, 16,
#     17, 17, 16, 39, 44, 36, 34, 17, 14, 14, 16, 17, 14, 37, 24, 23, 22, 32, 55, 49, 31, 42, 44, 41, 39, 35, 31, 24, 38, 25,
#     24, 13, 44, 20, 20, 22, 21, 18, 20, 22, 24, 27, 29, 18, 20, 24, 33, 26, 21, 30, 19, 30, 33, 37, 41, 21, 21, 16, 15, 34,
#     19, 29, 30, 29, 39, 22, 17, 14, 15
# ]

# # Menghitung jumlah kemunculan setiap item
# count_items = Counter(data)

# print("Jumlah item yang sama:")
# for item, count in count_items.items():
#     print(f"{item}: {count}")


from collections import Counter

data = [
    'P', 'P', 'P', 'P', 'W', 'P', 'P', 'P', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'P', 'P', 'P', 'W', 'P', 'P', 'P', 'W', 'W',
    'P', 'P', 'W', 'P', 'P', 'W', 'W', 'P', 'P', 'P', 'P', 'W', 'P', 'P', 'P', 'P', 'W', 'P', 'P', 'P', 'P', 'W', 'W', 'P', 'P',
    'W', 'P', 'P', 'P', 'P', 'W', 'W', 'W', 'P', 'P', 'W', 'W', 'W', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'W', 'P',
    'W', 'P', 'W', 'W', 'P', 'P', 'P', 'W', 'P', 'P', 'P', 'W', 'P', 'W', 'P', 'P', 'P', 'W', 'P', 'W', 'P', 'P', 'W', 'W', 'P'
]

# Menghitung jumlah kemunculan setiap item
count_items = Counter(data)

print("Jumlah item yang sama:")
for item, count in count_items.items():
    print(f"{item}: {count}")
