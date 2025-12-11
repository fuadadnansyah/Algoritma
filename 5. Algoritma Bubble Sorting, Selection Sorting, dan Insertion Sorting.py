# ==========================================================
#   Algoritma Sorting (Bubble, Selection, Insertion)
#   Versi Nomor 5 - Data Berbeda
#   By: Fuad Adnansyah
# ==========================================================

print("=== SORTING NOMOR 5 (DATA BERBEDA) ===\n")

# ---------------------------------------------------------
# 1. Bubble Sort
# ---------------------------------------------------------
def bubble_sort(arr):
    data = arr.copy()
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# ---------------------------------------------------------
# 2. Selection Sort
# ---------------------------------------------------------
def selection_sort(arr):
    data = arr.copy()
    for i in range(len(data)):
        min_i = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_i]:
                min_i = j
        data[i], data[min_i] = data[min_i], data[i]
    return data


# ---------------------------------------------------------
# 3. Insertion Sort
# ---------------------------------------------------------
def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data


# ---------------------------------------------------------
# Data uji (BERBEDA dari nomor 4)
# ---------------------------------------------------------
data_angka = [33, 11, 44, 5, 27, 19]

print("Data awal nomor 5:", data_angka)

print("\nBubble Sort:   ", bubble_sort(data_angka))
print("Selection Sort:", selection_sort(data_angka))
print("Insertion Sort:", insertion_sort(data_angka))
