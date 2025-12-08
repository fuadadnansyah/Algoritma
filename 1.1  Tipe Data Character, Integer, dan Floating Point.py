#include <stdio.h>

int main() {
    // Tipe Data Character
    char huruf = 'A';

    // Tipe Data Integer
    int angkaBulat = 25;

    // Tipe Data Floating Point
    float angkaPecahan = 3.14;
    double angkaPresisi = 10.56789123;

    // Output
    printf("=== Contoh Tipe Data ===\n");
    printf("Character    : %c\n", huruf);
    printf("Integer      : %d\n", angkaBulat);
    printf("Float        : %.2f\n", angkaPecahan);
    printf("Double       : %.8f\n", angkaPresisi);

    return 0;
}
