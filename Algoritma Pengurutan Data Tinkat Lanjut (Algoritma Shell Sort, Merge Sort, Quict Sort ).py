# ================================================================
#      ALGORITMA PENGURUTAN DATA TINGKAT LANJUT
#   Shell Sort, Merge Sort, dan Quick Sort
# ================================================================


# --------------------------------------------------------------
# 1. SHELL SORT
# --------------------------------------------------------------
def shell_sort(data):
    print("\n=== SHELL SORT ===")
    arr = data.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        print(f"\nGap saat ini: {gap}")

        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                print(f"Geser {arr[j - gap]} ke posisi {j}")
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr


# --------------------------------------------------------------
# 2. MERGE SORT
# --------------------------------------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        print(f"\nPisahkan: {arr}")

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # gabungkan hasil
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # tambahkan sisa left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # tambahkan sisa right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(f"Gabungkan menjadi: {arr}")

    return arr


# --------------------------------------------------------------
# 3. QUICK SORT
# --------------------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    print(f"\nPivot: {pivot} dari {arr}")

    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"  Left: {left}")
    print(f"  Mid : {mid}")
    print(f"  Right: {right}")

    return quick_sort(left) + mid + quick_sort(right)


# ===============================================================
#                     CONTOH PENGGUNAAN
# ===============================================================

data = [25, 7, 9, 1, 15, 3]

print("Data awal:", data)

hasil_shell = shell_sort(data)
print("Hasil Shell Sort:", hasil_shell)

hasil_merge = merge_sort(data.copy())
print("Hasil Merge Sort:", hasil_merge)

hasil_quick = quick_sort(data.copy())
print("Hasil Quick Sort:", hasil_quick)
