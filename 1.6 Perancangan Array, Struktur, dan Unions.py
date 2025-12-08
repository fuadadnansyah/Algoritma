#include <stdio.h>
#include <string.h>

// UNION untuk menyimpan kode barang (bisa int atau char)
union Kode {
    int kodeAngka;
    char kodeHuruf;
};

// STRUCT untuk menyimpan data barang
struct Barang {
    char nama[20];
    float harga;
    union Kode kode;
};

int main() {
    // Array berisi beberapa barang
    struct Barang daftar[3];

    // Mengisi data barang pertama
    strcpy(daftar[0].nama, "Pulpen");
    daftar[0].harga = 3000;
    daftar[0].kode.kodeAngka = 101;

    // Mengisi data barang kedua
    strcpy(daftar[1].nama, "Buku");
    daftar[1].harga = 7000;
    daftar[1].kode.kodeHuruf = 'B';

    // Mengisi data barang ketiga
    strcpy(daftar[2].nama, "Penghapus");
    daftar[2].harga = 2000;
    daftar[2].kode.kodeAngka = 303;

    // Output
    printf("=== DATA BARANG ===\n");
    for (int i = 0; i < 3; i++) {
        printf("\nBarang ke-%d\n", i+1);
        printf("Nama  : %s\n", daftar[i].nama);
        printf("Harga : %.2f\n", daftar[i].harga);

        // Menentukan apakah kode angka atau huruf
        if (i == 1) {
            printf("Kode  : %c (huruf)\n", daftar[i].kode.kodeHuruf);
        } else {
            printf("Kode  : %d (angka)\n", daftar[i].kode.kodeAngka);
        }
    }

    return 0;
}
