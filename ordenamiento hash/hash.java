import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        int[] numeros = {36, 34, 43, 11, 15, 20, 28};
        int[] resultado = ordenarPorHash(numeros);
        System.out.print("Lista ordenada: ");
        for (int numero : resultado) {
            System.out.print(numero + " ");
        }
    }

    public static int funcionHash(int valor, int minimo, int tamañoIntervalo) {
        return (valor - minimo) / tamañoIntervalo;
    }

    public static void ordenarPorInsercion(ArrayList<Integer> lista) {
        for (int i = 1; i < lista.size(); i++) {
            int valorActual = lista.get(i);
            int j = i - 1;
            while (j >= 0 && lista.get(j) > valorActual) {
                lista.set(j + 1, lista.get(j));
                j--;
            }
            lista.set(j + 1, valorActual);
        }
    }

    public static int[] ordenarPorHash(int[] listaNumeros) {
        int minimo = listaNumeros[0], maximo = listaNumeros[0];
        for (int numero : listaNumeros) {
            if (numero < minimo) minimo = numero;
            if (numero > maximo) maximo = numero;
        }

        int cantidadCubetas = listaNumeros.length;
        int tamañoIntervalo = ((maximo - minimo) / cantidadCubetas) + 1;

        ArrayList<ArrayList<Integer>> cubetas = new ArrayList<>();
        for (int i = 0; i < cantidadCubetas; i++) {
            cubetas.add(new ArrayList<>());
        }

        for (int numero : listaNumeros) {
            int indice = funcionHash(numero, minimo, tamañoIntervalo);
            cubetas.get(indice).add(numero);
        }

        ArrayList<Integer> listaOrdenada = new ArrayList<>();
        for (ArrayList<Integer> cubeta : cubetas) {
            ordenarPorInsercion(cubeta);
            listaOrdenada.addAll(cubeta);
        }

        int[] resultado = new int[listaOrdenada.size()];
        for (int i = 0; i < listaOrdenada.size(); i++) {
            resultado[i] = listaOrdenada.get(i);
        }

        return resultado;
    }
}