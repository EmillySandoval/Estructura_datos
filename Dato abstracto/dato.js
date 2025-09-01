class Persona {
    constructor(nombre, apellido1, apellido2) {
        this.nombre = nombre;
        this.apellido1 = apellido1;
        this.apellido2 = apellido2;
    }

    nombreCompleto() {
        return `${this.nombre} ${this.apellido1} ${this.apellido2}`;
    }
}

const personas = [
    new Persona("Emily", "sandoval", "Ramírez"),
    new Persona("Carlos", "Ramírez", "Torres")
];

personas.forEach(persona => {
    console.log(persona.nombreCompleto());
});
