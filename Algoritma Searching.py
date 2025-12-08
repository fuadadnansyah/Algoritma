# ===================================================
#                 ALGORITMA SEARCHING
#          Linear Search & Binary Search
# ===================================================


# -------------------------------
# 1. LINEAR SEARCH
# -------------------------------
def linear_search(data, target):
    print("\n=== LINEAR SEARCH ===")
    for i in range(len(data)):
        print(f"Bandingkan target {target} dengan data[{i}] = {data[i]}")
        if data[i] == target:
            return i
    return -1


# -------------------------------
# 2. BINARY SEARCH
# -------------------------------
def binary_search(data, target):
    print("\n=== BINARY SEARCH ===")
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Cek tengah data[{mid}] = {data[mid]}")

        if data[mid] == target:
            return mid
        elif target < data[mid]:
            print("→ Target lebih kecil, geser ke kiri")
            high = mid - 1
        else:
            print("→ Target lebih besar, geser ke kanan")
            low = mid + 1

    return -1


# =====================================================
#                 CONTOH PENGGUNAAN
# =====================================================

data_acak = [12, 7, 5, 20, 3, 9]
data_urut = [3, 5, 7, 9, 12, 20]

target = 9

# Linear Search
print("Data untuk linear:", data_acak)
hasil1 = linear_search(data_acak, target)

if hasil1 != -1:
    print(f"Target {target} ditemukan di index {hasil1}")
else:
    print(f"Target {target} tidak ditemukan")


# Binary Search
print("\nData untuk binary:", data_urut)
hasil2 = binary_search(data_urut, target)

if hasil2 != -1:
    print(f"Target {target} ditemukan di index {hasil2}")
else:
    print(f"Target {target} tidak ditemukan")
