import java.util.Scanner;

class Node {
    int data;
    Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList {
    private Node head;
    private Scanner scanner;
    
    public LinkedList() {
        head = null;
        scanner = new Scanner(System.in);
    }
    
    private void clearScreen() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            System.out.println("\n".repeat(50)); // Fallback
        }
    }
    
    public void beginset() {
        clearScreen();
        System.out.println("=== INSERTAR AL INICIO ===");
        System.out.print("Ingrese el valor del nodo: ");
        int item = scanner.nextInt();
        
        Node newNode = new Node(item);
        newNode.next = head;
        head = newNode;
        System.out.println("Nodo insertado al inicio correctamente");
    }
    
    public void lastinsert() {
        clearScreen();
        System.out.println("=== INSERTAR AL FINAL ===");
        System.out.print("Ingrese el valor del nodo: ");
        int item = scanner.nextInt();
        
        Node newNode = new Node(item);
        
        if (head == null) {
            head = newNode;
            System.out.println("Nodo insertado al final (lista estaba vacia)");
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            System.out.println("Nodo insertado al final correctamente");
        }
    }
    
    public void randominsert() {
        clearScreen();
        System.out.println("=== INSERTAR EN POSICION ESPECIFICA ===");
        System.out.print("Ingrese el valor del elemento: ");
        int item = scanner.nextInt();
        System.out.print("Ingrese la posicion despues de la cual desea insertar: ");
        int loc = scanner.nextInt();
        
        Node newNode = new Node(item);
        
        if (head == null) {
            System.out.println("La lista esta vacia. Insertando al inicio...");
            head = newNode;
        } else {
            Node temp = head;
            for (int i = 0; i < loc; i++) {
                if (temp == null) {
                    System.out.println("No se puede insertar en esa posicion");
                    return;
                }
                temp = temp.next;
            }
            
            if (temp == null) {
                System.out.println("No se puede insertar en esa posicion");
                return;
            }
            
            newNode.next = temp.next;
            temp.next = newNode;
            System.out.println("Nodo insertado correctamente en la posicion " + (loc + 1));
        }
    }
    
    public void beginDelete() {
        clearScreen();
        System.out.println("=== ELIMINAR DEL INICIO ===");
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else {
            head = head.next;
            System.out.println("Nodo eliminado del inicio correctamente");
        }
    }
    
    public void lastDelete() {
        clearScreen();
        System.out.println("=== ELIMINAR DEL FINAL ===");
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else if (head.next == null) {
            head = null;
            System.out.println("Unico nodo eliminado");
        } else {
            Node temp = head;
            Node prev = null;
            while (temp.next != null) {
                prev = temp;
                temp = temp.next;
            }
            prev.next = null;
            System.out.println("Nodo eliminado del final correctamente");
        }
    }
    
    public void randomDelete() {
        clearScreen();
        System.out.println("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
        System.out.print("Ingrese la posicion del nodo que desea eliminar: ");
        int loc = scanner.nextInt();
        
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        
        if (loc == 0) {
            head = head.next;
            System.out.println("Nodo eliminado de la posicion " + loc);
            return;
        }
        
        Node temp = head;
        Node prev = null;
        for (int i = 0; i < loc; i++) {
            if (temp == null) {
                System.out.println("No se puede eliminar - posicion fuera de rango");
                return;
            }
            prev = temp;
            temp = temp.next;
        }
        
        if (temp == null) {
            System.out.println("No se puede eliminar - posicion fuera de rango");
            return;
        }
        
        prev.next = temp.next;
        System.out.println("Nodo eliminado de la posicion " + loc);
    }
    
    public void search() {
        clearScreen();
        System.out.println("=== BUSCAR ELEMENTO ===");
        if (head == null) {
            System.out.println("Lista vacia");
            return;
        }
        
        System.out.print("Ingrese el elemento que desea buscar: ");
        int item = scanner.nextInt();
        
        Node temp = head;
        int i = 0;
        boolean found = false;
        
        while (temp != null) {
            if (temp.data == item) {
                System.out.println("Elemento encontrado en la posicion " + (i + 1));
                found = true;
                break;
            }
            i++;
            temp = temp.next;
        }
        
        if (!found) {
            System.out.println("Elemento no encontrado");
        }
    }
    
    public void display() {
        clearScreen();
        System.out.println("=== MOSTRAR LISTA ===");
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else {
            Node temp = head;
            System.out.print("Elementos de la lista: ");
            while (temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
            System.out.println();
        }
    }
    
    public void menu() {
        while (true) {
            clearScreen();
            System.out.println("\n\n**Menu Principal");
            System.out.println("\nElija una opcion del siguiente menu:");
            System.out.println("1. Insertar al inicio");
            System.out.println("2. Insertar al final");
            System.out.println("3. Insertar en posicion aleatoria");
            System.out.println("4. Eliminar del inicio");
            System.out.println("5. Eliminar del final");
            System.out.println("6. Eliminar nodo despues de una posicion");
            System.out.println("7. Buscar elemento");
            System.out.println("8. Mostrar lista");
            System.out.println("9. Salir");
            
            System.out.print("\nIngrese su eleccion: ");
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    beginset();
                    break;
                case 2:
                    lastinsert();
                    break;
                case 3:
                    randominsert();
                    break;
                case 4:
                    beginDelete();
                    break;
                case 5:
                    lastDelete();
                    break;
                case 6:
                    randomDelete();
                    break;
                case 7:
                    search();
                    break;
                case 8:
                    display();
                    break;
                case 9:
                    clearScreen();
                    System.out.println("Saliendo del programa...");
                    scanner.close();
                    return;
                default:
                    clearScreen();
                    System.out.println("Por favor ingrese una opcion valida...");
                    break;
            }
            
            if (choice != 9) {
                System.out.println("\n\nPresione Enter para continuar...");
                scanner.nextLine(); // Limpiar buffer
                scanner.nextLine(); // Esperar Enter
            }
        }
    }
    
    public static void main(String[] args) {
        LinkedList lista = new LinkedList();
        lista.menu();
    }
}