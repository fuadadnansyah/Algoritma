#include <stdio.h>

// Membuat union bernama Data
union Data {
    int angka;
    float pecahan;
    char huruf;
};

int main() {
    union Data data;

    // Menyimpan nilai integer
    data.angka = 100;
    printf("Isi union (angka) : %d\n", data.angka);

    // Menyimpan nilai float
    data.pecahan = 3.14;
    printf("Isi union (float) : %.2f\n", data.pecahan);

    // Menyimpan nilai character
    data.huruf = 'A';
    printf("Isi union (char)  : %c\n", data.huruf);

    // Menampilkan kembali nilai sebelumnya
    printf("\nPerhatikan bahwa nilai sebelumnya berubah karena union memakai memori yang sama.\n");

    return 0;
}
