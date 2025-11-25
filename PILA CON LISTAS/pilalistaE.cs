using System;

public class Node
{
    public int Data { get; set; }
    public Node Next { get; set; }
    
    public Node(int value)
    {
        Data = value;
        Next = null;
    }
}

public class Stack
{
    private Node top;
    
    public Stack()
    {
        top = null;
    }
    
    public void Push(int num)
    {
        Node newNode = new Node(num);
        newNode.Next = top;
        top = newNode;
    }
    
    public int Pop()
    {
        if (IsEmpty())
        {
            Console.WriteLine("Stack Underflow");
            return -1;
        }
        
        int poppedValue = top.Data;
        top = top.Next;
        return poppedValue;
    }
    
    public int Peek()
    {
        if (IsEmpty())
        {
            Console.WriteLine("Stack is empty");
            return -1;
        }
        return top.Data;
    }
    
    public bool IsEmpty()
    {
        return top == null;
    }
    
    public void Display()
    {
        if (IsEmpty())
        {
            Console.WriteLine("Stack is empty");
            return;
        }
        
        Node current = top;
        Console.Write("Elementos en la pila: ");
        while (current != null)
        {
            Console.Write(current.Data + " ");
            current = current.Next;
        }
        Console.WriteLine();
    }
}

class Program
{
    static void Main(string[] args)
    {
        Stack s = new Stack();
        s.Push(10);
        s.Push(20);
        s.Push(30);

        Console.WriteLine("Elemento Superior: " + s.Peek());
        Console.WriteLine("Extrae elemento: " + s.Pop());
        Console.WriteLine("Elemento Superior: " + s.Peek());
        s.Display();
    }
}