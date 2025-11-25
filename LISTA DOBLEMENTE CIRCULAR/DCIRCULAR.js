const readline = require('readline');

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class CircularLinkedList {
    constructor() {
        this.head = null;
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    }

    clearScreen() {
        console.log('\n'.repeat(50));
    }

    question(prompt) {
        return new Promise((resolve) => {
            this.rl.question(prompt, resolve);
        });
    }

    async insertAtBeginning() {
        this.clearScreen();
        console.log("=== INSERTAR AL INICIO ===");
        
        const input = await this.question("Ingrese el valor del nodo: ");
        const value = parseInt(input);
        
        if (isNaN(value)) {
            console.log("Error: Ingrese un numero valido");
            return;
        }

        const newNode = new Node(value);

        if (!this.head) {
            this.head = newNode;
            this.head.next = this.head;
            this.head.prev = this.head;
            console.log("Nodo insertado (lista vacia)");
        } else {
            const last = this.head.prev;
            
            newNode.next = this.head;
            newNode.prev = last;
            last.next = newNode;
            this.head.prev = newNode;
            this.head = newNode;
            
            console.log("Nodo insertado al inicio");
        }
    }

    async insertAtEnd() {
        this.clearScreen();
        console.log("=== INSERTAR AL FINAL ===");
        
        const input = await this.question("Ingrese el valor del nodo: ");
        const value = parseInt(input);
        
        if (isNaN(value)) {
            console.log("Error: Ingrese un numero valido");
            return;
        }

        const newNode = new Node(value);

        if (!this.head) {
            this.head = newNode;
            this.head.next = this.head;
            this.head.prev = this.head;
            console.log("Nodo insertado (lista vacia)");
        } else {
            const last = this.head.prev;
            
            newNode.next = this.head;
            newNode.prev = last;
            last.next = newNode;
            this.head.prev = newNode;
            
            console.log("Nodo insertado al final");
        }
    }

    async insertAtPosition() {
        this.clearScreen();
        console.log("=== INSERTAR EN POSICION ===");
        
        const valueInput = await this.question("Ingrese el valor del nodo: ");
        const value = parseInt(valueInput);
        
        if (isNaN(value)) {
            console.log("Error: Valor no valido");
            return;
        }

        const posInput = await this.question("Ingrese la posicion: ");
        const position = parseInt(posInput);
        
        if (isNaN(position) || position < 0) {
            console.log("Error: Posicion no valida");
            return;
        }

        const newNode = new Node(value);

        if (!this.head) {
            if (position === 0) {
                this.head = newNode;
                this.head.next = this.head;
                this.head.prev = this.head;
                console.log("Nodo insertado en posicion 0");
            } else {
                console.log("Error: La lista esta vacia, solo puede insertar en posicion 0");
            }
            return;
        }

        if (position === 0) {
            const last = this.head.prev;
            newNode.next = this.head;
            newNode.prev = last;
            last.next = newNode;
            this.head.prev = newNode;
            this.head = newNode;
            console.log("Nodo insertado en posicion 0");
            return;
        }

        let current = this.head;
        let count = 0;

        do {
            if (count === position - 1) {
                newNode.next = current.next;
                newNode.prev = current;
                current.next.prev = newNode;
                current.next = newNode;
                console.log("Nodo insertado en posicion " + position);
                return;
            }
            current = current.next;
            count++;
        } while (current !== this.head);

        console.log("Error: Posicion fuera de rango");
    }

    deleteFromBeginning() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL INICIO ===");
        
        if (!this.head) {
            console.log("La lista esta vacia");
            return;
        }

        if (this.head.next === this.head) {
            this.head = null;
            console.log("Unico nodo eliminado");
        } else {
            const last = this.head.prev;
            this.head = this.head.next;
            this.head.prev = last;
            last.next = this.head;
            console.log("Nodo eliminado del inicio");
        }
    }

    deleteFromEnd() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL FINAL ===");
        
        if (!this.head) {
            console.log("La lista esta vacia");
            return;
        }

        if (this.head.next === this.head) {
            this.head = null;
            console.log("Unico nodo eliminado");
        } else {
            const last = this.head.prev;
            const newLast = last.prev;
            
            newLast.next = this.head;
            this.head.prev = newLast;
            console.log("Nodo eliminado del final");
        }
    }

    async deleteFromPosition() {
        this.clearScreen();
        console.log("=== ELIMINAR DE POSICION ===");
        
        const posInput = await this.question("Ingrese la posicion a eliminar: ");
        const position = parseInt(posInput);
        
        if (isNaN(position) || position < 0) {
            console.log("Error: Posicion no valida");
            return;
        }

        if (!this.head) {
            console.log("La lista esta vacia");
            return;
        }

        if (position === 0) {
            this.deleteFromBeginning();
            return;
        }

        let current = this.head;
        let count = 0;

        do {
            if (count === position) {
                current.prev.next = current.next;
                current.next.prev = current.prev;
                
                if (current === this.head) {
                    this.head = current.next;
                }
                
                console.log("Nodo eliminado de posicion " + position);
                return;
            }
            current = current.next;
            count++;
        } while (current !== this.head);

        console.log("Error: Posicion fuera de rango");
    }

    async search() {
        this.clearScreen();
        console.log("=== BUSCAR ELEMENTO ===");
        
        if (!this.head) {
            console.log("La lista esta vacia");
            return;
        }

        const input = await this.question("Ingrese el elemento a buscar: ");
        const value = parseInt(input);
        
        if (isNaN(value)) {
            console.log("Error: Ingrese un numero valido");
            return;
        }

        let current = this.head;
        let position = 0;
        let found = false;

        do {
            if (current.data === value) {
                console.log("Elemento " + value + " encontrado en posicion " + position);
                found = true;
                break;
            }
            current = current.next;
            position++;
        } while (current !== this.head);

        if (!found) {
            console.log("Elemento " + value + " no encontrado");
        }
    }

    display() {
        this.clearScreen();
        console.log("=== LISTA CIRCULAR DOBLEMENTE ENLAZADA ===");
        
        if (!this.head) {
            console.log("La lista esta vacia");
            return;
        }

        console.log("Recorrido hacia adelante:");
        let current = this.head;
        let forward = "";
        
        do {
            forward += current.data + " -> ";
            current = current.next;
        } while (current !== this.head);
        
        console.log(forward + "(vuelve al inicio)");

        console.log("\nRecorrido hacia atras:");
        current = this.head.prev;
        let backward = "";
        const start = current;
        
        do {
            backward += current.data + " -> ";
            current = current.prev;
        } while (current !== start);
        
        console.log(backward + "(vuelve al final)");

        console.log("\nHead: " + this.head.data);
        console.log("Head.prev: " + this.head.prev.data);
        console.log("Head.next: " + this.head.next.data);
    }

    async showMenu() {
        let option;
        
        do {
            this.clearScreen();
            console.log("====================================");
            console.log("  LISTA DOBLEMENTE ENLAZADA CIRCULAR");
            console.log("====================================");
            console.log("1. Insertar al inicio");
            console.log("2. Insertar al final");
            console.log("3. Insertar en posicion");
            console.log("4. Eliminar del inicio");
            console.log("5. Eliminar del final");
            console.log("6. Eliminar de posicion");
            console.log("7. Buscar elemento");
            console.log("8. Mostrar lista");
            console.log("9. Salir");
            console.log("====================================");

            option = await this.question("\nSeleccione una opcion: ");

            switch(option) {
                case '1':
                    await this.insertAtBeginning();
                    break;
                case '2':
                    await this.insertAtEnd();
                    break;
                case '3':
                    await this.insertAtPosition();
                    break;
                case '4':
                    this.deleteFromBeginning();
                    break;
                case '5':
                    this.deleteFromEnd();
                    break;
                case '6':
                    await this.deleteFromPosition();
                    break;
                case '7':
                    await this.search();
                    break;
                case '8':
                    this.display();
                    break;
                case '9':
                    console.log("Saliendo del programa...");
                    break;
                default:
                    console.log("Opcion invalida");
            }

            if (option !== '9') {
                console.log("\nPresione Enter para continuar...");
                await this.question("");
            }

        } while (option !== '9');

        this.rl.close();
    }
}


function main() {
    const list = new CircularLinkedList();
    list.showMenu();
}

main();