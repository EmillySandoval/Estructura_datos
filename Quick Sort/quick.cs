using System;

class QuickSortPasos {
    static void QuickSort(int[] lista, int inicio, int fin, int nivel) {
        if (inicio < fin) {
            int indicePivote = Particion(lista, inicio, fin, nivel);
            QuickSort(lista, inicio, indicePivote - 1, nivel + 1);
            QuickSort(lista, indicePivote + 1, fin, nivel + 1);
        }
    }

    static int Particion(int[] lista, int inicio, int fin, int nivel) {
        int pivote = lista[fin];
        Console.Write(new string(' ', nivel * 2));
        Console.Write($"Pivote: {pivote}, Sublista: [");
        for (int k = inicio; k <= fin; k++) Console.Write(lista[k] + " ");
        Console.WriteLine("]");

        int posicion = inicio - 1;
        for (int j = inicio; j < fin; j++) {
            if (lista[j] <= pivote) {
                posicion++;
               
                int temp = lista[posicion];
                lista[posicion] = lista[j];
                lista[j] = temp;
            }
        }
       
        int tempFinal = lista[posicion + 1];
        lista[posicion + 1] = lista[fin];
        lista[fin] = tempFinal;

        return posicion + 1;
    }

    static void Main() {
        int[] numeros = {8, 3, 1, 7, 0, 10, 2};
        Console.Write("Original: ");
        foreach (int n in numeros) Console.Write(n + " ");
        Console.WriteLine();
        QuickSort(numeros, 0, numeros.Length - 1, 0);
        Console.Write("Ordenado: ");
        foreach (int n in numeros) Console.Write(n + " ");
    }
}