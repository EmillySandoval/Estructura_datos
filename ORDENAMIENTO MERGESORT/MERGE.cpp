#include <iostream>
#include <vector>
using namespace std;

void mergeSort(vector<int>& arreglo) {
    if (arreglo.size() > 1) {
        int medio = arreglo.size() / 2;
        vector<int> izquierda(arreglo.begin(), arreglo.begin() + medio);
        vector<int> derecha(arreglo.begin() + medio, arreglo.end());

        mergeSort(izquierda);
        mergeSort(derecha);

        int i = 0, j = 0, k = 0;

        while (i < izquierda.size() && j < derecha.size()) {
            if (izquierda[i] < derecha[j]) {
                arreglo[k++] = izquierda[i++];
            } else {
                arreglo[k++] = derecha[j++];
            }
        }

        while (i < izquierda.size()) {
            arreglo[k++] = izquierda[i++];
        }

        while (j < derecha.size()) {
            arreglo[k++] = derecha[j++];
        }
    }
}

int main() {
    vector<int> arreglo = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(arreglo);
    cout << "Arreglo ordenado: ";
    for (int num : arreglo) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}