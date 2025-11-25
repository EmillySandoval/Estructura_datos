#include <iostream>
#include <cstdlib>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;
    
    Node(int data) {
        this->data = data;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

class CircularLinkedList {
private:
    Node* head;
    
    void clearScreen() {
        system("cls");
    }
    
public:
    CircularLinkedList() {
        head = nullptr;
    }
    
    void beginset() {
        clearScreen();
        cout << "=== INSERTAR AL INICIO ===" << endl;
        cout << "Ingrese el valor del nodo: ";
        int item;
        cin >> item;
        
        Node* new_node = new Node(item);
        
        if (head == nullptr) {
            // Lista vacía - hacerlo circular
            head = new_node;
            head->next = head;
            head->prev = head;
            cout << "Nodo insertado al inicio (lista estaba vacia)" << endl;
        } else {
            // Insertar al inicio en lista circular
            Node* last = head->prev;
            
            new_node->next = head;
            new_node->prev = last;
            
            head->prev = new_node;
            last->next = new_node;
            
            head = new_node;
            cout << "Nodo insertado al inicio correctamente" << endl;
        }
    }
    
    void lastinsert() {
        clearScreen();
        cout << "=== INSERTAR AL FINAL ===" << endl;
        cout << "Ingrese el valor del nodo: ";
        int item;
        cin >> item;
        
        Node* new_node = new Node(item);
        
        if (head == nullptr) {
            // Lista vacía
            head = new_node;
            head->next = head;
            head->prev = head;
            cout << "Nodo insertado al final (lista estaba vacia)" << endl;
        } else {
            // Insertar al final
            Node* last = head->prev;
            
            new_node->next = head;
            new_node->prev = last;
            
            last->next = new_node;
            head->prev = new_node;
            
            cout << "Nodo insertado al final correctamente" << endl;
        }
    }
    
    void randominsert() {
        clearScreen();
        cout << "=== INSERTAR EN POSICION ESPECIFICA ===" << endl;
        cout << "Ingrese el valor del elemento: ";
        int item;
        cin >> item;
        cout << "Ingrese la posicion despues de la cual desea insertar: ";
        int loc;
        cin >> loc;
        
        Node* new_node = new Node(item);
        
        if (head == nullptr) {
            cout << "La lista esta vacia. Insertando al inicio..." << endl;
            head = new_node;
            head->next = head;
            head->prev = head;
        } else {
            Node* temp = head;
            for (int i = 0; i < loc; i++) {
                temp = temp->next;
                if (temp == head) {
                    cout << "No se puede insertar en esa posicion" << endl;
                    return;
                }
            }
            
            new_node->next = temp->next;
            new_node->prev = temp;
            
            temp->next->prev = new_node;
            temp->next = new_node;
            
            cout << "Nodo insertado correctamente en la posicion " << loc + 1 << endl;
        }
    }
    
    void begin_delete() {
        clearScreen();
        cout << "=== ELIMINAR DEL INICIO ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else if (head->next == head) {
            // Solo un nodo
            delete head;
            head = nullptr;
            cout << "Unico nodo eliminado" << endl;
        } else {
            Node* temp = head;
            Node* last = head->prev;
            
            head = head->next;
            head->prev = last;
            last->next = head;
            
            delete temp;
            cout << "Nodo eliminado del inicio correctamente" << endl;
        }
    }
    
    void last_delete() {
        clearScreen();
        cout << "=== ELIMINAR DEL FINAL ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else if (head->next == head) {
            // Solo un nodo
            delete head;
            head = nullptr;
            cout << "Unico nodo eliminado" << endl;
        } else {
            Node* last = head->prev;
            Node* second_last = last->prev;
            
            second_last->next = head;
            head->prev = second_last;
            
            delete last;
            cout << "Nodo eliminado del final correctamente" << endl;
        }
    }
    
    void random_delete() {
        clearScreen();
        cout << "=== ELIMINAR NODO EN POSICION ESPECIFICA ===" << endl;
        cout << "Ingrese la posicion del nodo que desea eliminar: ";
        int loc;
        cin >> loc;
        
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        
        if (loc == 0) {
            begin_delete();
            return;
        }
        
        Node* temp = head;
        for (int i = 0; i < loc; i++) {
            temp = temp->next;
            if (temp == head) {
                cout << "No se puede eliminar - posicion fuera de rango" << endl;
                return;
            }
        }
        
        // Si estamos eliminando el último nodo y es el único
        if (temp->next == temp && temp->prev == temp) {
            delete temp;
            head = nullptr;
        } else {
            temp->prev->next = temp->next;
            temp->next->prev = temp->prev;
            
            // Si eliminamos el head, actualizar head
            if (temp == head) {
                head = head->next;
            }
            
            delete temp;
        }
        
        cout << "Nodo eliminado de la posicion " << loc << endl;
    }
    
    void search() {
        clearScreen();
        cout << "=== BUSCAR ELEMENTO ===" << endl;
        if (head == nullptr) {
            cout << "Lista vacia" << endl;
            return;
        }
        
        cout << "Ingrese el elemento que desea buscar: ";
        int item;
        cin >> item;
        
        Node* temp = head;
        int i = 0;
        bool found = false;
        
        do {
            if (temp->data == item) {
                cout << "Elemento encontrado en la posicion " << i + 1 << endl;
                found = true;
                break;
            }
            i++;
            temp = temp->next;
        } while (temp != head);
        
        if (!found) {
            cout << "Elemento no encontrado" << endl;
        }
    }
    
    void display() {
        clearScreen();
        cout << "=== MOSTRAR LISTA CIRCULAR ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else {
            cout << "Recorrido hacia adelante: ";
            Node* temp = head;
            do {
                cout << temp->data << " ";
                temp = temp->next;
            } while (temp != head);
            cout << endl;
            
            cout << "Recorrido hacia atras: ";
            temp = head->prev;
            Node* start = temp;
            do {
                cout << temp->data << " ";
                temp = temp->prev;
            } while (temp != start);
            cout << endl;
        }
    }
    
    void menu() {
        int choice;
        do {
            clearScreen();
            cout << "\n\n**Menu Principal - LISTA DOBLEMENTE ENLAZADA CIRCULAR" << endl;
            cout << "\nElija una opcion del siguiente menu:" << endl;
            cout << "1. Insertar al inicio" << endl;
            cout << "2. Insertar al final" << endl;
            cout << "3. Insertar en posicion aleatoria" << endl;
            cout << "4. Eliminar del inicio" << endl;
            cout << "5. Eliminar del final" << endl;
            cout << "6. Eliminar nodo en posicion especifica" << endl;
            cout << "7. Buscar elemento" << endl;
            cout << "8. Mostrar lista (ambas direcciones)" << endl;
            cout << "9. Salir" << endl;
            
            cout << "\nIngrese su eleccion: ";
            cin >> choice;
            
            switch (choice) {
                case 1: beginset(); break;
                case 2: lastinsert(); break;
                case 3: randominsert(); break;
                case 4: begin_delete(); break;
                case 5: last_delete(); break;
                case 6: random_delete(); break;
                case 7: search(); break;
                case 8: display(); break;
                case 9: 
                    clearScreen();
                    cout << "Saliendo del programa..." << endl;
                    break;
                default:
                    clearScreen();
                    cout << "Por favor ingrese una opcion valida..." << endl;
            }
            
            if (choice != 9) {
                cout << "\n\nPresione Enter para continuar...";
                cin.ignore();
                cin.get();
            }
            
        } while (choice != 9);
    }
};

int main() {
    CircularLinkedList lista;
    lista.menu();
    return 0;
}