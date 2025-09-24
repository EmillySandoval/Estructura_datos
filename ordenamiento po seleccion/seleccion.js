function ordenamientoPorSeleccion(lista) {
    for (let i = 0; i < lista.length; i++) {
        let indiceMinimo = i;
        for (let j = i + 1; j < lista.length; j++) {
            if (lista[j] < lista[indiceMinimo]) {
                indiceMinimo = j;
            }
        }
        [lista[i], lista[indiceMinimo]] = [lista[indiceMinimo], lista[i]];
    }
}

function mostrarLista(lista) {
    console.log(lista.join(", "));
}


let numeros = [64, 25, 12, 22, 11];

console.log("Lista original:");
mostrarLista(numeros);

ordenamientoPorSeleccion(numeros);

console.log("Lista ordenada:");
mostrarLista(numeros);