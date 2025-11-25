import java.util.Scanner;

public class Cola {
    private static final int MAXSIZE = 5;
    private static int[] queue = new int[MAXSIZE];
    private static int front = -1, rear = -1;
    private static Scanner scanner = new Scanner(System.in);

    public static void insertar() {
        if (rear == MAXSIZE - 1) {
            System.out.println("\nDESBORDAMIENTO (OVERFLOW)\n");
            return;
        }

        System.out.print("\nIngrese el elemento: ");
        int elemento = scanner.nextInt();

        if (front == -1 && rear == -1) {
            front = rear = 0;
        } else {
            rear++;
        }

        queue[rear] = elemento;
        System.out.println("\nElemento insertado correctamente.\n");
    }

    public static void eliminar() {
        if (front == -1 || front > rear) {
            System.out.println("\nSUBDESBORDAMIENTO (UNDERFLOW)\n");
            return;
        }

        int elemento = queue[front];
        if (front == rear) {
            front = rear = -1;
        } else {
            front++;
        }

        System.out.println("\nElemento eliminado: " + elemento + "\n");
    }

    public static void mostrar() {
        if (rear == -1 || front == -1 || front > rear) {
            System.out.println("\nLa cola está vacía.\n");
        } else {
            System.out.println("\nElementos en la cola:");
            for (int i = front; i <= rear; i++) {
                System.out.println(queue[i]);
            }
        }
    }

    public static void main(String[] args) {
        int opcion = 0;
        
        while (opcion != 4) {
            System.out.println("\n========== MENU PRINCIPAL ==========");
            System.out.println("1. Insertar elemento");
            System.out.println("2. Eliminar elemento");
            System.out.println("3. Mostrar cola");
            System.out.println("4. Salir");
            System.out.print("Ingrese su opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    insertar();
                    break;
                case 2:
                    eliminar();
                    break;
                case 3:
                    mostrar();
                    break;
                case 4:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
                    break;
            }
        }
        scanner.close();
    }
}