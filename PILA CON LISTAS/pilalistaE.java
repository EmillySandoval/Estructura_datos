#include <iostream>

class Node {
public:
    int data;
    Node* next;
    
    Node(int value) {
        data = value;
        next = nullptr;
    }
};

class Stack {
private:
    Node* top;

public:
    Stack() {
        top = nullptr;
    }

    ~Stack() {
        // Destructor para liberar la memoria
        while (!isEmpty()) {
            pop();
        }
    }

    void push(int num) {
        Node* newNode = new Node(num);
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (isEmpty()) {
            std::cout << "Stack Underflow" << std::endl;
            return -1;
        }
        
        Node* temp = top;
        int poppedValue = top->data;
        top = top->next;
        delete temp;
        
        return poppedValue;
    }

    int peek() {
        if (isEmpty()) {
            std::cout << "Stack is empty" << std::endl;
            return -1;
        }
        return top->data;
    }

    bool isEmpty() {
        return top == nullptr;
    }

    // No necesitamos isFull() ya que las listas enlazadas 
    // solo están limitadas por la memoria disponible
    bool isFull() {
        return false; // Las listas enlazadas no tienen límite fijo
    }

    // Método adicional para mostrar todos los elementos (opcional)
    void display() {
        if (isEmpty()) {
            std::cout << "Stack is empty" << std::endl;
            return;
        }
        
        Node* current = top;
        std::cout << "Elementos en la pila: ";
        while (current != nullptr) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }
};

int main() {
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);

    std::cout << "Elemento Superior: " << s.peek() << std::endl;
    std::cout << "Extrae elemento: " << s.pop() << std::endl;
    std::cout << "Elemento Superior: " << s.peek() << std::endl;

    // Probando el método display
    s.display();

    return 0;
}