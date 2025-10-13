import java.util.*;

public class Main {
    static char[][] tableroJugador = new char[10][10];
    static char[][] tableroCPU = new char[10][10];

    static int[][] mapaBarcosJugador = new int[10][10]; 
    static int[][] mapaBarcosCPU = new int[10][10];

    static int[] partesRestantesJugador = {0, 5, 4, 3, 3, 2}; 
    static int[] partesRestantesCPU = {0, 5, 4, 3, 3, 2};

    static int aciertosJugador = 0;
    static int aciertosCPU = 0;
    static final int TOTAL_PARTES = 5 + 4 + 3 + 3 + 2;
    static Random rand = new Random();

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            inicializarTablero(tableroJugador);
            inicializarTablero(tableroCPU);

            System.out.println("Tu tablero vacío:");
            mostrarBarcos(mapaBarcosJugador);

            colocarBarcoManual(sc, mapaBarcosJugador, "Portaaviones", 5, 1);
            mostrarBarcos(mapaBarcosJugador);
            colocarBarcoManual(sc, mapaBarcosJugador, "Acorazado", 4, 2);
            mostrarBarcos(mapaBarcosJugador);
            colocarBarcoManual(sc, mapaBarcosJugador, "Submarino", 3, 3);
            mostrarBarcos(mapaBarcosJugador);
            colocarBarcoManual(sc, mapaBarcosJugador, "Destructor", 3, 4);
            mostrarBarcos(mapaBarcosJugador);
            colocarBarcoManual(sc, mapaBarcosJugador, "Patrullero", 2, 5);
            mostrarBarcos(mapaBarcosJugador);

            colocarBarcosAleatorios(mapaBarcosCPU);

            Set<String> disparosCPU = new HashSet<>();

            while (aciertosJugador < TOTAL_PARTES && aciertosCPU < TOTAL_PARTES) {
                System.out.println("\nTu tablero:");
                mostrarTablero(tableroJugador);
                System.out.println("Tablero enemigo:");
                mostrarTablero(tableroCPU);

                int fila = -1, col = -1;
                while (fila == -1) {
                    System.out.print("Dispara - Fila (A-J): ");
                    String entrada = sc.next().toUpperCase();
                    if (entrada.length() == 1) {
                        fila = letraAFila(entrada.charAt(0));
                        if (fila == -1) System.out.println("Letra inválida.");
                    } else System.out.println("Entrada inválida.");
                }
                while (col == -1) {
                    System.out.print("Columna (0-9): ");
                    String entrada = sc.next();
                    try {
                        int valor = Integer.parseInt(entrada);
                        if (valor >= 0 && valor < 10) col = valor;
                        else System.out.println("Número fuera de rango.");
                    } catch (Exception e) {
                        System.out.println("Entrada inválida.");
                    }
                }

                if (tableroCPU[fila][col] == 'X' || tableroCPU[fila][col] == 'O') {
                    System.out.println("Ya disparaste ahí.");
                } else if (mapaBarcosCPU[fila][col] > 0) {
                    System.out.println("¡Impacto!");
                    tableroCPU[fila][col] = 'X';
                    aciertosJugador++;
                    int id = mapaBarcosCPU[fila][col];
                    partesRestantesCPU[id]--;
                    if (partesRestantesCPU[id] == 0) {
                        System.out.println("¡Hundiste el " + nombreBarco(id) + " enemigo!");
                    }
                } else {
                    System.out.println("Agua...");
                    tableroCPU[fila][col] = 'O';
                }

                System.out.println("\nTurno de la computadora...");
                int f, c;
                do {
                    f = rand.nextInt(10);
                    c = rand.nextInt(10);
                } while (disparosCPU.contains(f + "," + c));
                disparosCPU.add(f + "," + c);

                System.out.println("La computadora disparó en " + (char) ('A' + f) + c);
                if (mapaBarcosJugador[f][c] > 0) {
                    System.out.println("¡La computadora te dio!");
                    tableroJugador[f][c] = 'X';
                    aciertosCPU++;
                    int id = mapaBarcosJugador[f][c];
                    partesRestantesJugador[id]--;
                    if (partesRestantesJugador[id] == 0) {
                        System.out.println("¡La computadora hundió tu " + nombreBarco(id) + "!");
                    }
                } else {
                    System.out.println("La computadora falló.");
                    tableroJugador[f][c] = 'O';
                }
            }

            if (aciertosJugador == TOTAL_PARTES) {
                System.out.println("\n¡Ganaste! Hundiste toda la flota enemiga 🎉");
            } else {
                System.out.println("\nLa computadora ganó... Hundió toda tu flota 💥");
            }

            System.out.println("\nTu tablero final:");
            mostrarTablero(tableroJugador);
            System.out.println("Tablero enemigo final:");
            mostrarTablero(tableroCPU);
        } catch (Exception e) {
            System.out.println("Ocurrió un error inesperado: " + e.getMessage());
            e.printStackTrace();
        }
    }

    static void inicializarTablero(char[][] tablero) {
        for (int i = 0; i < 10; i++)
            Arrays.fill(tablero[i], '~');
    }

    static void colocarBarcoManual(Scanner sc, int[][] matriz, String nombre, int tamaño, int idBarco) {
        boolean colocado = false;
        while (!colocado) {
            System.out.println("\nColoca tu " + nombre + " (tamaño " + tamaño + ")");
            int fila = -1, col = -1;

            while (fila == -1) {
                System.out.print("Fila inicial (A-J): ");
                String entrada = sc.next().toUpperCase();
                if (entrada.length() == 1) {
                    fila = letraAFila(entrada.charAt(0));
                    if (fila == -1) System.out.println("Letra inválida.");
                } else System.out.println("Entrada inválida.");
            }

            while (col == -1) {
                System.out.print("Columna inicial (0-9): ");
                String entrada = sc.next();
                try {
                    int valor = Integer.parseInt(entrada);
                    if (valor >= 0 && valor < 10) col = valor;
                    else System.out.println("Número fuera de rango.");
                } catch (Exception e) {
                    System.out.println("Entrada inválida.");
                }
            }

            System.out.print("Dirección (h para horizontal, v para vertical): ");
            char dir = sc.next().toLowerCase().charAt(0);

            if (dir == 'h' && col + tamaño <= 10 && espacioDisponible(matriz, fila, col, tamaño, dir)) {
                for (int i = 0; i < tamaño; i++)
                    matriz[fila][col + i] = idBarco;
                colocado = true;
            } else if (dir == 'v' && fila + tamaño <= 10 && espacioDisponible(matriz, fila, col, tamaño, dir)) {
                for (int i = 0; i < tamaño; i++)
                    matriz[fila + i][col] = idBarco;
                colocado = true;
            }

            if (!colocado) System.out.println("¡No se puede colocar ahí! Intenta otra vez.");
        }
    }

    static void colocarBarcosAleatorios(int[][] matriz) {
        int[] tamaños = {5, 4, 3, 3, 2};
        for (int id = 1; id <= tamaños.length; id++) {
            int tamaño = tamaños[id - 1];
            boolean colocado = false;
            while (!colocado) {
                int fila = rand.nextInt(10);
                int col = rand.nextInt(10);
                char dir = rand.nextBoolean() ? 'h' : 'v';

                if (dir == 'h' && col + tamaño <= 10 && espacioDisponible(matriz, fila, col, tamaño, dir)) {
                    for (int i = 0; i < tamaño; i++)
                        matriz[fila][col + i] = id;
                    colocado = true;
                } else if (dir == 'v' && fila + tamaño <= 10 && espacioDisponible(matriz, fila, col, tamaño, dir)) {
                    for (int i = 0; i < tamaño; i++)
                        matriz[fila + i][col] = id;
                    colocado = true;
                }
            }
        }
    }

    static boolean espacioDisponible(int[][] matriz, int fila, int col, int tamaño, char dir) {
        for (int i = -1; i <= tamaño; i++) {
            for (int j = -1; j <= 1; j++) {
                int f = dir == 'h' ? fila + j : fila + i;
                int c = dir == 'h' ? col + i : col + j;
                if (f >= 0 && f < 10 && c >= 0 && c < 10) {
                    if (matriz[f][c] > 0) return false;
                }
            }
        }
        return true;
    }

    static void mostrarTablero(char[][] tablero) {
        System.out.print("  ");
        for (int i = 0; i < 10; i++) System.out.print(i + " ");
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print((char) ('A' + i) + " ");
            for (int j = 0; j < 10; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
    }

    static void mostrarBarcos(int[][] matriz) {
        System.out.print("  ");
        for (int i = 0; i < 10; i++) System.out.print(i + " ");
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print((char) ('A' + i) + " ");
            for (int j = 0; j < 10; j++) {
                if (matriz[i][j] > 0) {
                    System.out.print("B ");
                } else {
                    System.out.print("~ ");
                }
            }
            System.out.println();
        }
    }

    static int letraAFila(char letra) {
        if (letra >= 'A' && letra <= 'J') {
            return letra - 'A';
        }
        return -1;
    }

    static String nombreBarco(int id) {
        switch (id) {
            case 1: return "Portaaviones";
            case 2: return "Acorazado";
            case 3: return "Submarino";
            case 4: return "Destructor";
            case 5: return "Patrullero";
            default: return "Barco desconocido";
        }
    }
}