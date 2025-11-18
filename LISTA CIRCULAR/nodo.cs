using System;

class Node {
    public int data;
    public Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class CircularLinkedList {
    private Node head;
    private Node tail;
    
    private void ClearScreen() {
        Console.Clear();
    }
    
    public void Beginset() {
        ClearScreen();
        Console.WriteLine("=== INSERTAR AL INICIO ===");
        Console.Write("Ingrese el valor del nodo: ");
        int item = Convert.ToInt32(Console.ReadLine());
        
        Node new_node = new Node(item);
        
        if (head == null) {
            head = new_node;
            tail = new_node;
            new_node.next = head;
            Console.WriteLine("Primer nodo insertado al inicio (lista circular creada)");
        } else {
            new_node.next = head;
            head = new_node;
            tail.next = head;
            Console.WriteLine("Nodo insertado al inicio correctamente");
        }
    }
    
    public void Lastinsert() {
        ClearScreen();
        Console.WriteLine("=== INSERTAR AL FINAL ===");
        Console.Write("Ingrese el valor del nodo: ");
        int item = Convert.ToInt32(Console.ReadLine());
        
        Node new_node = new Node(item);
        
        if (head == null) {
            head = new_node;
            tail = new_node;
            new_node.next = head;
            Console.WriteLine("Primer nodo insertado al final (lista circular creada)");
        } else {
            tail.next = new_node;
            tail = new_node;
            new_node.next = head;
            Console.WriteLine("Nodo insertado al final correctamente");
        }
    }
    
    public void Randominsert() {
        ClearScreen();
        Console.WriteLine("=== INSERTAR EN POSICION ESPECIFICA ===");
        Console.Write("Ingrese el valor del elemento: ");
        int item = Convert.ToInt32(Console.ReadLine());
        Console.Write("Ingrese la posicion despues de la cual desea insertar: ");
        int loc = Convert.ToInt32(Console.ReadLine());
        
        if (head == null) {
            Console.WriteLine("La lista esta vacia. Insertando como primer nodo...");
            Node new_node = new Node(item);
            head = new_node;
            tail = new_node;
            new_node.next = head;
            return;
        }
        
        if (loc < 0) {
            Console.WriteLine("Posicion no valida");
            return;
        }
        
        Node new_node2 = new Node(item);
        Node temp = head;
        int count = 0;
        
        while (count < loc) {
            temp = temp.next;
            count++;
            if (temp == head && loc > 0) {
                Console.WriteLine("Posicion fuera de rango");
                return;
            }
        }
        
        new_node2.next = temp.next;
        temp.next = new_node2;
        
        if (temp == tail) {
            tail = new_node2;
        }
        
        Console.WriteLine($"Nodo insertado correctamente despues de la posicion {loc}");
    }
    
    public void Begin_delete() {
        ClearScreen();
        Console.WriteLine("=== ELIMINAR DEL INICIO ===");
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else if (head == tail) {
            head = null;
            tail = null;
            Console.WriteLine("Unico nodo eliminado");
        } else {
            head = head.next;
            tail.next = head;
            Console.WriteLine("Nodo eliminado del inicio correctamente");
        }
    }
    
    public void Last_delete() {
        ClearScreen();
        Console.WriteLine("=== ELIMINAR DEL FINAL ===");
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else if (head == tail) {
            head = null;
            tail = null;
            Console.WriteLine("Unico nodo eliminado");
        } else {
            Node temp = head;
            while (temp.next != tail) {
                temp = temp.next;
            }
            tail = temp;
            tail.next = head;
            Console.WriteLine("Nodo eliminado del final correctamente");
        }
    }
    
    public void Random_delete() {
        ClearScreen();
        Console.WriteLine("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
        Console.Write("Ingrese la posicion del nodo que desea eliminar (0-based): ");
        int loc = Convert.ToInt32(Console.ReadLine());
        
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        
        if (loc == 0) {
            Begin_delete();
            return;
        }
        
        Node temp = head;
        Node prev = null;
        int count = 0;
        
        while (count < loc) {
            prev = temp;
            temp = temp.next;
            count++;
            if (temp == head) {
                Console.WriteLine("Posicion fuera de rango");
                return;
            }
        }
        
        prev.next = temp.next;
        
        if (temp == tail) {
            tail = prev;
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
        
        do {
            if (temp.data == item) {
                Console.WriteLine($"Elemento encontrado en la posicion {i}");
                found = true;
                break;
            }
            temp = temp.next;
            i++;
        } while (temp != head);
        
        if (!found) {
            Console.WriteLine("Elemento no encontrado");
        }
    }
    
    public void Display() {
        ClearScreen();
        Console.WriteLine("=== MOSTRAR LISTA CIRCULAR ===");
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else {
            Node temp = head;
            Console.Write("Elementos de la lista: ");
            do {
                Console.Write(temp.data + " ");
                temp = temp.next;
            } while (temp != head);
            Console.WriteLine();
            Console.WriteLine($"Head: {head.data}, Tail: {tail.data}, Tail->next: {tail.next.data}");
            Console.WriteLine("(La lista es circular - el ultimo nodo apunta al primero)");
        }
    }
    
    public void Menu() {
        int choice;
        do {
            ClearScreen();
            Console.WriteLine("\n\n********* MENU LISTA CIRCULAR *********");
            Console.WriteLine("\nElija una opcion del siguiente menu:");
            Console.WriteLine("1. Insertar al inicio");
            Console.WriteLine("2. Insertar al final");
            Console.WriteLine("3. Insertar en posicion especifica");
            Console.WriteLine("4. Eliminar del inicio");
            Console.WriteLine("5. Eliminar del final");
            Console.WriteLine("6. Eliminar nodo en posicion especifica");
            Console.WriteLine("7. Buscar elemento");
            Console.WriteLine("8. Mostrar lista");
            Console.WriteLine("9. Salir");
            
            Console.Write("\nIngrese su eleccion: ");
            choice = Convert.ToInt32(Console.ReadLine());
            
            switch (choice) {
                case 1: Beginset(); break;
                case 2: Lastinsert(); break;
                case 3: Randominsert(); break;
                case 4: Begin_delete(); break;
                case 5: Last_delete(); break;
                case 6: Random_delete(); break;
                case 7: Search(); break;
                case 8: Display(); break;
                case 9: Console.WriteLine("Saliendo del programa..."); break;
                default: Console.WriteLine("Por favor ingrese una opcion valida..."); break;
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
        CircularLinkedList lista = new CircularLinkedList();
        lista.Menu();
    }
}