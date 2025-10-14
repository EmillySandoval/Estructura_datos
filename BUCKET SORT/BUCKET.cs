using System;
using System.Collections.Generic;

class BucketSort {
    public static List<double> OrdenarCubetas(double[] arreglo) {
        int tamaño = arreglo.Length;
        List<List<double>> cubetas = new List<List<double>>();

    
        for (int i = 0; i < tamaño; i++) {
            cubetas.Add(new List<double>());
        }

        foreach (double numero in arreglo) {
            int indice = (int)(numero * tamaño);
            cubetas[indice].Add(numero);
        }

     
        foreach (var cubeta in cubetas) {
            cubeta.Sort();
        }

        List<double> arregloOrdenado = new List<double>();
        foreach (var cubeta in cubetas) {
            arregloOrdenado.AddRange(cubeta);
        }

        return arregloOrdenado;
    }

    static void Main() {
        double[] datos = {0.42, 0.32, 0.23, 0.52, 0.25, 0.47};
        var resultado = OrdenarCubetas(datos);
        Console.WriteLine(string.Join(", ", resultado));
    }
}