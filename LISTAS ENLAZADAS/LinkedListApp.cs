using System;

namespace LinkedListApp
{
    class Node
    {
        public int data;
        public Node next;
        
        public Node(int data)
        {
            this.data = data;
            this.next = null;
        }
    }
    
    class LinkedList
    {
        private Node head;
        
        public LinkedList()
        {
            head = null;
        }
        
        private void ClearScreen()
        {
            Console.Clear();
        }
        
        public void Beginset()
        {
            ClearScreen();
            Console.WriteLine("=== INSERTAR AL INICIO ===");
            Console.Write("Ingrese el valor del nodo: ");
            int item = Convert.ToInt32(Console.ReadLine());
            
            Node newNode = new Node(item);
            newNode.next = head;
            head = newNode;
            Console.WriteLine("Nodo insertado al inicio correctamente");
        }
        
        public void Lastinsert()
        {
            ClearScreen();
            Console.WriteLine("=== INSERTAR AL FINAL ===");
            Console.Write("Ingrese el valor del nodo: ");
            int item = Convert.ToInt32(Console.ReadLine());
            
            Node newNode = new Node(item);
            
            if (head == null)
            {
                head = newNode;
                Console.WriteLine("Nodo insertado al final (lista estaba vacia)");
            }
            else
            {
                Node temp = head;
                while (temp.next != null)
                {
                    temp = temp.next;
                }
                temp.next = newNode;
                Console.WriteLine("Nodo insertado al final correctamente");
            }
        }
        
        public void Randominsert()
        {
            ClearScreen();
            Console.WriteLine("=== INSERTAR EN POSICION ESPECIFICA ===");
            Console.Write("Ingrese el valor del elemento: ");
            int item = Convert.ToInt32(Console.ReadLine());
            Console.Write("Ingrese la posicion despues de la cual desea insertar: ");
            int loc = Convert.ToInt32(Console.ReadLine());
            
            Node newNode = new Node(item);
            
            if (head == null)
            {
                Console.WriteLine("La lista esta vacia. Insertando al inicio...");
                head = newNode;
            }
            else
            {
                Node temp = head;
                for (int i = 0; i < loc; i++)
                {
                    if (temp == null)
                    {
                        Console.WriteLine("No se puede insertar en esa posicion");
                        return;
                    }
                    temp = temp.next;
                }
                
                if (temp == null)
                {
                    Console.WriteLine("No se puede insertar en esa posicion");
                    return;
                }
                
                newNode.next = temp.next;
                temp.next = newNode;
                Console.WriteLine($"Nodo insertado correctamente en la posicion {loc + 1}");
            }
        }
        
        public void BeginDelete()
        {
            ClearScreen();
            Console.WriteLine("=== ELIMINAR DEL INICIO ===");
            if (head == null)
            {
                Console.WriteLine("La lista esta vacia");
            }
            else
            {
                head = head.next;
                Console.WriteLine("Nodo eliminado del inicio correctamente");
            }
        }
        
        public void LastDelete()
        {
            ClearScreen();
            Console.WriteLine("=== ELIMINAR DEL FINAL ===");
            if (head == null)
            {
                Console.WriteLine("La lista esta vacia");
            }
            else if (head.next == null)
            {
                head = null;
                Console.WriteLine("Unico nodo eliminado");
            }
            else
            {
                Node temp = head;
                Node prev = null;
                while (temp.next != null)
                {
                    prev = temp;
                    temp = temp.next;
                }
                prev.next = null;
                Console.WriteLine("Nodo eliminado del final correctamente");
            }
        }
        
        public void RandomDelete()
        {
            ClearScreen();
            Console.WriteLine("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
            Console.Write("Ingrese la posicion del nodo que desea eliminar: ");
            int loc = Convert.ToInt32(Console.ReadLine());
            
            if (head == null)
            {
                Console.WriteLine("La lista esta vacia");
                return;
            }
            
            if (loc == 0)
            {
                head = head.next;
                Console.WriteLine($"Nodo eliminado de la posicion {loc}");
                return;
            }
            
            Node temp = head;
            Node prev = null;
            for (int i = 0; i < loc; i++)
            {
                if (temp == null)
                {
                    Console.WriteLine("No se puede eliminar - posicion fuera de rango");
                    return;
                }
                prev = temp;
                temp = temp.next;
            }
            
            if (temp == null)
            {
                Console.WriteLine("No se puede eliminar - posicion fuera de rango");
                return;
            }
            
            prev.next = temp.next;
            Console.WriteLine($"Nodo eliminado de la posicion {loc}");
        }
        
        public void Search()
        {
            ClearScreen();
            Console.WriteLine("=== BUSCAR ELEMENTO ===");
            if (head == null)
            {
                Console.WriteLine("Lista vacia");
                return;
            }
            
            Console.Write("Ingrese el elemento que desea buscar: ");
            int item = Convert.ToInt32(Console.ReadLine());
            
            Node temp = head;
            int i = 0;
            bool found = false;
            
            while (temp != null)
            {
                if (temp.data == item)
                {
                    Console.WriteLine($"Elemento encontrado en la posicion {i + 1}");
                    found = true;
                    break;
                }
                i++;
                temp = temp.next;
            }
            
            if (!found)
            {
                Console.WriteLine("Elemento no encontrado");
            }
        }
        
        public void Display()
        {
            ClearScreen();
            Console.WriteLine("=== MOSTRAR LISTA ===");
            if (head == null)
            {
                Console.WriteLine("La lista esta vacia");
            }
            else
            {
                Node temp = head;
                Console.Write("Elementos de la lista: ");
                while (temp != null)
                {
                    Console.Write(temp.data + " ");
                    temp = temp.next;
                }
                Console.WriteLine();
            }
        }
        
        public void Menu()
        {
            while (true)
            {
                ClearScreen();
                Console.WriteLine("\n\n**Menu Principal");
                Console.WriteLine("\nElija una opcion del siguiente menu:");
                Console.WriteLine("1. Insertar al inicio");
                Console.WriteLine("2. Insertar al final");
                Console.WriteLine("3. Insertar en posicion aleatoria");
                Console.WriteLine("4. Eliminar del inicio");
                Console.WriteLine("5. Eliminar del final");
                Console.WriteLine("6. Eliminar nodo despues de una posicion");
                Console.WriteLine("7. Buscar elemento");
                Console.WriteLine("8. Mostrar lista");
                Console.WriteLine("9. Salir");
                
                Console.Write("\nIngrese su eleccion: ");
                string input = Console.ReadLine();
                
                if (int.TryParse(input, out int choice))
                {
                    switch (choice)
                    {
                        case 1:
                            Beginset();
                            break;
                        case 2:
                            Lastinsert();
                            break;
                        case 3:
                            Randominsert();
                            break;
                        case 4:
                            BeginDelete();
                            break;
                        case 5:
                            LastDelete();
                            break;
                        case 6:
                            RandomDelete();
                            break;
                        case 7:
                            Search();
                            break;
                        case 8:
                            Display();
                            break;
                        case 9:
                            ClearScreen();
                            Console.WriteLine("Saliendo del programa...");
                            return;
                        default:
                            ClearScreen();
                            Console.WriteLine("Por favor ingrese una opcion valida...");
                            break;
                    }
                    
                    if (choice != 9)
                    {
                        Console.WriteLine("\n\nPresione Enter para continuar...");
                        Console.ReadLine();
                    }
                }
                else
                {
                    ClearScreen();
                    Console.WriteLine("Por favor ingrese un numero valido...");
                    Console.WriteLine("\n\nPresione Enter para continuar...");
                    Console.ReadLine();
                }
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            LinkedList lista = new LinkedList();
            lista.Menu();
        }
    }
}