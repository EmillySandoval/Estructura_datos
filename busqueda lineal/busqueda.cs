using System;

class Programa {
    static int BusquedaLineal(int[] arr, int objetivo) {
        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] == objetivo)
                return i;
        }
        return -1;
    }

    static void Main() {
        int[] arreglo = {3, 8, 1, 5, 9};
        Console.WriteLine(BusquedaLineal(arreglo, 5)); 
    }
}