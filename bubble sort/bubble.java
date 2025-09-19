import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[20];
        Random rand = new Random();

        
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rand.nextInt(100) + 1;
        }


        System.out.println("Arreglo original:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

    
        bubbleSort(arr);

   
        System.out.println("\nArreglo ordenado:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }


    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
          
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}