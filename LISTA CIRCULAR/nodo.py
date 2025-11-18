import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Referencia al último nodo para optimizar inserciones
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def beginset(self):
        self.clear_screen()
        print("=== INSERTAR AL INICIO ===")
        item = int(input("Ingrese el valor del nodo: "))
        new_node = Node(item)
        
        if self.head is None:
            # Lista vacía - primer nodo
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Apunta a sí mismo
            print("Primer nodo insertado al inicio (lista circular creada)")
        else:
            # Insertar al inicio
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # El último nodo apunta al nuevo primero
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
            new_node.next = self.head
            print("Primer nodo insertado al final (lista circular creada)")
        else:
            # Insertar al final
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head  # El nuevo último apunta al primero
            print("Nodo insertado al final correctamente")
    
    def randominsert(self):
        self.clear_screen()
        print("=== INSERTAR EN POSICION ESPECIFICA ===")
        item = int(input("Ingrese el valor del elemento: "))
        loc = int(input("Ingrese la posicion despues de la cual desea insertar: "))
        
        if self.head is None:
            print("La lista esta vacia. Insertando como primer nodo...")
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return
        
        if loc < 0:
            print("Posicion no valida")
            return
        
        new_node = Node(item)
        temp = self.head
        count = 0
        
        # Navegar hasta la posición deseada
        while count < loc:
            temp = temp.next
            count += 1
            # Si damos la vuelta completa, paramos
            if temp == self.head and loc > 0:
                print("Posicion fuera de rango")
                return
        
        # Insertar después de temp
        new_node.next = temp.next
        temp.next = new_node
        
        # Actualizar tail si insertamos después del último
        if temp == self.tail:
            self.tail = new_node
        
        print(f"Nodo insertado correctamente despues de la posicion {loc}")
    
    def begin_delete(self):
        self.clear_screen()
        print("=== ELIMINAR DEL INICIO ===")
        if self.head is None:
            print("La lista esta vacia")
        elif self.head == self.tail:
            # Solo un nodo
            self.head = None
            self.tail = None
            print("Unico nodo eliminado")
        else:
            # Múltiples nodos
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head  # Actualizar referencia circular
            temp = None
            print("Nodo eliminado del inicio correctamente")
    
    def last_delete(self):
        self.clear_screen()
        print("=== ELIMINAR DEL FINAL ===")
        if self.head is None:
            print("La lista esta vacia")
        elif self.head == self.tail:
            # Solo un nodo
            self.head = None
            self.tail = None
            print("Unico nodo eliminado")
        else:
            # Múltiples nodos - encontrar el penúltimo
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            
            # Eliminar el último
            self.tail = temp
            self.tail.next = self.head
            print("Nodo eliminado del final correctamente")
    
    def random_delete(self):
        self.clear_screen()
        print("=== ELIMINAR NODO EN POSICION ESPECIFICA ===")
        loc = int(input("Ingrese la posicion del nodo que desea eliminar (0-based): "))
        
        if self.head is None:
            print("La lista esta vacia")
            return
        
        if loc == 0:
            self.begin_delete()
            return
        
        temp = self.head
        prev = None
        count = 0
        
        # Navegar hasta la posición
        while count < loc:
            prev = temp
            temp = temp.next
            count += 1
            if temp == self.head:
                print("Posicion fuera de rango")
                return
        
        # Eliminar el nodo
        prev.next = temp.next
        
        # Actualizar tail si eliminamos el último
        if temp == self.tail:
            self.tail = prev
        
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
        
        # Recorrer la lista circular
        while True:
            if temp.data == item:
                print(f"Elemento encontrado en la posicion {i}")
                found = True
                break
            
            temp = temp.next
            i += 1
            
            # Si volvemos al inicio, terminamos
            if temp == self.head:
                break
        
        if not found:
            print("Elemento no encontrado")
    
    def display(self):
        self.clear_screen()
        print("=== MOSTRAR LISTA CIRCULAR ===")
        if self.head is None:
            print("La lista esta vacia")
        else:
            temp = self.head
            print("Elementos de la lista: ", end="")
            
            # Recorrer hasta volver al inicio
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            
            print(f"\nHead: {self.head.data}, Tail: {self.tail.data}, Tail->next: {self.tail.next.data}")
            print("(La lista es circular - el ultimo nodo apunta al primero)")
    
    def menu(self):
        linked_list = self
        while True:
            self.clear_screen()
            print("\n\n********* MENU LISTA CIRCULAR *********")
            print("\nElija una opcion del siguiente menu:")
            print("1. Insertar al inicio")
            print("2. Insertar al final")
            print("3. Insertar en posicion especifica")
            print("4. Eliminar del inicio")
            print("5. Eliminar del final")
            print("6. Eliminar nodo en posicion especifica")
            print("7. Buscar elemento")
            print("8. Mostrar lista")
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
    lista = CircularLinkedList()
    lista.menu()