import java.util.Arrays;

public class MergeSortJava {

    o
    public static void mergeSort(int[] arreglo) {
        if (arreglo.length > 1) {
            int medio = arreglo.length / 2;

            
            int[] izquierda = Arrays.copyOfRange(arreglo, 0, medio);
            int[] derecha = Arrays.copyOfRange(arreglo, medio, arreglo.length);

           
            mergeSort(izquierda);
            mergeSort(derecha);

          
            int i = 0, j = 0, k = 0;

            while (i < izquierda.length && j < derecha.length) {
                if (izquierda[i] < derecha[j]) {
                    arreglo[k++] = izquierda[i++];
                } else {
                    arreglo[k++] = derecha[j++];
                }
            }

          
            while (i < izquierda.length) {
                arreglo[k++] = izquierda[i++];
            }

           
            while (j < derecha.length) {
                arreglo[k++] = derecha[j++];
            }
        }
    }
    public static void main(String[] args) {
        int[] arreglo = {38, 27, 43, 3, 9, 82, 10};
        mergeSort(arreglo);
        System.out.println("Arreglo ordenado: " + Arrays.toString(arreglo));
    }
}