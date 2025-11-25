class Pila {
    constructor() {
        this.TAMANIO_MAXIMO = 100;
        this.pila = new Array(this.TAMANIO_MAXIMO);
        this.tope = -1;
    }
    
    apilar(numero) {
        if (this.tope === this.TAMANIO_MAXIMO - 1) {
            console.log("Desbordamiento de Pila");
            return;
        }
        this.tope++;
        this.pila[this.tope] = numero;
    }
    
    desapilar() {
        if (this.tope === -1) {
            console.log("Subdesbordamiento de Pila");
            return -1;
        }
        const elemento = this.pila[this.tope];
        this.tope--;
        return elemento;
    }
    
    mirar() {
        if (this.tope === -1) {
            console.log("La pila está vacía");
            return -1;
        }
        return this.pila[this.tope];
    }
    
    estaVacia() {
        return this.tope === -1;
    }
    
    estaLlena() {
        return this.tope === this.TAMANIO_MAXIMO - 1;
    }
}

// Ejemplo de uso
const p = new Pila();
p.apilar(10);
p.apilar(20);
p.apilar(30);

console.log("Elemento Superior:", p.mirar());
console.log("Extrae elemento:", p.desapilar());
console.log("Elemento Superior:", p.mirar());