using System;

class Program
{
    static void Main()
    {
        int[,] matriz2D = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        int[] matriz1D = new int[9];
        int index = 0;

        Console.WriteLine("Matriz 2D original:");
        for (int i = 0; i < matriz2D.GetLength(0); i++)
        {
            for (int j = 0; j < matriz2D.GetLength(1); j++)
            {
                Console.Write(matriz2D[i, j] + " ");
                matriz1D[index++] = matriz2D[i, j];
            }
            Console.WriteLine();
        }

        Console.WriteLine("\nMatriz 1D:");
        foreach (int val in matriz1D)
            Console.Write(val + " ");

    }
}