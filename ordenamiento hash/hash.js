function funcionHash(valor, minimo, tamañoIntervalo) {
    return Math.floor((valor - minimo) / tamañoIntervalo);
}

function ordenarPorInsercion(lista) {
    for (let i = 1; i < lista.length; i++) {
        let valorActual = lista[i];
        let j = i - 1;
        while (j >= 0 && lista[j] > valorActual) {
            lista[j + 1] = lista[j];
            j--;
        }
        lista[j + 1] = valorActual;
    }
}

function ordenamientoHash(listaNumeros) {
    let minimo = Math.min(...listaNumeros);
    let maximo = Math.max(...listaNumeros);
    let cantidadCubetas = listaNumeros.length;
    let tamañoIntervalo = Math.floor((maximo - minimo) / cantidadCubetas) + 1;

    let cubetas = Array.from({ length: cantidadCubetas }, () => []);

    for (let numero of listaNumeros) {
        let indice = funcionHash(numero, minimo, tamañoIntervalo);
        cubetas[indice].push(numero);
    }

    let listaOrdenada = [];
    for (let cubeta of cubetas) {
        ordenarPorInsercion(cubeta);
        listaOrdenada = listaOrdenada.concat(cubeta);
    }

    return listaOrdenada;
}

let numeros = [36, 34, 43, 11, 15, 20, 28];
let resultado = ordenamientoHash(numeros);
console.log("Lista ordenada:", resultado);