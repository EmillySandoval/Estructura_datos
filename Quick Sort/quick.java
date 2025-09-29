public class Main {

    public static void quickSort(int[] lista, int inicio, int fin, int nivel) {
        if (inicio < fin) {
            int pivote = particion(lista, inicio, fin, nivel);
            quickSort(lista, inicio, pivote - 1, nivel + 1);
            quickSort(lista, pivote + 1, fin, nivel + 1);
        }
    }

    public static int particion(int[] lista, int inicio, int fin, int nivel) {
        int pivote = lista[fin];
        System.out.print("  ".repeat(nivel));
        System.out.print("Pivote: " + pivote + ", Sublista: [");
        for (int k = inicio; k <= fin; k++) {
            System.out.print(lista[k] + " ");
        }
        System.out.println("]");

        int i = inicio - 1;
        for (int j = inicio; j < fin; j++) {
            if (lista[j] <= pivote) {
                i++;
                int temp = lista[i];
                lista[i] = lista[j];
                lista[j] = temp;
            }
        }
        int temp = lista[i + 1];
        lista[i + 1] = lista[fin];
        lista[fin] = temp;
        return i + 1;
    }

    public static void main(String[] args) {
        int[] numeros = {8, 3, 1, 7, 0, 10, 2};
        System.out.print("Original: ");
        for (int n : numeros) {
            System.out.print(n + " ");
        }
        System.out.println();

        quickSort(numeros, 0, numeros.length - 1, 0);

        System.out.print("Ordenado: ");
        for (int n : numeros) {
            System.out.print(n + " ");
        }
    }
}