#include <stdio.h>

// Membuat struktur bernama Mahasiswa
struct Mahasiswa {
    char nama[30];
    int umur;
    float ipk;
};

int main() {
    // Membuat variabel dari struct
    struct Mahasiswa mhs1;

    // Mengisi data
    printf("Masukkan nama: ");
    scanf("%s", mhs1.nama);

    printf("Masukkan umur: ");
    scanf("%d", &mhs1.umur);

    printf("Masukkan IPK: ");
    scanf("%f", &mhs1.ipk);

    // Menampilkan data
    printf("\n=== DATA MAHASISWA ===\n");
    printf("Nama : %s\n", mhs1.nama);
    printf("Umur : %d\n", mhs1.umur);
    printf("IPK  : %.2f\n", mhs1.ipk);

    return 0;
}
