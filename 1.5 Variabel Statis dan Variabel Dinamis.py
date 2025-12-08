#include <stdio.h>
#include <stdlib.h>

// ===========================
//   >>> VARIABEL STATIS <<<
// ===========================
static int nilaiTetap = 10;   // VARIABEL STATIS

// Fungsi dengan variabel static lokal
void contohStatic() {
    static int hitung = 0;    // VARIABEL STATIS (tidak reset)
    hitung++;
    printf("Nilai static dalam fungsi = %d\n", hitung);
}

int main() {

    printf("=== BAGIAN VARIABEL STATIS ===\n");
    printf("nilaiTetap (static global) = %d\n", nilaiTetap);
    contohStatic();
    contohStatic();
    contohStatic();

    // ===========================
    //   >>> VARIABEL DINAMIS <<<
    // ===========================
    int *dataDinamis;    // POINTER untuk variabel dinamis (belum ada memori)

    // Alokasi memori dinamis
    dataDinamis = (int*) malloc(sizeof(int));   // VARIABEL DINAMIS

    if (dataDinamis == NULL) {
        printf("Gagal mengalokasikan memori!\n");
        return 1;
    }

    *dataDinamis = 50;  // Mengisi nilai variabel dinamis
    printf("\n=== BAGIAN VARIABEL DINAMIS ===\n");
    printf("Nilai variabel dinamis = %d\n", *dataDinamis);

    // Bebaskan memori
    free(dataDinamis);

    printf("Memori variabel dinamis dibebaskan.\n");

    return 0;
}
