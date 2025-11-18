import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def beginset(self):
        self.clear_screen()
        print("=== INSERTAR AL INICIO ===")
        item = int(input("Ingrese el valor del nodo: "))
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        print("Nodo insertado al inicio correctamente")
    
    def lastinsert(self):
        self.clear_screen()
        print("=== INSERTAR AL FINAL ===")
        item = int(input("Ingrese el valor del nodo: "))
        new_node = Node(item)
        
        if self.head is None:
            self.head = new_node
            print("Nodo insertado al final (lista estaba vacia)")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            print("Nodo insertado al final correctamente")
    
    def randominsert(self):
        self.clear_screen()
        print("=== INSERTAR EN POSICION ESPECIFICA ===")
        item = int(input("Ingrese el valor del elemento: "))
        loc = int(input("Ingrese la posicion despues de la cual desea insertar: "))
        
        new_node = Node(item)
        
        if self.head is None:
            print("La lista esta vacia. Insertando al inicio...")
            self.head = new_node
        else:
            temp = self.head
            for i in range(loc):
                if temp is None:
                    print("No se puede insertar en esa posicion")
                    return
                temp = temp.next
            
            if temp is None:
                print("No se puede insertar en esa posicion")
                return
            
            new_node.next = temp.next
            temp.next = new_node
            print(f"Nodo insertado correctamente en la posicion {loc + 1}")
    
    def begin_delete(self):
        self.clear_screen()
        print("=== ELIMINAR DEL INICIO ===")
        if self.head is None:
            print("La lista esta vacia")
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            print("Nodo eliminado del inicio correctamente")
    
    def last_delete(self):
        self.clear_screen()
        print("=== ELIMINAR DEL FINAL ===")
        if self.head is None:
            print("La lista esta vacia")
        elif self.head.next is None:
            self.head = None
            print("Unico nodo eliminado")
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None
            temp = None
            print("Nodo eliminado del final correctamente")
    
    def random_delete(self):
        self.clear_screen()
        print("=== ELIMINAR NODO EN POSICION ESPECIFICA ===")
        loc = int(input("Ingrese la posicion del nodo que desea eliminar: "))
        
        if self.head is None:
            print("La lista esta vacia")
            return
        
        if loc == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
            print(f"Nodo eliminado de la posicion {loc}")
            return
        
        temp = self.head
        for i in range(loc):
            prev = temp
            temp = temp.next
            if temp is None:
                print("No se puede eliminar - posicion fuera de rango")
                return
        
        prev.next = temp.next
        temp = None
        print(f"Nodo eliminado de la posicion {loc}")
    
    def search(self):
        self.clear_screen()
        print("=== BUSCAR ELEMENTO ===")
        if self.head is None:
            print("Lista vacia")
            return
        
        item = int(input("Ingrese el elemento que desea buscar: "))
        temp = self.head
        i = 0
        found = False
        
        while temp is not None:
            if temp.data == item:
                print(f"Elemento encontrado en la posicion {i + 1}")
                found = True
                break
            i += 1
            temp = temp.next
        
        if not found:
            print("Elemento no encontrado")
    
    def display(self):
        self.clear_screen()
        print("=== MOSTRAR LISTA ===")
        if self.head is None:
            print("La lista esta vacia")
        else:
            temp = self.head
            print("Elementos de la lista: ", end="")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
    
    def menu(self):
        while True:
            self.clear_screen()
            print("\n\n**Menu Principal")
            print("\nElija una opcion del siguiente menu:")
            print("1. Insertar al inicio")
            print("2. Insertar al final")
            print("3. Insertar en posicion aleatoria")
            print("4. Eliminar del inicio")
            print("5. Eliminar del final")
            print("6. Eliminar nodo despues de una posicion")
            print("7. Buscar elemento")
            print("8. Mostrar lista")
            print("9. Salir")
            
            try:
                choice = int(input("\nIngrese su eleccion: "))
                
                if choice == 1:
                    self.beginset()
                elif choice == 2:
                    self.lastinsert()
                elif choice == 3:
                    self.randominsert()
                elif choice == 4:
                    self.begin_delete()
                elif choice == 5:
                    self.last_delete()
                elif choice == 6:
                    self.random_delete()
                elif choice == 7:
                    self.search()
                elif choice == 8:
                    self.display()
                elif choice == 9:
                    self.clear_screen()
                    print("Saliendo del programa...")
                    break
                else:
                    self.clear_screen()
                    print("Por favor ingrese una opcion valida...")
                
                if choice != 9:
                    input("\n\nPresione Enter para continuar...")
                    
            except ValueError:
                self.clear_screen()
                print("Por favor ingrese un numero valido...")
                input("\n\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    lista = LinkedList()
    lista.menu()