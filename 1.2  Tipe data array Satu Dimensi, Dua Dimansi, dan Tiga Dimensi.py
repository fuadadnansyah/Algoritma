#include <stdio.h>

int main() {
    // ===========================
    // Array Satu Dimensi (1D)
    // ===========================
    int array1D[5] = {10, 20, 30, 40, 50};

    // ===========================
    // Array Dua Dimensi (2D)
    // ===========================
    int array2D[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // ===========================
    // Array Tiga Dimensi (3D)
    // ===========================
    int array3D[2][2][2] = {
        { {1, 2}, {3, 4} },
        { {5, 6}, {7, 8} }
    };


    // OUTPUT
    printf("=== ARRAY 1 DIMENSI ===\n");
    for (int i = 0; i < 5; i++) {
        printf("array1D[%d] = %d\n", i, array1D[i]);
    }

    printf("\n=== ARRAY 2 DIMENSI ===\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("array2D[%d][%d] = %d\n", i, j, array2D[i][j]);
        }
    }

    printf("\n=== ARRAY 3 DIMENSI ===\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                printf("array3D[%d][%d][%d] = %d\n", i, j, k, array3D[i][j][k]);
            }
        }
    }

    return 0;
}
