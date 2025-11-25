#include <iostream>
#define TAMANIO_MAXIMO 100

class Pila {
private:
    int pila[TAMANIO_MAXIMO];
    int tope;

public:
    Pila() {
        tope = -1;
    }

    void apilar(int numero) {
        if (tope == TAMANIO_MAXIMO - 1) {
            std::cout << "Desbordamiento de Pila" << std::endl;
            return;
        }
        pila[++tope] = numero;
    }

    int desapilar() {
        if (tope == -1) {
            std::cout << "Subdesbordamiento de Pila" << std::endl;
            return -1;
        }
        return pila[tope--];
    }

    int mirar() {
        if (tope == -1) {
            std::cout << "La pila está vacía" << std::endl;
            return -1;
        }
        return pila[tope];
    }

    bool estaVacia() {
        return tope == -1;
    }

    bool estaLlena() {
        return tope == TAMANIO_MAXIMO - 1;
    }
};

int main() {
    Pila p;
    p.apilar(10);
    p.apilar(20);
    p.apilar(30);

    std::cout << "Elemento Superior: " << p.mirar() << std::endl;
    std::cout << "Extrae elemento: " << p.desapilar() << std::endl;
    std::cout << "Elemento Superior: " << p.mirar() << std::endl;

    return 0;
}