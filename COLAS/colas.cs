using System;

class Cola
{
    private const int MAXSIZE = 5;
    private int[] queue = new int[MAXSIZE];
    private int front = -1, rear = -1;

    public void Insertar()
    {
        if (rear == MAXSIZE - 1)
        {
            Console.WriteLine("\nDESBORDAMIENTO (OVERFLOW)\n");
            return;
        }

        Console.Write("\nIngrese el elemento: ");
        int elemento = Convert.ToInt32(Console.ReadLine());

        if (front == -1 && rear == -1)
        {
            front = rear = 0;
        }
        else
        {
            rear++;
        }

        queue[rear] = elemento;
        Console.WriteLine("\nElemento insertado correctamente.\n");
    }

    public void Eliminar()
    {
        if (front == -1 || front > rear)
        {
            Console.WriteLine("\nSUBDESBORDAMIENTO (UNDERFLOW)\n");
            return;
        }

        int elemento = queue[front];
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front++;
        }

        Console.WriteLine($"\nElemento eliminado: {elemento}\n");
    }

    public void Mostrar()
    {
        if (rear == -1 || front == -1 || front > rear)
        {
            Console.WriteLine("\nLa cola está vacía.\n");
        }
        else
        {
            Console.WriteLine("\nElementos en la cola:");
            for (int i = front; i <= rear; i++)
            {
                Console.WriteLine(queue[i]);
            }
        }
    }

    public static void Main(string[] args)
    {
        Cola cola = new Cola();
        int opcion = 0;

        while (opcion != 4)
        {
            Console.WriteLine("\n========== MENU PRINCIPAL ==========");
            Console.WriteLine("1. Insertar elemento");
            Console.WriteLine("2. Eliminar elemento");
            Console.WriteLine("3. Mostrar cola");
            Console.WriteLine("4. Salir");
            Console.Write("Ingrese su opción: ");
            opcion = Convert.ToInt32(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    cola.Insertar();
                    break;
                case 2:
                    cola.Eliminar();
                    break;
                case 3:
                    cola.Mostrar();
                    break;
                case 4:
                    Console.WriteLine("Saliendo del programa...");
                    break;
                default:
                    Console.WriteLine("Opción inválida. Intente nuevamente.");
                    break;
            }
        }
    }
}