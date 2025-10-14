#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> ordenarCubetas(vector<double>& arreglo) {
    int tamaño = arreglo.size();
    vector<vector<double>> cubetas(tamaño);

    for (double numero : arreglo) {
        int indice = int(numero * tamaño);
        cubetas[indice].push_back(numero);
    }
 
    for (auto& cubeta : cubetas) {
        sort(cubeta.begin(), cubeta.end());
    }

    vector<double> arregloOrdenado;
    for (auto& cubeta : cubetas) {
        arregloOrdenado.insert(arregloOrdenado.end(), cubeta.begin(), cubeta.end());
    }

    return arregloOrdenado;
}

int main() {
    vector<double> datos = {0.42, 0.32, 0.23, 0.52, 0.25, 0.47};
    vector<double> resultado = ordenarCubetas(datos);

    for (double numero : resultado) {
        cout << numero << " ";
    }
    cout << endl;
}