import java.util.Scanner;

public class Main {
    static char[][] tablero = new char[10][10];
    static boolean[][] barcos = new boolean[10][10];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        inicializarTablero();

      
        colocarBarco(sc, "Portaaviones", 5);
        colocarBarco(sc, "Acorazado", 4);
        colocarBarco(sc, "Submarino", 3);
        colocarBarco(sc, "Destructor", 3);
        colocarBarco(sc, "Patrullero", 2);

       
        System.out.println("\n🚢 Todos los barcos han sido colocados. Aquí está tu tablero:");
        mostrarTableroConBarcos();
    }

    static void inicializarTablero() {
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < 10; j++)
                tablero[i][j] = '~'; 

    static void colocarBarco(Scanner sc, String nombre, int tamaño) {
        boolean colocado = false;
        while (!colocado) {
            System.out.println("\nColoca tu " + nombre + " (tamaño " + tamaño + ")");
            System.out.print("Fila inicial (0-9): ");
            int fila = sc.nextInt();
            System.out.print("Columna inicial (0-9): ");
            int col = sc.nextInt();
            System.out.print("Dirección (h para horizontal, v para vertical): ");
            char dir = sc.next().charAt(0);

            if (dir == 'h' && col + tamaño <= 10) {
                boolean espacioLibre = true;
                for (int i = 0; i < tamaño; i++)
                    if (barcos[fila][col + i]) espacioLibre = false;

                if (espacioLibre) {
                    for (int i = 0; i < tamaño; i++) {
                        barcos[fila][col + i] = true;
                        tablero[fila][col + i] = nombre.charAt(0);
                    }
                    colocado = true;
                }
            } else if (dir == 'v' && fila + tamaño <= 10) {
                boolean espacioLibre = true;
                for (int i = 0; i < tamaño; i++)
                    if (barcos[fila + i][col]) espacioLibre = false;

                if (espacioLibre) {
                    for (int i = 0; i < tamaño; i++) {
                        barcos[fila + i][col] = true;
                        tablero[fila + i][col] = nombre.charAt(0); 
                    }
                    colocado = true;
                }
            }

            if (!colocado) {
                System.out.println("❌ No se puede colocar ahí. Intenta otra vez.");
            }
        }
    }

    static void mostrarTableroConBarcos() {
        System.out.print("  ");
        for (int i = 0; i < 10; i++) System.out.print(i + " ");
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < 10; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
    }
}