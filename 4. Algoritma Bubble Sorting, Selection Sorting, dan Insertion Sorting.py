# ==========================================================
#   Algoritma Bubble Sort, Selection Sort, Insertion Sort
#   By: Fuad Adnansyah
# ==========================================================

print("=== ALGORITMA SORTING (BUBBLE, SELECTION, INSERTION) ===\n")

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
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
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
# Data Uji
# ---------------------------------------------------------
angka = [14, 3, 9, 22, 7, 18]

print("Data awal:", angka)

print("\nHasil Bubble Sort:   ", bubble_sort(angka))
print("Hasil Selection Sort:", selection_sort(angka))
print("Hasil Insertion Sort:", insertion_sort(angka))
