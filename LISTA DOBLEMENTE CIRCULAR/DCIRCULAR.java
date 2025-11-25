import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node prev;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class CircularLinkedList {
    private Node head;
    private Scanner scanner;
    
    public CircularLinkedList() {
        head = null;
        scanner = new Scanner(System.in);
    }
    
    private void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
    
    public void beginset() {
        clearScreen();
        System.out.println("=== INSERTAR AL INICIO ===");
        System.out.print("Ingrese el valor del nodo: ");
        int item = scanner.nextInt();
        
        Node new_node = new Node(item);
        
        if (head == null) {
            head = new_node;
            head.next = head;
            head.prev = head;
            System.out.println("Nodo insertado al inicio (lista estaba vacia)");
        } else {
            Node last = head.prev;
            
            new_node.next = head;
            new_node.prev = last;
            
            head.prev = new_node;
            last.next = new_node;
            
            head = new_node;
            System.out.println("Nodo insertado al inicio correctamente");
        }
    }
    
    public void lastinsert() {
        clearScreen();
        System.out.println("=== INSERTAR AL FINAL ===");
        System.out.print("Ingrese el valor del nodo: ");
        int item = scanner.nextInt();
        
        Node new_node = new Node(item);
        
        if (head == null) {
            head = new_node;
            head.next = head;
            head.prev = head;
            System.out.println("Nodo insertado al final (lista estaba vacia)");
        } else {
            Node last = head.prev;
            
            new_node.next = head;
            new_node.prev = last;
            
            last.next = new_node;
            head.prev = new_node;
            
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
        
        Node new_node = new Node(item);
        
        if (head == null) {
            System.out.println("La lista esta vacia. Insertando al inicio...");
            head = new_node;
            head.next = head;
            head.prev = head;
        } else {
            Node temp = head;
            for (int i = 0; i < loc; i++) {
                temp = temp.next;
                if (temp == head) {
                    System.out.println("No se puede insertar en esa posicion");
                    return;
                }
            }
            
            new_node.next = temp.next;
            new_node.prev = temp;
            
            temp.next.prev = new_node;
            temp.next = new_node;
            
            System.out.println("Nodo insertado correctamente en la posicion " + (loc + 1));
        }
    }
    
    public void begin_delete() {
        clearScreen();
        System.out.println("=== ELIMINAR DEL INICIO ===");
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else if (head.next == head) {
            head = null;
            System.out.println("Unico nodo eliminado");
        } else {
            Node temp = head;
            Node last = head.prev;
            
            head = head.next;
            head.prev = last;
            last.next = head;
            
            System.out.println("Nodo eliminado del inicio correctamente");
        }
    }
    
    public void last_delete() {
        clearScreen();
        System.out.println("=== ELIMINAR DEL FINAL ===");
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else if (head.next == head) {
            head = null;
            System.out.println("Unico nodo eliminado");
        } else {
            Node last = head.prev;
            Node secondLast = last.prev;
            
            secondLast.next = head;
            head.prev = secondLast;
            
            System.out.println("Nodo eliminado del final correctamente");
        }
    }
    
    public void random_delete() {
        clearScreen();
        System.out.println("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
        System.out.print("Ingrese la posicion del nodo que desea eliminar: ");
        int loc = scanner.nextInt();
        
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        
        if (loc == 0) {
            begin_delete();
            return;
        }
        
        Node temp = head;
        for (int i = 0; i < loc; i++) {
            temp = temp.next;
            if (temp == head) {
                System.out.println("No se puede eliminar - posicion fuera de rango");
                return;
            }
        }
        
        if (temp.next == temp && temp.prev == temp) {
            head = null;
        } else {
            temp.prev.next = temp.next;
            temp.next.prev = temp.prev;
            
            if (temp == head) {
                head = head.next;
            }
        }
        
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
        
        do {
            if (temp.data == item) {
                System.out.println("Elemento encontrado en la posicion " + (i + 1));
                found = true;
                break;
            }
            i++;
            temp = temp.next;
        } while (temp != head);
        
        if (!found) {
            System.out.println("Elemento no encontrado");
        }
    }
    
    public void display() {
        clearScreen();
        System.out.println("=== MOSTRAR LISTA CIRCULAR ===");
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else {
            System.out.print("Recorrido hacia adelante: ");
            Node temp = head;
            do {
                System.out.print(temp.data + " ");
                temp = temp.next;
            } while (temp != head);
            System.out.println();
            
            System.out.print("Recorrido hacia atras: ");
            temp = head.prev;
            Node start = temp;
            do {
                System.out.print(temp.data + " ");
                temp = temp.prev;
            } while (temp != start);
            System.out.println();
        }
    }
    
    public void menu() {
        int choice;
        do {
            clearScreen();
            System.out.println("\n\n**Menu Principal - LISTA DOBLEMENTE ENLAZADA CIRCULAR");
            System.out.println("\nElija una opcion del siguiente menu:");
            System.out.println("1. Insertar al inicio");
            System.out.println("2. Insertar al final");
            System.out.println("3. Insertar en posicion aleatoria");
            System.out.println("4. Eliminar del inicio");
            System.out.println("5. Eliminar del final");
            System.out.println("6. Eliminar nodo en posicion especifica");
            System.out.println("7. Buscar elemento");
            System.out.println("8. Mostrar lista (ambas direcciones)");
            System.out.println("9. Salir");
            
            System.out.print("\nIngrese su eleccion: ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1: beginset(); break;
                case 2: lastinsert(); break;
                case 3: randominsert(); break;
                case 4: begin_delete(); break;
                case 5: last_delete(); break;
                case 6: random_delete(); break;
                case 7: search(); break;
                case 8: display(); break;
                case 9: 
                    clearScreen();
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    clearScreen();
                    System.out.println("Por favor ingrese una opcion valida...");
            }
            
            if (choice != 9) {
                System.out.println("\n\nPresione Enter para continuar...");
                scanner.nextLine();
                scanner.nextLine();
            }
            
        } while (choice != 9);
        scanner.close();
    }
    
    public static void main(String[] args) {
        CircularLinkedList lista = new CircularLinkedList();
        lista.menu();
    }
}