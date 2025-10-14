import java.util.*;

public class BucketSort {
    public static List<Double> ordenarCubetas(double[] arreglo) {
        int tamaño = arreglo.length;
        List<List<Double>> cubetas = new ArrayList<>();

        for (int i = 0; i < tamaño; i++) {
            cubetas.add(new ArrayList<>());
        }

        for (double numero : arreglo) {
            int indice = (int)(numero * tamaño);
            cubetas.get(indice).add(numero);
        }

        for (List<Double> cubeta : cubetas) {
            Collections.sort(cubeta);
        }

     
        List<Double> arregloOrdenado = new ArrayList<>();
        for (List<Double> cubeta : cubetas) {
            arregloOrdenado.addAll(cubeta);
        }

        return arregloOrdenado;
    }

    public static void main(String[] args) {
        double[] datos = {0.42, 0.32, 0.23, 0.52, 0.25, 0.47};
        List<Double> resultado = ordenarCubetas(datos);
        System.out.println(resultado);
    }
}