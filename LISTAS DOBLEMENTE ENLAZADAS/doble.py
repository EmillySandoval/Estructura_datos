import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Nuevo puntero al nodo anterior

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Nueva referencia al último nodo
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def beginset(self):
        self.clear_screen()
        print("=== INSERTAR AL INICIO ===")
        item = int(input("Ingrese el valor del nodo: "))
        new_node = Node(item)
        
        if self.head is None:
            # Lista vacía
            self.head = new_node
            self.tail = new_node
            print("Nodo insertado al inicio (lista estaba vacia)")
        else:
            # Lista no vacía
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            print("Nodo insertado al inicio correctamente")
    
    def lastinsert(self):
        self.clear_screen()
        print("=== INSERTAR AL FINAL ===")
        item = int(input("Ingrese el valor del nodo: "))
        new_node = Node(item)
        
        if self.head is None:
            # Lista vacía
            self.head = new_node
            self.tail = new_node
            print("Nodo insertado al final (lista estaba vacia)")
        else:
            # Lista no vacía
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
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
            self.tail = new_node
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
            
            # Insertar después del nodo temp
            new_node.next = temp.next
            new_node.prev = temp
            
            if temp.next is not None:
                temp.next.prev = new_node
            else:
                # Si estamos insertando después del último nodo
                self.tail = new_node
            
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
            
            if self.head is not None:
                self.head.prev = None
            else:
                # Lista queda vacía
                self.tail = None
            
            temp = None
            print("Nodo eliminado del inicio correctamente")
    
    def last_delete(self):
        self.clear_screen()
        print("=== ELIMINAR DEL FINAL ===")
        if self.head is None:
            print("La lista esta vacia")
        elif self.head.next is None:
            # Solo hay un nodo
            self.head = None
            self.tail = None
            print("Unico nodo eliminado")
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
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
            # Eliminar el primer nodo
            self.begin_delete()
            return
        
        temp = self.head
        for i in range(loc):
            if temp is None:
                print("No se puede eliminar - posicion fuera de rango")
                return
            temp = temp.next
        
        if temp is None:
            print("No se puede eliminar - posicion fuera de rango")
            return
        
        # Actualizar referencias
        if temp.prev is not None:
            temp.prev.next = temp.next
        
        if temp.next is not None:
            temp.next.prev = temp.prev
        else:
            # Si eliminamos el último nodo
            self.tail = temp.prev
        
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
            print("Recorrido hacia adelante: ", end="")
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
            
            print("Recorrido hacia atrás: ", end="")
            temp = self.tail
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.prev
            print()
    
    def menu(self):
        linked_list = self
        while True:
            self.clear_screen()
            print("\n\n**Menu Principal - LISTA DOBLEMENTE ENLAZADA")
            print("\nElija una opcion del siguiente menu:")
            print("1. Insertar al inicio")
            print("2. Insertar al final")
            print("3. Insertar en posicion aleatoria")
            print("4. Eliminar del inicio")
            print("5. Eliminar del final")
            print("6. Eliminar nodo en posicion especifica")
            print("7. Buscar elemento")
            print("8. Mostrar lista (ambas direcciones)")
            print("9. Salir")
            
            try:
                choice = int(input("\nIngrese su eleccion: "))
                
                if choice == 1:
                    linked_list.beginset()
                elif choice == 2:
                    linked_list.lastinsert()
                elif choice == 3:
                    linked_list.randominsert()
                elif choice == 4:
                    linked_list.begin_delete()
                elif choice == 5:
                    linked_list.last_delete()
                elif choice == 6:
                    linked_list.random_delete()
                elif choice == 7:
                    linked_list.search()
                elif choice == 8:
                    linked_list.display()
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