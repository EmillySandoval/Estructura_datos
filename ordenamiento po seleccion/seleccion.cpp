#include <iostream>
using namespace std;

void ordenamientoPorSeleccion(int lista[], int tamaño) {
    for (int i = 0; i < tamaño - 1; i++) {
        int indiceMinimo = i;
        for (int j = i + 1; j < tamaño; j++) {
            if (lista[j] < lista[indiceMinimo]) {
                indiceMinimo = j;
            }
        }
        swap(lista[i], lista[indiceMinimo]);
    }
}

void mostrarLista(int lista[], int tamaño) {
    for (int i = 0; i < tamaño; i++)
        cout << lista[i] << " ";
    cout << endl;
}

int main() {
    int numeros[] = {64, 25, 12, 22, 11};
    int tamaño = sizeof(numeros) / sizeof(numeros[0]);

    cout << "Lista original: ";
    mostrarLista(numeros, tamaño);

    ordenamientoPorSeleccion(numeros, tamaño);

    cout << "Lista ordenada: ";
    mostrarLista(numeros, tamaño);

    return 0;
}