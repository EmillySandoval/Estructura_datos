using System;

class Programa {
    static void OrdenamientoPorSeleccion(int[] lista) {
        for (int i = 0; i < lista.Length - 1; i++) {
            int indiceMinimo = i;
            for (int j = i + 1; j < lista.Length; j++) {
                if (lista[j] < lista[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }
            int temporal = lista[i];
            lista[i] = lista[indiceMinimo];
            lista[indiceMinimo] = temporal;
        }
    }

    static void MostrarLista(int[] lista) {
        Console.WriteLine(string.Join(", ", lista));
    }

    static void Main() {
        int[] numeros = {64, 25, 12, 22, 11};

        Console.WriteLine("Lista original:");
        MostrarLista(numeros);

        OrdenamientoPorSeleccion(numeros);

        Console.WriteLine("Lista ordenada:");
        MostrarLista(numeros);
    }
}