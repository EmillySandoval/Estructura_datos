import java.util.Arrays;

public class RadixSort {
    
    // Counting Sort para un dígito específico (exp)
    static void countingSort(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];
        
        // Contar la frecuencia de cada dígito
        for (int i = 0; i < n; i++) {
            int index = (arr[i] / exp) % 10;
            count[index]++;
        }
        
        // Cambiar count[i] para que contenga la posición actual
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
        
        // Construir el array de salida
        for (int i = n - 1; i >= 0; i--) {
            int index = (arr[i] / exp) % 10;
            output[count[index] - 1] = arr[i];
            count[index]--;
        }
        
        // Copiar el array de salida al array original
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }
    
    // Función principal de Radix Sort
    static void radixSort(int[] arr) {
        int maxNum = Arrays.stream(arr).max().getAsInt();
        
        // Aplicar counting sort para cada dígito
        for (int exp = 1; maxNum / exp > 0; exp *= 10) {
            countingSort(arr, exp);
        }
    }
    
    // Ejemplo de uso
    public static void main(String[] args) {
        int[] arr = {170, 45, 75, 90, 2, 802, 24, 66};
        
        System.out.print("Array original: ");
        System.out.println(Arrays.toString(arr));
        
        radixSort(arr);
        
        System.out.print("Array ordenado: ");
        System.out.println(Arrays.toString(arr));
    }
}