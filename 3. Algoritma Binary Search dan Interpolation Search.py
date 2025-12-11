# ==========================================================
#   Algoritma Binary Search & Interpolation Search
#   By: Fuad Adnansyah
# ==========================================================

print("=== BINARY SEARCH & INTERPOLATION SEARCH ===")

# -----------------------------
#   Binary Search
# -----------------------------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# -----------------------------
#   Interpolation Search
# -----------------------------
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Rumus posisi taksiran
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Data untuk uji coba
data_sorted = [5, 12, 18, 25, 32, 40, 47, 55]

# Hasil pencarian
print("\nBinary Search (mencari 25):")
print("Index ditemukan:", binary_search(data_sorted, 25))

print("\nInterpolation Search (mencari 32):")
print("Index ditemukan:", interpolation_search(data_sorted, 32))
