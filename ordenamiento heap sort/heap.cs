using System;

class OrdenamientoHeap
{
   
    static void CrearMonticulo(int[] arreglo, int tamaño, int índiceRaíz)
    {
        int índiceMayor = índiceRaíz;
        int índiceIzquierdo = 2 * índiceRaíz + 1;
        int índiceDerecho = 2 * índiceRaíz + 2;

        if (índiceIzquierdo < tamaño && arreglo[índiceIzquierdo] > arreglo[índiceMayor])
        {
            índiceMayor = índiceIzquierdo;
        }

     
        if (índiceDerecho < tamaño && arreglo[índiceDerecho] > arreglo[índiceMayor])
        {
            índiceMayor = índiceDerecho;
        }

        if (índiceMayor != índiceRaíz)
        {
            int temporal = arreglo[índiceRaíz];
            arreglo[índiceRaíz] = arreglo[índiceMayor];
            arreglo[índiceMayor] = temporal;

            CrearMonticulo(arreglo, tamaño, índiceMayor);
        }
    }

   
    public static void OrdenarHeap(int[] arreglo)
    {
        int tamaño = arreglo.Length;

  
        for (int i = tamaño / 2 - 1; i >= 0; i--)
        {
            CrearMonticulo(arreglo, tamaño, i);
        }

       
        for (int i = tamaño - 1; i >= 0; i--)
        {
            int temporal = arreglo[0];
            arreglo[0] = arreglo[i];
            arreglo[i] = temporal;

            CrearMonticulo(arreglo, i, 0);
        }
    }


    public static void MostrarArreglo(int[] arreglo)
    {
        foreach (int número in arreglo)
        {
            Console.Write(número + " ");
        }
        Console.WriteLine();
    }

    
    static void Main()
    {
        int[] arreglo = { 12, 11, 13, 5, 6, 7 };
        Console.WriteLine("Arreglo original:");
        MostrarArreglo(arreglo);

        OrdenarHeap(arreglo);

        Console.WriteLine("Arreglo ordenado con Heap Sort:");
        MostrarArreglo(arreglo);
    }
}