using System;

public class Pila
{
    private const int TAMANIO_MAXIMO = 100;
    private int[] pila;
    private int tope;
    
    public Pila()
    {
        pila = new int[TAMANIO_MAXIMO];
        tope = -1;
    }
    
    public void Apilar(int numero)
    {
        if (tope == TAMANIO_MAXIMO - 1)
        {
            Console.WriteLine("Desbordamiento de Pila");
            return;
        }
        pila[++tope] = numero;
    }
    
    public int Desapilar()
    {
        if (tope == -1)
        {
            Console.WriteLine("Subdesbordamiento de Pila");
            return -1;
        }
        return pila[tope--];
    }
    
    public int Mirar()
    {
        if (tope == -1)
        {
            Console.WriteLine("La pila está vacía");
            return -1;
        }
        return pila[tope];
    }
    
    public bool EstaVacia()
    {
        return tope == -1;
    }
    
    public bool EstaLlena()
    {
        return tope == TAMANIO_MAXIMO - 1;
    }
    
    public static void Main(string[] args)
    {
        Pila p = new Pila();
        p.Apilar(10);
        p.Apilar(20);
        p.Apilar(30);
        
        Console.WriteLine("Elemento Superior: " + p.Mirar());
        Console.WriteLine("Extrae elemento: " + p.Desapilar());
        Console.WriteLine("Elemento Superior: " + p.Mirar());
    }
}