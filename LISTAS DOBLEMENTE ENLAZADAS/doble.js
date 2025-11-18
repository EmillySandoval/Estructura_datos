const readline = require('readline');

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class LinkedList {
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

    question(prompt) {
        return new Promise((resolve) => {
            this.rl.question(prompt, resolve);
        });
    }

    async waitForEnter() {
        return new Promise((resolve) => {
            this.rl.question("\n\nPresione Enter para continuar...", resolve);
        });
    }

    async beginset() {
        this.clearScreen();
        console.log("=== INSERTAR AL INICIO ===");
        const item = parseInt(await this.question("Ingrese el valor del nodo: "));
        if (isNaN(item)) {
            console.log("Entrada inválida. Debe ser un número.");
            return;
        }

        const new_node = new Node(item);

        if (this.head === null) {
            this.head = new_node;
            this.tail = new_node;
            console.log("Nodo insertado al inicio (lista estaba vacía)");
        } else {
            new_node.next = this.head;
            this.head.prev = new_node;
            this.head = new_node;
            console.log("Nodo insertado al inicio correctamente");
        }
    }

    async lastinsert() {
        this.clearScreen();
        console.log("=== INSERTAR AL FINAL ===");
        const item = parseInt(await this.question("Ingrese el valor del nodo: "));
        if (isNaN(item)) {
            console.log("Entrada inválida. Debe ser un número.");
            return;
        }

        const new_node = new Node(item);

        if (this.head === null) {
            this.head = new_node;
            this.tail = new_node;
            console.log("Nodo insertado al final (lista estaba vacía)");
        } else {
            new_node.prev = this.tail;
            this.tail.next = new_node;
            this.tail = new_node;
            console.log("Nodo insertado al final correctamente");
        }
    }

    async randominsert() {
        this.clearScreen();
        console.log("=== INSERTAR EN POSICIÓN ESPECÍFICA ===");
        const item = parseInt(await this.question("Ingrese el valor del elemento: "));
        const loc = parseInt(await this.question("Ingrese la posición después de la cual desea insertar: "));
        if (isNaN(item) || isNaN(loc)) {
            console.log("Entrada inválida. Debe ingresar números.");
            return;
        }

        const new_node = new Node(item);

        if (this.head === null) {
            console.log("La lista está vacía. Insertando al inicio...");
            this.head = new_node;
            this.tail = new_node;
        } else {
            let temp = this.head;
            for (let i = 0; i < loc; i++) {
                if (temp === null) {
                    console.log("No se puede insertar en esa posición");
                    return;
                }
                temp = temp.next;
            }

            if (temp === null) {
                console.log("No se puede insertar en esa posición");
                return;
            }

            new_node.next = temp.next;
            new_node.prev = temp;

            if (temp.next !== null) {
                temp.next.prev = new_node;
            } else {
                this.tail = new_node;
            }

            temp.next = new_node;
            console.log(`Nodo insertado correctamente en la posición ${loc + 1}`);
        }
    }

    begin_delete() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL INICIO ===");
        if (this.head === null) {
            console.log("La lista está vacía");
        } else {
            this.head = this.head.next;
            if (this.head !== null) {
                this.head.prev = null;
            } else {
                this.tail = null;
            }
            console.log("Nodo eliminado del inicio correctamente");
        }
    }

    last_delete() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL FINAL ===");
        if (this.head === null) {
            console.log("La lista está vacía");
        } else if (this.head.next === null) {
            this.head = null;
            this.tail = null;
            console.log("Único nodo eliminado");
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
            console.log("Nodo eliminado del final correctamente");
        }
    }

    async random_delete() {
        this.clearScreen();
        console.log("=== ELIMINAR NODO EN POSICIÓN ESPECÍFICA ===");
        const loc = parseInt(await this.question("Ingrese la posición del nodo que desea eliminar: "));
        if (isNaN(loc)) {
            console.log("Entrada inválida. Debe ser un número.");
            return;
        }

        if (this.head === null) {
            console.log("La lista está vacía");
            return;
        }

        if (loc === 0) {
            this.begin_delete();
            return;
        }

        let temp = this.head;
        for (let i = 0; i < loc; i++) {
            if (temp === null) {
                console.log("No se puede eliminar - posición fuera de rango");
                return;
            }
            temp = temp.next;
        }

        if (temp === null) {
            console.log("No se puede eliminar - posición fuera de rango");
            return;
        }

        if (temp.prev !== null) {
            temp.prev.next = temp.next;
        }

        if (temp.next !== null) {
            temp.next.prev = temp.prev;
        } else {
            this.tail = temp.prev;
        }

        console.log(`Nodo eliminado de la posición ${loc}`);
    }

    async search() {
        this.clearScreen();
        console.log("=== BUSCAR ELEMENTO ===");
        if (this.head === null) {
            console.log("Lista vacía");
            return;
        }

        const item = parseInt(await this.question("Ingrese el elemento que desea buscar: "));
        if (isNaN(item)) {
            console.log("Entrada inválida. Debe ser un número.");
            return;
        }

        let temp = this.head;
        let i = 0;
        let found = false;

        while (temp !== null) {
            if (temp.data === item) {
                console.log(`Elemento encontrado en la posición ${i + 1}`);
                found = true;
                break;
            }
            i++;
            temp = temp.next;
        }

        if (!found) {
            console.log("Elemento no encontrado");
        }
    }

    display() {
        this.clearScreen();
        console.log("=== MOSTRAR LISTA ===");
        if (this.head === null) {
            console.log("La lista está vacía");
        } else {
            process.stdout.write("Recorrido hacia adelante: ");
            let temp = this.head;
            while (temp !== null) {
                process.stdout.write(temp.data + " ");
                temp = temp.next;
            }
            console.log();

            process.stdout.write("Recorrido hacia atrás: ");
            temp = this.tail;
            while (temp !== null) {
                process.stdout.write(temp.data + " ");
                temp = temp.prev;
            }
            console.log();
        }
    }

    async menu() {
        let choice;
        do {
            this.clearScreen();
            console.log("\n\n** Menú Principal - LISTA DOBLEMENTE ENLAZADA **");
            console.log("\nElija una opción del siguiente menú:");
            console.log("1. Insertar al inicio");
            console.log("2. Insertar al final");
            console.log("3. Insertar en posición aleatoria");
            console.log("4. Eliminar del inicio");
            console.log("5. Eliminar del final");
            console.log("6. Eliminar nodo en posición específica");
            console.log("7. Buscar elemento");
            console.log("8. Mostrar lista (ambas direcciones)");
            console.log("9. Salir");

            choice = await this.question("\nIngrese su elección: ");

            switch (parseInt(choice)) {
                case 1: await this.beginset(); break;
                case 2: await this.lastinsert(); break;
                case 3: await this.randominsert(); break;
                case 4: this.begin_delete(); break;
                case 5: this.last_delete(); break;
                case 6: await this.random_delete(); break;
                case 7: await this.search(); break;
                case 8: this.display(); break;
                case 9:
                    this.clearScreen();
                    console.log("Saliendo del programa...");
                    break;
                default:
                    this.clearScreen();
                    console.log("Por favor ingrese una opción válida...");
            }

            if (parseInt(choice) !== 9) {
                await this.waitForEnter();
            }

        } while (parseInt(choice) !== 9);
        this.rl.close();
    }
}

const lista = new LinkedList();
lista.menu();