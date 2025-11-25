MAXSIZE = 5
queue = [0] * MAXSIZE
front = -1
rear = -1

def insertar():
    global front, rear
    if rear == MAXSIZE - 1:
        print("\nDESBORDAMIENTO (OVERFLOW)\n")
        return
    
    try:
        elemento = int(input("\nIngrese el elemento: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    if front == -1 and rear == -1:
        front = rear = 0
    else:
        rear += 1
    
    queue[rear] = elemento
    print("\nElemento insertado correctamente.\n")

def eliminar():
    global front, rear
    if front == -1 or front > rear:
        print("\nSUBDESBORDAMIENTO (UNDERFLOW)\n")
        return
    
    elemento = queue[front]
    if front == rear:
        front = rear = -1
    else:
        front += 1
    
    print(f"\nElemento eliminado: {elemento}\n")

def mostrar():
    if rear == -1 or front == -1 or front > rear:
        print("\nLa cola está vacía.\n")
    else:
        print("\nElementos en la cola:")
        for i in range(front, rear + 1):
            print(queue[i])

def main():
    opcion = 0
    while opcion != 4:
        print("\n========== MENU PRINCIPAL ==========")
        print("1. Insertar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar cola")
        print("4. Salir")
        
        try:
            opcion = int(input("Ingrese su opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        if opcion == 1:
            insertar()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            mostrar()
        elif opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "_main_":
    main()