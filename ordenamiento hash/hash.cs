using System;
using System.Collections.Generic;

class OrdenamientoHash
{
    static void Main()
    {
        int[] numeros = {36, 34, 43, 11, 15, 20, 28};
        int[] resultado = OrdenarPorHash(numeros);
        Console.WriteLine("Lista ordenada: " + string.Join(", ", resultado));
    }

    static int FuncionHash(int valor, int minimo, int tamañoIntervalo)
    {
        return (valor - minimo) / tamañoIntervalo;
    }

    static void OrdenarPorInsercion(List<int> lista)
    {
        for (int i = 1; i < lista.Count; i++)
        {
            int valorActual = lista[i];
            int j = i - 1;
            while (j >= 0 && lista[j] > valorActual)
            {
                lista[j + 1] = lista[j];
                j--;
            }
            lista[j + 1] = valorActual;
        }
    }

    static int[] OrdenarPorHash(int[] listaNumeros)
    {
        int minimo = listaNumeros[0], maximo = listaNumeros[0];
        foreach (int numero in listaNumeros)
        {
            if (numero < minimo) minimo = numero;
            if (numero > maximo) maximo = numero;
        }

        int cantidadCubetas = listaNumeros.Length;
        int tamañoIntervalo = ((maximo - minimo) / cantidadCubetas) + 1;

        List<List<int>> cubetas = new List<List<int>>();
        for (int i = 0; i < cantidadCubetas; i++)
        {
            cubetas.Add(new List<int>());
        }

        foreach (int numero in listaNumeros)
        {
            int indice = FuncionHash(numero, minimo, tamañoIntervalo);
            cubetas[indice].Add(numero);
        }

        List<int> listaOrdenada = new List<int>();
        foreach (var cubeta in cubetas)
        {
            OrdenarPorInsercion(cubeta);
            listaOrdenada.AddRange(cubeta);
        }

        return listaOrdenada.ToArray();
    }
}