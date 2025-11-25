// cola-simple.js
const readline = require('readline');

const MAXSIZE = 5;
let queue = [];
let front = -1;
let rear = -1;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function insertar() {
    if (rear === MAXSIZE - 1) {
        console.log("\nDESBORDAMIENTO (OVERFLOW)\n");
        mostrarMenu();
        return;
    }

    rl.question("\nIngrese el elemento: ", (input) => {
        const elemento = parseInt(input);
        
        if (isNaN(elemento)) {
            console.log("Error: Debe ingresar un numero valido.");
            mostrarMenu();
            return;
        }

        if (front === -1 && rear === -1) {
            front = rear = 0;
        } else {
            rear++;
        }

        queue[rear] = elemento;
        console.log("\nElemento insertado correctamente.\n");
        mostrarMenu();
    });
}

function eliminar() {
    if (front === -1 || front > rear) {
        console.log("\nSUBDESBORDAMIENTO (UNDERFLOW)\n");
        mostrarMenu();
        return;
    }

    const elemento = queue[front];
    if (front === rear) {
        front = rear = -1;
    } else {
        front++;
    }

    console.log("\nElemento eliminado: " + elemento + "\n");
    mostrarMenu();
}

function mostrar() {
    if (rear === -1 || front === -1 || front > rear) {
        console.log("\nLa cola esta vacia.\n");
    } else {
        console.log("\nElementos en la cola:");
        for (let i = front; i <= rear; i++) {
            console.log(queue[i]);
        }
    }
    mostrarMenu();
}

function mostrarMenu() {
    console.log("\n========== MENU PRINCIPAL ==========");
    console.log("1. Insertar elemento");
    console.log("2. Eliminar elemento");
    console.log("3. Mostrar cola");
    console.log("4. Salir");
    rl.question("Ingrese su opcion: ", procesarOpcion);
}

function procesarOpcion(input) {
    const opcion = parseInt(input);
    
    if (isNaN(opcion)) {
        console.log("Error: Opcion invalida. Debe ingresar un numero.");
        mostrarMenu();
        return;
    }

    switch (opcion) {
        case 1:
            insertar();
            break;
        case 2:
            eliminar();
            break;
        case 3:
            mostrar();
            break;
        case 4:
            console.log("Saliendo del programa...");
            rl.close();
            break;
        default:
            console.log("Opcion invalida. Intente nuevamente.");
            mostrarMenu();
            break;
    }
}


mostrarMenu();