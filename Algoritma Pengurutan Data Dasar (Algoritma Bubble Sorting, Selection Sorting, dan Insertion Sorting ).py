# ======================================================
#        ALGORITMA PENGURUTAN DATA DASAR
#   Bubble Sort, Selection Sort, dan Insertion Sort
# ======================================================


# -----------------------------------
# 1. BUBBLE SORT
# -----------------------------------
def bubble_sort(data):
    print("\n=== BUBBLE SORT ===")
    arr = data.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            print(f"Bandingkan {arr[j]} dan {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"  → Tukar {arr[j]} dengan {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# -----------------------------------
# 2. SELECTION SORT
# -----------------------------------
def selection_sort(data):
    print("\n=== SELECTION SORT ===")
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        min_index = i
        print(f"\nMulai dari index {i}")

        for j in range(i + 1, n):
            print(f"  Bandingkan {arr[j]} dengan {arr[min_index]}")
            if arr[j] < arr[min_index]:
                print(f"  → {arr[j]} lebih kecil, jadi minimum baru")
                min_index = j

        if min_index != i:
            print(f"Tukar {arr[i]} dengan {arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -----------------------------------
# 3. INSERTION SORT
# -----------------------------------
def insertion_sort(data):
    print("\n=== INSERTION SORT ===")
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print(f"\nMasukkan {key} ke posisi yang tepat")

        while j >= 0 and key < arr[j]:
            print(f"  Geser {arr[j]} ke kanan")
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"  Letakkan {key} di posisi {j+1}")

    return arr


# =====================================================
#                 CONTOH PENGGUNAAN
# =====================================================

data = [20, 5, 7, 1, 12]

print("Data awal:", data)

hasil_bubble = bubble_sort(data)
print("Hasil Bubble Sort:", hasil_bubble)

hasil_selection = selection_sort(data)
print("Hasil Selection Sort:", hasil_selection)

hasil_insertion = insertion_sort(data)
print("Hasil Insertion Sort:", hasil_insertion)
