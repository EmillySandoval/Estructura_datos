function insertarEnIndice(lista, valor, indice) {
    lista.splice(indice, 0, valor);
    return lista;
}


let miLista = [1, 2, 3, 5];
console.log(insertarEnIndice(miLista, 4, 3)); 