const readline = require('readline');

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
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
        
        const newNode = new Node(parseInt(item));
        newNode.next = this.head;
        this.head = newNode;
        console.log("Nodo insertado al inicio correctamente");
    }

    async lastinsert() {
        this.clearScreen();
        console.log("=== INSERTAR AL FINAL ===");
        const item = await this.question("Ingrese el valor del nodo: ");
        
        const newNode = new Node(parseInt(item));
        
        if (this.head === null) {
            this.head = newNode;
            console.log("Nodo insertado al final (lista estaba vacia)");
        } else {
            let temp = this.head;
            while (temp.next !== null) {
                temp = temp.next;
            }
            temp.next = newNode;
            console.log("Nodo insertado al final correctamente");
        }
    }

    async randominsert() {
        this.clearScreen();
        console.log("=== INSERTAR EN POSICION ESPECIFICA ===");
        const item = await this.question("Ingrese el valor del elemento: ");
        const loc = await this.question("Ingrese la posicion despues de la cual desea insertar: ");
        
        const newNode = new Node(parseInt(item));
        
        if (this.head === null) {
            console.log("La lista esta vacia. Insertando al inicio...");
            this.head = newNode;
        } else {
            let temp = this.head;
            for (let i = 0; i < parseInt(loc); i++) {
                if (temp === null) {
                    console.log("No se puede insertar en esa posicion");
                    return;
                }
                temp = temp.next;
            }
            
            if (temp === null) {
                console.log("No se puede insertar en esa posicion");
                return;
            }
            
            newNode.next = temp.next;
            temp.next = newNode;
            console.log(`Nodo insertado correctamente en la posicion ${parseInt(loc) + 1}`);
        }
    }

    async beginDelete() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL INICIO ===");
        if (this.head === null) {
            console.log("La lista esta vacia");
        } else {
            this.head = this.head.next;
            console.log("Nodo eliminado del inicio correctamente");
        }
    }

    async lastDelete() {
        this.clearScreen();
        console.log("=== ELIMINAR DEL FINAL ===");
        if (this.head === null) {
            console.log("La lista esta vacia");
        } else if (this.head.next === null) {
            this.head = null;
            console.log("Unico nodo eliminado");
        } else {
            let temp = this.head;
            let prev = null;
            while (temp.next !== null) {
                prev = temp;
                temp = temp.next;
            }
            prev.next = null;
            console.log("Nodo eliminado del final correctamente");
        }
    }

    async randomDelete() {
        this.clearScreen();
        console.log("=== ELIMINAR NODO EN POSICION ESPECIFICA ===");
        const loc = await this.question("Ingrese la posicion del nodo que desea eliminar: ");
        
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        
        if (parseInt(loc) === 0) {
            this.head = this.head.next;
            console.log(`Nodo eliminado de la posicion ${loc}`);
            return;
        }
        
        let temp = this.head;
        let prev = null;
        for (let i = 0; i < parseInt(loc); i++) {
            if (temp === null) {
                console.log("No se puede eliminar - posicion fuera de rango");
                return;
            }
            prev = temp;
            temp = temp.next;
        }
        
        if (temp === null) {
            console.log("No se puede eliminar - posicion fuera de rango");
            return;
        }
        
        prev.next = temp.next;
        console.log(`Nodo eliminado de la posicion ${loc}`);
    }

    async search() {
        this.clearScreen();
        console.log("=== BUSCAR ELEMENTO ===");
        if (this.head === null) {
            console.log("Lista vacia");
            return;
        }
        
        const item = await this.question("Ingrese el elemento que desea buscar: ");
        
        let temp = this.head;
        let i = 0;
        let found = false;
        
        while (temp !== null) {
            if (temp.data === parseInt(item)) {
                console.log(`Elemento encontrado en la posicion ${i + 1}`);
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

    async display() {
        this.clearScreen();
        console.log("=== MOSTRAR LISTA ===");
        if (this.head === null) {
            console.log("La lista esta vacia");
        } else {
            let temp = this.head;
            process.stdout.write("Elementos de la lista: ");
            while (temp !== null) {
                process.stdout.write(temp.data + " ");
                temp = temp.next;
            }
            console.log();
        }
    }

    question(prompt) {
        return new Promise((resolve) => {
            this.rl.question(prompt, resolve);
        });
    }

    async waitForEnter() {
        await this.question("\n\nPresione Enter para continuar...");
    }

    async menu() {
        while (true) {
            this.clearScreen();
            console.log("\n\n**Menu Principal");
            console.log("\nElija una opcion del siguiente menu:");
            console.log("1. Insertar al inicio");
            console.log("2. Insertar al final");
            console.log("3. Insertar en posicion aleatoria");
            console.log("4. Eliminar del inicio");
            console.log("5. Eliminar del final");
            console.log("6. Eliminar nodo despues de una posicion");
            console.log("7. Buscar elemento");
            console.log("8. Mostrar lista");
            console.log("9. Salir");
            
            const choice = await this.question("\nIngrese su eleccion: ");
            
            switch (parseInt(choice)) {
                case 1:
                    await this.beginset();
                    break;
                case 2:
                    await this.lastinsert();
                    break;
                case 3:
                    await this.randominsert();
                    break;
                case 4:
                    await this.beginDelete();
                    break;
                case 5:
                    await this.lastDelete();
                    break;
                case 6:
                    await this.randomDelete();
                    break;
                case 7:
                    await this.search();
                    break;
                case 8:
                    await this.display();
                    break;
                case 9:
                    this.clearScreen();
                    console.log("Saliendo del programa...");
                    this.rl.close();
                    return;
                default:
                    this.clearScreen();
                    console.log("Por favor ingrese una opcion valida...");
                    break;
            }
            
            if (parseInt(choice) !== 9) {
                await this.waitForEnter();
            }
        }
    }
}

// Ejecutar el programa
const lista = new LinkedList();
lista.menu().catch(console.error);