public class Main {
    public static void ordenamientoPorSeleccion(int[] lista) {
        for (int i = 0; i < lista.length - 1; i++) {
            int indiceMinimo = i;
            for (int j = i + 1; j < lista.length; j++) {
                if (lista[j] < lista[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }
       
            int temporal = lista[i];
            lista[i] = lista[indiceMinimo];
            lista[indiceMinimo] = temporal;
        }
    }

  
    public static void mostrarLista(int[] lista) {
        for (int numero : lista) {
            System.out.print(numero + " ");
        }
        System.out.println();
    }

    
    public static void main(String[] args) {
        int[] numeros = {64, 25, 12, 22, 11};

        System.out.println("Lista original:");
        mostrarLista(numeros);

        ordenamientoPorSeleccion(numeros);

        System.out.println("Lista ordenada:");
        mostrarLista(numeros);
    }
}