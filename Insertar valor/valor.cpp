#include <iostream>
#include <vector>

std::vector<int> insertarEnIndice(std::vector<int> lista, int valor, int indice) {
    lista.insert(lista.begin() + indice, valor);
    return lista;
}

int main() {
    std::vector<int> miLista = {1, 2, 3, 5};
    miLista = insertarEnIndice(miLista, 4, 3);
    for (int num : miLista) std::cout << num << " ";
    return 0;
}