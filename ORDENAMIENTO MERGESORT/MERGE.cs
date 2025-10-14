using System;

class MergeSortCSharp {
    public static void MergeSort(int[] arreglo) {
        if (arreglo.Length > 1) {
            int medio = arreglo.Length / 2;
            int[] izquierda = new int[medio];
            int[] derecha = new int[arreglo.Length - medio];

            Array.Copy(arreglo, 0, izquierda, 0, medio);
            Array.Copy(arreglo, medio, derecha, 0, arreglo.Length - medio);

            MergeSort(izquierda);
            MergeSort(derecha);

            int i = 0, j = 0, k = 0;

            while (i < izquierda.Length && j < derecha.Length) {
                if (izquierda[i] < derecha[j]) {
                    arreglo[k++] = izquierda[i++];
                } else {
                    arreglo[k++] = derecha[j++];
                }
            }

            while (i < izquierda.Length) {
                arreglo[k++] = izquierda[i++];
            }

            while (j < derecha.Length) {
                arreglo[k++] = derecha[j++];
            }
        }
    }

    static void Main() {
        int[] arreglo = {38, 27, 43, 3, 9, 82, 10};
        MergeSort(arreglo);
        Console.WriteLine("Arreglo ordenado: " + string.Join(", ", arreglo));
    }
}