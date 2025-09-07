#include <iostream>
using namespace std;

int busquedaLineal(int arr[], int n, int objetivo) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == objetivo)
            return i;
    }
    return -1;
}

int main() {
    int arreglo[] = {3, 8, 1, 5, 9};
    int n = sizeof(arreglo) / sizeof(arreglo[0]);
    cout << busquedaLineal(arreglo, n, 5);  
    return 0;
}