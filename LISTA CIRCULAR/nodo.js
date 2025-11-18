const readline = require('readline');

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class CircularLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
    }

    clearScreen() {
        console.clear();
    }

    async beginset() {
        this.clearScreen();
        console.log("=== INSERTAR AL INICIO ===");
        const item = await this.question("Ingrese el valor del nodo: ");
        
        const new_node = new Node(parseInt(item));
        
        if (this.head === null) {
            this.head = new_node;
            this.tail = new_node;
            new_node.next = this.head;
            console.log("Primer nodo insertado al inicio (lista circular creada)");
        } else {
            new_node.next = this.head;
            this.head = new_node;
            this.tail.next = this.head;
            console.log("Nodo insertado al inicio correctamente");
        }
    }

    async lastinsert() {
        this.clearScreen();
        console.log("=== INSERTAR AL FINAL ===");
        const item = await this.question("Ingrese el valor del nodo: ");
        
        const new_node = new Node(parseInt(item));
        
        if (this.head === null) {
            this.head = new_node;
            this.tail = new_node;
            new_node.next = this.head;
            console.log("Primer nodo insertado al final (lista circular creada)");
        } else {
            this.tail.next = new_node;
            this.tail = new_node;
            new_node.next = this.head;
            console.log("Nodo insertado al final correctamente");
        }
    }

    async randominsert() {
        this.clearScreen();
        console.log("=== INSERTAR EN POSICION ESPECIFICA ===");
        const item = await this.question("Ingrese el valor del elemento: ");
        const loc_input = await this.question("Ingrese la posicion después de la cual desea insertar: ");
        
        const position = parseInt(loc_input);
        const value = parseInt(item);
        
        if (isNaN(position) || position < 0) {
            console.log("Posición no válida");
            return;
        }
        
        if (this.head === null) {
            console.log("La lista está vacía. Insertando como primer nodo...");
            const new_node = new Node(value);
            this.head = new_node;
            this.tail = new_node;
            new_node.next = this.head;
            return;
        }
        
        const new_node = new Node(value);
        let temp = this.head;
        let count = 0;
        
        if (position === 0) {
            new_node.next = this.head.next;
            this.head.next = new_node;
            if (this.head === this.tail) {
                this.tail = new_node;
            }
            console.log("Nodo insertado después de la posición 0");
            return;
        }
        
        while (count < position) {
            temp = temp.next;
            count++;
            if (temp === this.head) {
                console.log("Posición fuera de rango");
                return;
            }
        }
        
        new_node.next = temp.next;
        temp.next = new_node;
        
        if (temp === this.tail) {
            this.tail = new_node;
        }
        
        console.log(`Nodo insertado correctamente después de la posición ${position}`);
    }

    begin_delete() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL INICIO ===");
        if (this.head === null) {
            console.log("La lista está vacía");
            return;
        }
        
        if (this.head === this.tail) {
            this.head = null;
            this.tail = null;
            console.log("Único nodo eliminado");
        } else {
            this.head = this.head.next;
            this.tail.next = this.head;
            console.log("Nodo eliminado del inicio correctamente");
        }
    }

    last_delete() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL FINAL ===");
        if (this.head === null) {
            console.log("La lista está vacía");
            return;
        }
        
        if (this.head === this.tail) {
            this.head = null;
            this.tail = null;
            console.log("Único nodo eliminado");
        } else {
            let temp = this.head;
            while (temp.next !== this.tail) {
                temp = temp.next;
            }
            temp.next = this.head;
            this.tail = temp;
            console.log("Nodo eliminado del final correctamente");
        }
    }

    async random_delete() {
        this.clearScreen();
        console.log("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
        const loc_input = await this.question("Ingrese la posición del nodo que desea eliminar (0-based): ");
        
        const position = parseInt(loc_input);
        
        if (this.head === null) {
            console.log("La lista está vacía");
            return;
        }
        
        if (isNaN(position) || position < 0) {
            console.log("Posición no válida");
            return;
        }
        
        if (position === 0) {
            this.begin_delete();
            return;
        }
        
        let temp = this.head;
        let prev = null;
        let count = 0;
        
        do {
            prev = temp;
            temp = temp.next;
            count++;
            
            if (count === position) {
                prev.next = temp.next;
                
                if (temp === this.tail) {
                    this.tail = prev;
                }
                
                console.log(`Nodo eliminado de la posición ${position}`);
                return;
            }
        } while (temp !== this.head && count <= position);
        
        console.log("Posición fuera de rango");
    }

    async search() {
        this.clearScreen();
        console.log("=== BUSCAR ELEMENTO ===");
        
        if (this.head === null) {
            console.log("Lista vacía");
            return;
        }
        
        const item = await this.question("Ingrese el elemento que desea buscar: ");
        const searchValue = parseInt(item);
        
        if (isNaN(searchValue)) {
            console.log("Ingrese un número válido");
            return;
        }
        
        let temp = this.head;
        let i = 0;
        let found = false;
        
        do {
            if (temp.data === searchValue) {
                console.log(`Elemento encontrado en la posición ${i}`);
                found = true;
                break;
            }
            temp = temp.next;
            i++;
        } while (temp !== this.head);
        
        if (!found) {
            console.log("Elemento no encontrado");
        }
    }

    display() {
        this.clearScreen();
        console.log("=== MOSTRAR LISTA CIRCULAR ===");
        
        if (this.head === null) {
            console.log("La lista está vacía");
        } else {
            let temp = this.head;
            let elements = [];
            
            do {
                elements.push(temp.data);
                temp = temp.next;
            } while (temp !== this.head);
            
            console.log("Elementos de la lista: " + elements.join(" → "));
            console.log(`Head: ${this.head.data}, Tail: ${this.tail.data}, Tail->next: ${this.tail.next.data}`);
            console.log("(La lista es circular - el último nodo apunta al primero)");
        }
    }

    question(prompt) {
        return new Promise((resolve) => {
            this.rl.question(prompt, resolve);
        });
    }

    async menu() {
        let choice;
        do {
            this.clearScreen();
            console.log("\n\n********* MENU LISTA CIRCULAR *********");
            console.log("\n1. Insertar al inicio");
            console.log("2. Insertar al final");
            console.log("3. Insertar en posición específica");
            console.log("4. Eliminar del inicio");
            console.log("5. Eliminar del final");
            console.log("6. Eliminar nodo en posición específica");
            console.log("7. Buscar elemento");
            console.log("8. Mostrar lista");
            console.log("9. Salir");
            
            choice = await this.question("\nIngrese su elección: ");
            
            switch (choice) {
                case '1': await this.beginset(); break;
                case '2': await this.lastinsert(); break;
                case '3': await this.randominsert(); break;
                case '4': this.begin_delete(); break;
                case '5': this.last_delete(); break;
                case '6': await this.random_delete(); break;
                case '7': await this.search(); break;
                case '8': this.display(); break;
                case '9': console.log("Saliendo del programa..."); break;
                default: console.log("Por favor ingrese una opción válida..."); break;
            }
            
            if (choice !== '9') {
                console.log("\nPresione Enter para continuar...");
                await this.question("");
            }
        } while (choice !== '9');
        
        this.rl.close();
    }
}

const lista = new CircularLinkedList();
lista.menu();
