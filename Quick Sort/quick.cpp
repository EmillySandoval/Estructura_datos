#include <iostream>
using namespace std;

void imprimir(int lista[], int inicio, int fin, int nivel, int pivote) {
    cout << string(nivel * 2, ' ') << "Pivote: " << pivote << ", Sublista: [";
    for (int i = inicio; i <= fin; i++) cout << lista[i] << " ";
    cout << "]\n";
}

int particion(int lista[], int inicio, int fin, int nivel) {
    int pivote = lista[fin];
    imprimir(lista, inicio, fin, nivel, pivote);
    int i = inicio - 1;
    for (int j = inicio; j < fin; j++) {
        if (lista[j] <= pivote) {
            i++;
            swap(lista[i], lista[j]);
        }
    }
    swap(lista[i + 1], lista[fin]);
    return i + 1;
}

void quickSort(int lista[], int inicio, int fin, int nivel) {
    if (inicio < fin) {
        int pivote = particion(lista, inicio, fin, nivel);
        quickSort(lista, inicio, pivote - 1, nivel + 1);
        quickSort(lista, pivote + 1, fin, nivel + 1);
    }
}

int main() {
    int numeros[] = {8, 3, 1, 7, 0, 10, 2};
    int tam = sizeof(numeros) / sizeof(numeros[0]);
    cout << "Original: ";
    for (int i = 0; i < tam; i++) cout << numeros[i] << " ";
    cout << "\n";
    quickSort(numeros, 0, tam - 1, 0);
    cout << "Ordenado: ";
    for (int i = 0; i < tam; i++) cout << numeros[i] << " ";
}