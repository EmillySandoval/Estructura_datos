#include <iostream>
#include <vector>
using namespace std;

void construirMonticulo(vector<int>& lista, int tamaño, int indiceRaiz) {
    int indiceMayor = indiceRaiz;
    int indiceIzquierdo = 2 * indiceRaiz + 1;
    int indiceDerecho = 2 * indiceRaiz + 2;

    if (indiceIzquierdo < tamaño && lista[indiceIzquierdo] > lista[indiceMayor])
        indiceMayor = indiceIzquierdo;

    if (indiceDerecho < tamaño && lista[indiceDerecho] > lista[indiceMayor])
        indiceMayor = indiceDerecho;

    if (indiceMayor != indiceRaiz) {
        swap(lista[indiceRaiz], lista[indiceMayor]);
        construirMonticulo(lista, tamaño, indiceMayor);
    }
}

void ordenarPorMonticulo(vector<int>& lista) {
    int tamaño = lista.size();

    for (int i = tamaño / 2 - 1; i >= 0; i--)
        construirMonticulo(lista, tamaño, i);

    for (int i = tamaño - 1; i > 0; i--) {
        swap(lista[0], lista[i]);
        construirMonticulo(lista, i, 0);
    }
}

int main() {
    vector<int> listaNumeros = {12, 4, 7, 9, 1, 15, 3};
    cout << "Lista original: ";
    for (int num : listaNumeros) cout << num << " ";
    cout << endl;

    ordenarPorMonticulo(listaNumeros);

    cout << "Lista ordenada: ";
    for (int num : listaNumeros) cout << num << " ";
    cout << endl;

    return 0;
}