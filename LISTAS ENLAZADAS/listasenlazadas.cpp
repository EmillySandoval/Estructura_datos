#include <iostream>  // Para operaciones de entrada/salida (cout, cin)
#include <cstdlib>  // Para funciones del sistema como exit()
#ifdef _WIN32
    #include <windows.h>  // Para system("cls") en Windows
#else
    #include <unistd.h>  // Para system("clear") en Linux/Mac
#endif
using namespace std;  // Uso del espacio de nombres estándar

// Definición de la estructura del nodo para la lista enlazada
struct node {
    int data;    // Almacena el valor numérico del nodo
    struct node *next; // Puntero que apunta al siguiente nodo en la lista
};

// Variable global que apunta al primer nodo de la lista
// Se inicializa automáticamente a NULL al ser una variable global
struct node *head;

// Función para limpiar la pantalla
void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// Declaración de funciones para operaciones de la lista enlazada
void beginset();   // Inserta un nuevo nodo al principio de la lista
void lastinsert();   // Inserta un nuevo nodo al final de la lista
void randominsert();   // Inserta un nuevo nodo después de una posición específica
void begin_delete();   // Elimina el primer nodo de la lista
void last_delete();   // Elimina el último nodo de la lista
void random_delete();   // Elimina un nodo después de una posición específica
void display();   // Muestra todos los elementos de la lista
void search();   // Busca un elemento específico en la lista y muestra su posición

// Función principal
int main() {
    int choice = 0;  // variable para la elección del usuario
    while (choice != 9) {  // ciclo hasta que el usuario elija salir
        clearScreen();  // Limpiar pantalla al inicio de cada ciclo
        cout << "\n\n**Menu Principal\n";  // Título del menú
        cout << "\nElija una opcion del siguiente menu:\n";  // Instrucción para elegir una opción
        // Opciones del menú
        cout << "1.Insertar al inicio\n2.Insertar al final\n3.Insertar en posicion aleatoria\n4.Eliminar del inicio\n5.Eliminar del final\n6.Eliminar nodo despues de una posicion\n7.Buscar elemento\n8.Mostrar lista\n9.Salir\n";
        cout << "\nIngrese su eleccion: ";  // Solicita la opción del usuario
        cin >> choice;  // Lee la opción del usuario

        switch (choice) {  // Evalúa la opción seleccionada
            case 1:
                clearScreen();
                beginset();  // Llama a la función para insertar al principio
                break;
            case 2:
                clearScreen();
                lastinsert();  // Llama a la función para insertar al final
                break;
            case 3:
                clearScreen();
                randominsert();  // Llama a la función para insertar en una posición específica
                break;
            case 4:
                clearScreen();
                begin_delete();  // Llama a la función para eliminar el primer nodo
                break;
            case 5:
                clearScreen();
                last_delete();  // Llama a la función para eliminar el último nodo
                break;
            case 6:
                clearScreen();
                random_delete();  // Llama a la función para eliminar un nodo en una posición específica
                break;
            case 7:
                clearScreen();
                search();  // Llama a la función para buscar un elemento en la lista
                break;
            case 8:
                clearScreen();
                display();  // Llama a la función para mostrar todos los elementos de la lista
                break;
            case 9:
                clearScreen();
                cout << "Saliendo del programa...\n";
                exit(0);  // Sale del programa
                break;
            default:
                clearScreen();
                cout << "Por favor ingrese una opcion valida...";  // Maneja opciones inválidas
        }

        // Pausa antes de volver al menú (solo si no es salir)
        if (choice != 9) {
            cout << "\n\nPresione Enter para continuar...";
            cin.ignore();
            cin.get();
        }
    }
    return 0;
}

void beginset() {
    struct node *ptr;
    int item;
    ptr = new node;
    if (ptr == NULL) {
        cout << "OVERFLOW - No hay memoria disponible\n";
    } else {
        cout << "=== INSERTAR AL INICIO ===\n";
        cout << "Ingrese el valor del nodo: ";
        cin >> item;
        ptr->data = item;
        ptr->next = head;
        head = ptr;
        cout << "Nodo insertado al inicio correctamente\n";
    }
}

void lastinsert() {
    struct node *ptr, *temp;
    int item;
    ptr = new node;
    if (ptr == NULL) {
        cout << "OVERFLOW - No hay memoria disponible\n";
    } else {
        cout << "=== INSERTAR AL FINAL ===\n";
        cout << "Ingrese el valor del nodo: ";
        cin >> item;
        ptr->data = item;
        if (head == NULL) {
            ptr->next = NULL;
            head = ptr;
            cout << "Nodo insertado al final (lista estaba vacia)\n";
        } else {
            temp = head;
            while (temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->next = NULL;
            cout << "Nodo insertado al final correctamente\n";
        }
    }
}

void randominsert() {
    int i, loc, item;
    struct node *ptr, *temp;
    ptr = new node;
    if (ptr == NULL) {
        cout << "OVERFLOW - No hay memoria disponible\n";
    } else {
        cout << "=== INSERTAR EN POSICION ESPECIFICA ===\n";
        cout << "Ingrese el valor del elemento: ";
        cin >> item;
        ptr->data = item;
        cout << "Ingrese la posicion despues de la cual desea insertar: ";
        cin >> loc;
        temp = head;

        if (head == NULL) {
            cout << "La lista esta vacia. Insertando al inicio...\n";
            ptr->next = NULL;
            head = ptr;
        } else {
            for (i = 0; i < loc; i++) {
                if (temp == NULL) {
                    cout << "No se puede insertar en esa posicion\n";
                    delete ptr;
                    return;
                }
                temp = temp->next;
            }
            ptr->next = temp->next;
            temp->next = ptr;
        }
        cout << "Nodo insertado correctamente en la posicion " << loc + 1 << endl;
    }
}

void begin_delete() {
    struct node *ptr;
    cout << "=== ELIMINAR DEL INICIO ===\n";
    if (head == NULL) {
        cout << "La lista esta vacia\n";
    } else {
        ptr = head;
        head = ptr->next;
        delete ptr;
        cout << "Nodo eliminado del inicio correctamente\n";
    }
}

void last_delete() {
    struct node *ptr, *ptr1;
    cout << "=== ELIMINAR DEL FINAL ===\n";
    if (head == NULL) {
        cout << "La lista esta vacia\n";
    } else if (head->next == NULL) {
        delete head;
        head = NULL;
        cout << "Unico nodo eliminado\n";
    } else {
        ptr = head;
        while (ptr->next != NULL) {
            ptr1 = ptr;
            ptr = ptr->next;
        }
        ptr1->next = NULL;
        delete ptr;
        cout << "Nodo eliminado del final correctamente\n";
    }
}

void random_delete() {
    struct node *ptr, *ptr1;
    int loc, i;
    cout << "=== ELIMINAR NODO EN POSICION ESPECIFICA ===\n";
    cout << "Ingrese la posicion del nodo que desea eliminar: ";
    cin >> loc;

    if (head == NULL) {
        cout << "La lista esta vacia\n";
        return;
    }

    ptr = head;
    if (loc == 0) {
        head = ptr->next;
        delete ptr;
        cout << "Nodo eliminado de la posicion " << loc << endl;
        return;
    }

    for (i = 0; i < loc; i++) {
        ptr1 = ptr;
        ptr = ptr->next;
        if (ptr == NULL) {
            cout << "No se puede eliminar - posicion fuera de rango\n";
            return;
        }
    }
    ptr1->next = ptr->next;
    delete ptr;
    cout << "Nodo eliminado de la posicion " << loc << endl;
}

void search() {
    struct node *ptr;
    int item, i = 0, flag = 1;
    cout << "=== BUSCAR ELEMENTO ===\n";
    ptr = head;
    if (ptr == NULL) {
        cout << "Lista vacia\n";
    } else {
        cout << "Ingrese el elemento que desea buscar: ";
        cin >> item;
        while (ptr != NULL) {
            if (ptr->data == item) {
                cout << "Elemento encontrado en la posicion " << i + 1 << endl;
                flag = 0;
                break;
            }
            i++;
            ptr = ptr->next;
        }
        if (flag == 1) {
            cout << "Elemento no encontrado\n";
        }
    }
}

void display() {
    struct node *ptr;
    cout << "=== MOSTRAR LISTA ===\n";
    ptr = head;
    if (ptr == NULL) {
        cout << "La lista esta vacia";
    } else {
        cout << "Elementos de la lista: ";
        while (ptr != NULL) {
            cout << ptr->data << " ";
            ptr = ptr->next;
        }
        cout << endl;
    }
}
