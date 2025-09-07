using System;
using System.Collections.Generic;

class Program {
    static List<int> InsertarEnIndice(List<int> lista, int valor, int indice) {
        lista.Insert(indice, valor);
        return lista;
    }

    static void Main() {
        List<int> miLista = new List<int> {1, 2, 3, 5};
        miLista = InsertarEnIndice(miLista, 4, 3);
        Console.WriteLine(string.Join(", ", miLista));
    }
}