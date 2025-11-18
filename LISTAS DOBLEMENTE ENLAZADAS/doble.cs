using System;

class Node {
    public int data;
    public Node next;
    public Node prev;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class LinkedList {
    private Node head;
    private Node tail;
    
    private void ClearScreen() {
        Console.Clear();
    }
    
    public LinkedList() {
        head = null;
        tail = null;
    }
    
    public void BeginSet() {
        ClearScreen();
        Console.WriteLine("=== INSERTAR AL INICIO ===");
        Console.Write("Ingrese el valor del nodo: ");
        int item = Convert.ToInt32(Console.ReadLine());
        
        Node new_node = new Node(item);
        
        if (head == null) {
            head = new_node;
            tail = new_node;
            Console.WriteLine("Nodo insertado al inicio (lista estaba vacia)");
        } else {
            new_node.next = head;
            head.prev = new_node;
            head = new_node;
            Console.WriteLine("Nodo insertado al inicio correctamente");
        }
    }
    
    public void LastInsert() {
        ClearScreen();
        Console.WriteLine("=== INSERTAR AL FINAL ===");
        Console.Write("Ingrese el valor del nodo: ");
        int item = Convert.ToInt32(Console.ReadLine());
        
        Node new_node = new Node(item);
        
        if (head == null) {
            head = new_node;
            tail = new_node;
            Console.WriteLine("Nodo insertado al final (lista estaba vacia)");
        } else {
            new_node.prev = tail;
            tail.next = new_node;
            tail = new_node;
            Console.WriteLine("Nodo insertado al final correctamente");
        }
    }
    
    public void RandomInsert() {
        ClearScreen();
        Console.WriteLine("=== INSERTAR EN POSICION ESPECIFICA ===");
        Console.Write("Ingrese el valor del elemento: ");
        int item = Convert.ToInt32(Console.ReadLine());
        Console.Write("Ingrese la posicion despues de la cual desea insertar: ");
        int loc = Convert.ToInt32(Console.ReadLine());
        
        Node new_node = new Node(item);
        
        if (head == null) {
            Console.WriteLine("La lista esta vacia. Insertando al inicio...");
            head = new_node;
            tail = new_node;
        } else {
            Node temp = head;
            for (int i = 0; i < loc; i++) {
                if (temp == null) {
                    Console.WriteLine("No se puede insertar en esa posicion");
                    return;
                }
                temp = temp.next;
            }
            
            if (temp == null) {
                Console.WriteLine("No se puede insertar en esa posicion");
                return;
            }
            
            new_node.next = temp.next;
            new_node.prev = temp;
            
            if (temp.next != null) {
                temp.next.prev = new_node;
            } else {
                tail = new_node;
            }
            
            temp.next = new_node;
            Console.WriteLine($"Nodo insertado correctamente en la posicion {loc + 1}");
        }
    }
    
    public void BeginDelete() {
        ClearScreen();
        Console.WriteLine("=== ELIMINAR DEL INICIO ===");
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else {
            Node temp = head;
            head = head.next;
            
            if (head != null) {
                head.prev = null;
            } else {
                tail = null;
            }
            
            Console.WriteLine("Nodo eliminado del inicio correctamente");
        }
    }
    
    public void LastDelete() {
        ClearScreen();
        Console.WriteLine("=== ELIMINAR DEL FINAL ===");
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else if (head.next == null) {
            head = null;
            tail = null;
            Console.WriteLine("Unico nodo eliminado");
        } else {
            Node temp = tail;
            tail = tail.prev;
            tail.next = null;
            Console.WriteLine("Nodo eliminado del final correctamente");
        }
    }
    
    public void RandomDelete() {
        ClearScreen();
        Console.WriteLine("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
        Console.Write("Ingrese la posicion del nodo que desea eliminar: ");
        int loc = Convert.ToInt32(Console.ReadLine());
        
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        
        if (loc == 0) {
            BeginDelete();
            return;
        }
        
        Node temp = head;
        for (int i = 0; i < loc; i++) {
            if (temp == null) {
                Console.WriteLine("No se puede eliminar - posicion fuera de rango");
                return;
            }
            temp = temp.next;
        }
        
        if (temp == null) {
            Console.WriteLine("No se puede eliminar - posicion fuera de rango");
            return;
        }
        
        if (temp.prev != null) {
            temp.prev.next = temp.next;
        }
        
        if (temp.next != null) {
            temp.next.prev = temp.prev;
        } else {
            tail = temp.prev;
        }
        
        Console.WriteLine($"Nodo eliminado de la posicion {loc}");
    }
    
    public void Search() {
        ClearScreen();
        Console.WriteLine("=== BUSCAR ELEMENTO ===");
        if (head == null) {
            Console.WriteLine("Lista vacia");
            return;
        }
        
        Console.Write("Ingrese el elemento que desea buscar: ");
        int item = Convert.ToInt32(Console.ReadLine());
        
        Node temp = head;
        int i = 0;
        bool found = false;
        
        while (temp != null) {
            if (temp.data == item) {
                Console.WriteLine($"Elemento encontrado en la posicion {i + 1}");
                found = true;
                break;
            }
            i++;
            temp = temp.next;
        }
        
        if (!found) {
            Console.WriteLine("Elemento no encontrado");
        }
    }
    
    public void Display() {
        ClearScreen();
        Console.WriteLine("=== MOSTRAR LISTA ===");
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else {
            Console.Write("Recorrido hacia adelante: ");
            Node temp = head;
            while (temp != null) {
                Console.Write(temp.data + " ");
                temp = temp.next;
            }
            Console.WriteLine();
            
            Console.Write("Recorrido hacia atras: ");
            temp = tail;
            while (temp != null) {
                Console.Write(temp.data + " ");
                temp = temp.prev;
            }
            Console.WriteLine();
        }
    }
    
    public void Menu() {
        int choice;
        do {
            ClearScreen();
            Console.WriteLine("\n\n**Menu Principal - LISTA DOBLEMENTE ENLAZADA");
            Console.WriteLine("\nElija una opcion del siguiente menu:");
            Console.WriteLine("1. Insertar al inicio");
            Console.WriteLine("2. Insertar al final");
            Console.WriteLine("3. Insertar en posicion aleatoria");
            Console.WriteLine("4. Eliminar del inicio");
            Console.WriteLine("5. Eliminar del final");
            Console.WriteLine("6. Eliminar nodo en posicion especifica");
            Console.WriteLine("7. Buscar elemento");
            Console.WriteLine("8. Mostrar lista (ambas direcciones)");
            Console.WriteLine("9. Salir");
            
            Console.Write("\nIngrese su eleccion: ");
            choice = Convert.ToInt32(Console.ReadLine());
            
            switch (choice) {
                case 1: BeginSet(); break;
                case 2: LastInsert(); break;
                case 3: RandomInsert(); break;
                case 4: BeginDelete(); break;
                case 5: LastDelete(); break;
                case 6: RandomDelete(); break;
                case 7: Search(); break;
                case 8: Display(); break;
                case 9: 
                    ClearScreen();
                    Console.WriteLine("Saliendo del programa...");
                    break;
                default:
                    ClearScreen();
                    Console.WriteLine("Por favor ingrese una opcion valida...");
                    break;
            }
            
            if (choice != 9) {
                Console.WriteLine("\n\nPresione Enter para continuar...");
                Console.ReadLine();
            }
            
        } while (choice != 9);
    }
}

class Program {
    static void Main(string[] args) {
        LinkedList lista = new LinkedList();
        lista.Menu();
    }
}