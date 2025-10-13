class OrdenamientoHeap {

    
    public void crearMonticulo(int[] arreglo, int tamaño, int índiceRaíz) {
        int índiceMayor = índiceRaíz;
        int índiceIzquierdo = 2 * índiceRaíz + 1;
        int índiceDerecho = 2 * índiceRaíz + 2;

        if (índiceIzquierdo < tamaño && arreglo[índiceIzquierdo] > arreglo[índiceMayor]) {
            índiceMayor = índiceIzquierdo;
        }

        if (índiceDerecho < tamaño && arreglo[índiceDerecho] > arreglo[índiceMayor]) {
            índiceMayor = índiceDerecho;
        }

        if (índiceMayor != índiceRaíz) {
            int temporal = arreglo[índiceRaíz];
            arreglo[índiceRaíz] = arreglo[índiceMayor];
            arreglo[índiceMayor] = temporal;

            crearMonticulo(arreglo, tamaño, índiceMayor);
        }
    }


    public void ordenarHeap(int[] arreglo) {
        int tamaño = arreglo.length;

        for (int i = tamaño / 2 - 1; i >= 0; i--) {
            crearMonticulo(arreglo, tamaño, i);
        }

        for (int i = tamaño - 1; i >= 0; i--) {
            int temporal = arreglo[0];
            arreglo[0] = arreglo[i];
            arreglo[i] = temporal;

            crearMonticulo(arreglo, i, 0);
        }
    }

  
    public void mostrarArreglo(int[] arreglo) {
        for (int número : arreglo) {
            System.out.print(número + " ");
        }
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        OrdenamientoHeap ordenamiento = new OrdenamientoHeap();
        int[] arreglo = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Arreglo original:");
        ordenamiento.mostrarArreglo(arreglo);

        ordenamiento.ordenarHeap(arreglo);

        System.out.println("Arreglo ordenado con Heap Sort:");
        ordenamiento.mostrarArreglo(arreglo);
    }
}