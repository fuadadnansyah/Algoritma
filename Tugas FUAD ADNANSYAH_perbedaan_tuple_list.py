# Contoh perbedaan List dan Tuple di Python

# List (bisa diubah / mutable)
my_list = [10, 20, 30]
print("List awal:", my_list)

my_list[0] = 99    # mengubah elemen list
my_list.append(40) # menambah elemen baru
print("List setelah diubah:", my_list)

# Tuple (tidak bisa diubah / immutable)
my_tuple = (10, 20, 30)
print("\nTuple awal:", my_tuple)

try:
    my_tuple[0] = 99  # ERROR! Tuple tidak bisa diubah
except TypeError:
    print("Tuple tidak bisa diubah (immutable)")

# Penjelasan singkat:
# List = Dapat diubah → cocok untuk data yang selalu berubah.
# Tuple = Tidak dapat diubah → cocok untuk data tetap, seperti koordinat atau hari dalam seminggu.

print("\nTipe data list  :", type(my_list))
print("Tipe data tuple :", type(my_tuple))
