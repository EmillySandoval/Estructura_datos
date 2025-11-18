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

class LinkedList {
private:
    Node* head;
    Node* tail;

    void clearScreen() {
        system("cls");
    }

public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    void beginset() {
        clearScreen();
        cout << "=== INSERTAR AL INICIO ===" << endl;
        cout << "Ingrese el valor del nodo: ";
        int item;
        cin >> item;

        Node* new_node = new Node(item);

        if (head == nullptr) {
            head = new_node;
            tail = new_node;
            cout << "Nodo insertado al inicio (lista estaba vacia)" << endl;
        } else {
            new_node->next = head;
            head->prev = new_node;
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
            head = new_node;
            tail = new_node;
            cout << "Nodo insertado al final (lista estaba vacia)" << endl;
        } else {
            new_node->prev = tail;
            tail->next = new_node;
            tail = new_node;
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
            tail = new_node;
        } else {
            Node* temp = head;
            for (int i = 0; i < loc; i++) {
                if (temp == nullptr) {
                    cout << "No se puede insertar en esa posicion" << endl;
                    return;
                }
                temp = temp->next;
            }

            if (temp == nullptr) {
                cout << "No se puede insertar en esa posicion" << endl;
                return;
            }

            new_node->next = temp->next;
            new_node->prev = temp;

            if (temp->next != nullptr) {
                temp->next->prev = new_node;
            } else {
                tail = new_node;
            }

            temp->next = new_node;
            cout << "Nodo insertado correctamente en la posicion " << loc + 1 << endl;
        }
    }

    void begin_delete() {
        clearScreen();
        cout << "=== ELIMINAR DEL INICIO ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else {
            Node* temp = head;
            head = head->next;

            if (head != nullptr) {
                head->prev = nullptr;
            } else {
                tail = nullptr;
            }

            delete temp;
            cout << "Nodo eliminado del inicio correctamente" << endl;
        }
    }

    void last_delete() {
        clearScreen();
        cout << "=== ELIMINAR DEL FINAL ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else if (head->next == nullptr) {
            delete head;
            head = nullptr;
            tail = nullptr;
            cout << "Unico nodo eliminado" << endl;
        } else {
            Node* temp = tail;
            tail = tail->prev;
            tail->next = nullptr;
            delete temp;
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
            if (temp == nullptr) {
                cout << "No se puede eliminar - posicion fuera de rango" << endl;
                return;
            }
            temp = temp->next;
        }

        if (temp == nullptr) {
            cout << "No se puede eliminar - posicion fuera de rango" << endl;
            return;
        }

        if (temp->prev != nullptr) {
            temp->prev->next = temp->next;
        }

        if (temp->next != nullptr) {
            temp->next->prev = temp->prev;
        } else {
            tail = temp->prev;
        }

        delete temp;
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

        while (temp != nullptr) {
            if (temp->data == item) {
                cout << "Elemento encontrado en la posicion " << i + 1 << endl;
                found = true;
                break;
            }
            i++;
            temp = temp->next;
        }

        if (!found) {
            cout << "Elemento no encontrado" << endl;
        }
    }

    void display() {
        clearScreen();
        cout << "=== MOSTRAR LISTA ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else {
            cout << "Recorrido hacia adelante: ";
            Node* temp = head;
            while (temp != nullptr) {
                cout << temp->data << " ";
                temp = temp->next;
            }
            cout << endl;

            cout << "Recorrido hacia atras: ";
            temp = tail;
            while (temp != nullptr) {
                cout << temp->data << " ";
                temp = temp->prev;
            }
            cout << endl;
        }
    }

    void menu() {
        int choice;
        do {
            clearScreen();
            cout << "\n\n**Menu Principal - LISTA DOBLEMENTE ENLAZADA" << endl;
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
    LinkedList lista;
    lista.menu();
    return 0;
}