import java.util.Random;

public class Main {
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i], j = i - 1;
            while (j >= 0 && arr[j] > key)
                arr[j + 1] = arr[j--];
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        Random rand = new Random();
        int[] arr = new int[10];
        System.out.print("Antes de ordenar: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rand.nextInt(100) + 1;
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        insertionSort(arr);

        System.out.print("Después de ordenar: ");
        for (int num : arr)
            System.out.print(num + " ");
        System.out.println();
    }
}