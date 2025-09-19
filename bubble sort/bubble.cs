using System;

class Program {
    static void BubbleSort(int[] arr) {
        int n = arr.Length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    }

    static void Main() {
        Random rand = new Random();
        int[] arr = new int[20];
        for (int i = 0; i < arr.Length; i++)
            arr[i] = rand.Next(1, 101);

        Console.WriteLine("Arreglo original:");
        Console.WriteLine(string.Join(" ", arr));

        BubbleSort(arr);

        Console.WriteLine("\nArreglo ordenado:");
        Console.WriteLine(string.Join(" ", arr));
    }
}