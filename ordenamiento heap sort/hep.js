function imprimirLista(lista) {
    console.log(lista.join(" "));
}

function construirMonticulo(lista, tamaño, raiz) {
    let mayor = raiz;
    let izquierdo = 2 * raiz + 1;
    let derecho = 2 * raiz + 2;

    if (izquierdo < tamaño && lista[izquierdo] > lista[mayor])
        mayor = izquierdo;

    if (derecho < tamaño && lista[derecho] > lista[mayor])
        mayor = derecho;

    if (mayor !== raiz) {
        [lista[raiz], lista[mayor]] = [lista[mayor], lista[raiz]];
        construirMonticulo(lista, tamaño, mayor);
    }
}

function ordenarPorHeap(lista) {
    let tamaño = lista.length;

    console.log("Construyendo montículo máximo...");
    for (let i = Math.floor(tamaño / 2) - 1; i >= 0; i--) {
        construirMonticulo(lista, tamaño, i);
        imprimirLista(lista);
    }

    console.log("Extrayendo elementos del montículo...");
    for (let i = tamaño - 1; i > 0; i--) {
        [lista[0], lista[i]] = [lista[i], lista[0]];
        construirMonticulo(lista, i, 0);
        imprimirLista(lista);
    }
}


let listaNumeros = [12, 4, 7, 9, 1, 15, 3];
console.log("Lista original:");
imprimirLista(listaNumeros);

ordenarPorHeap(listaNumeros);

console.log("Lista ordenada:");
imprimirLista(listaNumeros);