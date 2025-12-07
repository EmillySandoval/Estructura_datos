using System;
using System.Collections.Generic;

class Programa {
    static List<int> OrdenarPorHash(List<int> lista) {
        Dictionary<int, int> tablaHash = new Dictionary<int, int>();

        foreach (int número in lista) {
            if (tablaHash.ContainsKey(número))
                tablaHash[número]++;
            else
                tablaHash[número] = 1;
        }

        List<int> clavesOrdenadas = new List<int>(tablaHash.Keys);
        clavesOrdenadas.Sort();

        List<int> listaOrdenada = new List<int>();
        foreach (int número in clavesOrdenadas) {
            for (int i = 0; i < tablaHash[número]; i++) {
                listaOrdenada.Add(número);
            }
        }

        return listaOrdenada;
    }

    static void Main() {
        List<int> listaNúmeros = new List<int> { 4, 2, 7, 2, 5, 4, 1 };

        Console.WriteLine("Lista original: " + string.Join(", ", listaNúmeros));
        List<int> listaFinal = OrdenarPorHash(listaNúmeros);
        Console.WriteLine("Lista ordenada por hashing: " + string.Join(", ", listaFinal));
    }
}