using System;

class Program {
    static void InsertionSort(int[] arr) {
        for (int i = 1; i < arr.Length; i++) {
            int key = arr[i], j = i - 1;
            while (j >= 0 && arr[j] > key)
                arr[j + 1] = arr[j--];
            arr[j + 1] = key;
        }
    }

    static void Main() {
        Random rnd = new Random();
        int[] arr = new int[10];
        for (int i = 0; i < arr.Length; i++)
            arr[i] = rnd.Next(1, 101);

        Console.WriteLine("Antes de ordenar: " + string.Join(", ", arr));
        InsertionSort(arr);
        Console.WriteLine("Después de ordenar: " + string.Join(", ", arr));
    }
}