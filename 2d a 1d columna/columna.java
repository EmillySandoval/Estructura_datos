public class Main {
    public static void main(String[] args) {
        int[][] matriz2D = {{1,2,3},{4,5,6},{7,8,9}};
        int[] matriz1D = new int[9];
        int index = 0;

        System.out.println("Matriz 2D original:");
        for (int i = 0; i < matriz2D.length; i++) {
            for (int j = 0; j < matriz2D[i].length; j++) {
                System.out.print(matriz2D[i][j] + " ");
            }
            System.out.println();
        }

        for (int j = 0; j < matriz2D[0].length; j++) {
            for (int i = 0; i < matriz2D.length; i++) {
                matriz1D[index++] = matriz2D[i][j];
            }
        }

        System.out.println("\nMatriz 1D (por columnas):");
        for (int val : matriz1D)
            System.out.print(val + " ");

       
    }
}