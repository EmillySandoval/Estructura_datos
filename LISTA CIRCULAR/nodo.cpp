#include <iostream>
#include <cstdlib>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class CircularLinkedList {
private:
    Node* head;
    Node* tail;

    void clearScreen() {
        system("cls");
    }

public:
    CircularLinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    void beginset() {
        clearScreen();
        cout << "=== INSERTAR AL INICIO ===" << endl;
        int item;
        cout << "Ingrese el valor del nodo: ";
        cin >> item;

        Node* new_node = new Node(item);

        if (head == nullptr) {
            head = new_node;
            tail = new_node;
            new_node->next = head;
            cout << "Primer nodo insertado al inicio (lista circular creada)" << endl;
        } else {
            new_node->next = head;
            head = new_node;
            tail->next = head;
            cout << "Nodo insertado al inicio correctamente" << endl;
        }
    }

    void lastinsert() {
        clearScreen();
        cout << "=== INSERTAR AL FINAL ===" << endl;
        int item;
        cout << "Ingrese el valor del nodo: ";
        cin >> item;

        Node* new_node = new Node(item);

        if (head == nullptr) {
            head = new_node;
            tail = new_node;
            new_node->next = head;
            cout << "Primer nodo insertado al final (lista circular creada)" << endl;
        } else {
            tail->next = new_node;
            tail = new_node;
            new_node->next = head;
            cout << "Nodo insertado al final correctamente" << endl;
        }
    }

    void randominsert() {
        clearScreen();
        cout << "=== INSERTAR EN POSICION ESPECIFICA ===" << endl;
        int item, loc;
        cout << "Ingrese el valor del elemento: ";
        cin >> item;
        cout << "Ingrese la posicion despues de la cual desea insertar: ";
        cin >> loc;

        if (head == nullptr) {
            cout << "La lista esta vacia. Insertando como primer nodo..." << endl;
            Node* new_node = new Node(item);
            head = new_node;
            tail = new_node;
            new_node->next = head;
            return;
        }

        if (loc < 0) {
            cout << "Posicion no valida" << endl;
            return;
        }

        Node* new_node = new Node(item);
        Node* temp = head;
        int count = 0;

        while (count < loc) {
            temp = temp->next;
            count++;
            if (temp == head && loc > 0) {
                cout << "Posicion fuera de rango" << endl;
                return;
            }
        }

        new_node->next = temp->next;
        temp->next = new_node;

        if (temp == tail) {
            tail = new_node;
        }

        cout << "Nodo insertado correctamente despues de la posicion " << loc << endl;
    }

    void begin_delete() {
        clearScreen();
        cout << "=== ELIMINAR DEL INICIO ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
            cout << "Unico nodo eliminado" << endl;
        } else {
            Node* temp = head;
            head = head->next;
            tail->next = head;
            delete temp;
            cout << "Nodo eliminado del inicio correctamente" << endl;
        }
    }

    void last_delete() {
        clearScreen();
        cout << "=== ELIMINAR DEL FINAL ===" << endl;
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
        } else if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
            cout << "Unico nodo eliminado" << endl;
        } else {
            Node* temp = head;
            while (temp->next != tail) {
                temp = temp->next;
            }
            delete tail;
            tail = temp;
            tail->next = head;
            cout << "Nodo eliminado del final correctamente" << endl;
        }
    }

    void random_delete() {
        clearScreen();
        cout << "=== ELIMINAR NODO EN POSICION ESPECIFICA ===" << endl;
        int loc;
        cout << "Ingrese la posicion del nodo que desea eliminar (0-based): ";
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
        Node* prev = nullptr;
        int count = 0;

        while (count < loc) {
            prev = temp;
            temp = temp->next;
            count++;
            if (temp == head) {
                cout << "Posicion fuera de rango" << endl;
                return;
            }
        }

        prev->next = temp->next;

        if (temp == tail) {
            tail = prev;
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

        int item;
        cout << "Ingrese el elemento que desea buscar: ";
        cin >> item;

        Node* temp = head;
        int i = 0;
        bool found = false;

        do {
            if (temp->data == item) {
                cout << "Elemento encontrado en la posicion " << i << endl;
                found = true;
                break;
            }
            temp = temp->next;
            i++;
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
            Node* temp = head;
            cout << "Elementos de la lista: ";
            do {
                cout << temp->data << " ";
                temp = temp->next;
            } while (temp != head);
            cout << endl;
            cout << "Head: " << head->data << ", Tail: " << tail->data << ", Tail->next: " << tail->next->data << endl;
            cout << "(La lista es circular - el ultimo nodo apunta al primero)" << endl;
        }
    }

    void menu() {
        int choice;
        do {
            clearScreen();
            cout << "\n\n********* MENU LISTA CIRCULAR *********" << endl;
            cout << "\nElija una opcion del siguiente menu:" << endl;
            cout << "1. Insertar al inicio" << endl;
            cout << "2. Insertar al final" << endl;
            cout << "3. Insertar en posicion especifica" << endl;
            cout << "4. Eliminar del inicio" << endl;
            cout << "5. Eliminar del final" << endl;
            cout << "6. Eliminar nodo en posicion especifica" << endl;
            cout << "7. Buscar elemento" << endl;
            cout << "8. Mostrar lista" << endl;
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
                case 9: cout << "Saliendo del programa..." << endl; break;
                default: cout << "Por favor ingrese una opcion valida..." << endl;
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
