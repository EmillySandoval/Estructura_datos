#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int funcionHash(int valor, int minimo, int tamañoIntervalo) {
    return (valor - minimo) / tamañoIntervalo;
}

void ordenarPorInsercion(vector<int>& lista) {
    for (int i = 1; i < lista.size(); i++) {
        int valorActual = lista[i];
        int j = i - 1;
        while (j >= 0 && lista[j] > valorActual) {
            lista[j + 1] = lista[j];
            j--;
        }
        lista[j + 1] = valorActual;
    }
}

vector<int> ordenamientoHash(vector<int> listaNumeros) {
    int minimo = *min_element(listaNumeros.begin(), listaNumeros.end());
    int maximo = *max_element(listaNumeros.begin(), listaNumeros.end());
    int cantidadCubetas = listaNumeros.size();
    int tamañoIntervalo = ((maximo - minimo) / cantidadCubetas) + 1;

    vector<vector<int>> cubetas(cantidadCubetas);

    for (int numero : listaNumeros) {
        int indice = funcionHash(numero, minimo, tamañoIntervalo);
        cubetas[indice].push_back(numero);
    }

    vector<int> listaOrdenada;
    for (auto& cubeta : cubetas) {
        ordenarPorInsercion(cubeta);
        listaOrdenada.insert(listaOrdenada.end(), cubeta.begin(), cubeta.end());
    }

    return listaOrdenada;
}

int main() {
    vector<int> numeros = {36, 34, 43, 11, 15, 20, 28};
    vector<int> resultado = ordenamientoHash(numeros);

    cout << "Lista ordenada: ";
    for (int numero : resultado) {
        cout << numero << " ";
    }
    cout << endl;
    return 0;
}