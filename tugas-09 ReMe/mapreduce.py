import json
from functools import reduce

with open("dummy.json", "r", encoding="utf-8") as file:
    data = json.load(file)

id_habit = int(input("Masukkan ID Habit (1-13): "))

print("Sebelum Mapping")
print(data[:5])

# Map
mapped_data = list(
    map(lambda d: [d["id_habit"], d["status"]], data)
)

print("\nSetelah Mapping")
print(mapped_data[:5])

# Shuffle
sorted_data = sorted(mapped_data, key=lambda x: x[0])

print("\nSetelah Shuffle")
print(sorted_data[:10])

# Filter
filtered_data = list(
    filter(lambda d: d[0] == id_habit, sorted_data)
)

print("\nSetelah Filter")
print(filtered_data[:10])

# Reduce
def hitung_berhasil(total, data):
    if data[1] == "berhasil":
        return total + 1
    return total

jumlah_berhasil = reduce(hitung_berhasil, filtered_data, 0)

total_checkin = len(filtered_data)

persentase = 0
if total_checkin > 0:
    persentase = (jumlah_berhasil / total_checkin) * 100

print("\nHasil")
print(f"ID Habit                 : {id_habit}")
print(f"Total Check-in           : {total_checkin}")
print(f"Jumlah Berhasil          : {jumlah_berhasil}")
print(f"Persentase Keberhasilan  : {persentase:.2f}%")