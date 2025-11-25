class Node {
    constructor(value) {
        this.data = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
    }
    
    push(num) {
        const newNode = new Node(num);
        newNode.next = this.top;
        this.top = newNode;
    }
    
    pop() {
        if (this.isEmpty()) {
            console.log("Stack Underflow");
            return -1;
        }
        
        const poppedValue = this.top.data;
        this.top = this.top.next;
        return poppedValue;
    }
    
    peek() {
        if (this.isEmpty()) {
            console.log("Stack is empty");
            return -1;
        }
        return this.top.data;
    }
    
    isEmpty() {
        return this.top === null;
    }
    
    display() {
        if (this.isEmpty()) {
            console.log("Stack is empty");
            return;
        }
        
        let current = this.top;
        let elements = [];
        while (current !== null) {
            elements.push(current.data);
            current = current.next;
        }
        console.log("Elementos en la pila: " + elements.join(" "));
    }
}

// Uso
const s = new Stack();
s.push(10);
s.push(20);
s.push(30);

console.log("Elemento Superior: " + s.peek());
console.log("Extrae elemento: " + s.pop());
console.log("Elemento Superior: " + s.peek());
s.display();

// Pruebas adicionales
console.log("\n--- Pruebas adicionales ---");
s.push(40);
s.push(50);
console.log("Elemento Superior después de nuevos push: " + s.peek());
s.display();

console.log("Extrae elemento: " + s.pop());
console.log("Extrae elemento: " + s.pop());
console.log("Extrae elemento: " + s.pop());
console.log("Intenta extraer de pila vacía: " + s.pop());
s.display();