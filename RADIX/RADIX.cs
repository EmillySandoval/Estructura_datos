using System;
using System.Collections.Generic;
using System.Linq;

class RadixSort {
    // Counting Sort para un dígito específico (exp)
    static void CountingSort(int[] arr, int exp) {
        int n = arr.Length;
        int[] output = new int[n];
        int[] count = new int[10];
        
        // Contar la frecuencia de cada dígito
        for (int i = 0; i < n; i++) {
            int index = (arr[i] / exp) % 10;
            count[index]++;
        }
        
        // Cambiar count[i] para que contenga la posición actual
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
        
        // Construir el array de salida
        for (int i = n - 1; i >= 0; i--) {
            int index = (arr[i] / exp) % 10;
            output[count[index] - 1] = arr[i];
            count[index]--;
        }
        
        // Copiar el array de salida al array original
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }
    
    // Función principal de Radix Sort
    static void Sort(int[] arr) {
        int maxNum = arr.Max();
        
        // Aplicar counting sort para cada dígito
        for (int exp = 1; maxNum / exp > 0; exp *= 10) {
            CountingSort(arr, exp);
        }
    }
    
    // Ejemplo de uso
    static void Main() {
        int[] arr = {170, 45, 75, 90, 2, 802, 24, 66};
        
        Console.Write("Array original: ");
        Console.WriteLine(string.Join(" ", arr));
        
        Sort(arr);
        
        Console.Write("Array ordenado: ");
        Console.WriteLine(string.Join(" ", arr));
    }
}