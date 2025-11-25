class Node:
    def _init_(self, value):
        self.data = value
        self.next = None

class Stack:
    def _init_(self):
        self.top = None
    
    def push(self, num):
        new_node = Node(num)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return -1
        
        temp = self.top
        popped_value = self.top.data
        self.top = self.top.next
        del temp
        return popped_value
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        
        current = self.top
        print("Elementos en la pila:", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Uso
if __name__ == "_main_":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Elemento Superior:", s.peek())
    print("Extrae elemento:", s.pop())
    print("Elemento Superior:", s.peek())
    s.display()