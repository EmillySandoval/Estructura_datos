    if (lista.length <= 1) {
        console.log("  ".repeat(nivel) + "Retorno:", lista);
        return lista;
    }
    let pivote = lista[0];
    let menores = lista.slice(1).filter(x => x <= pivote);
    let mayores = lista.slice(1).filter(x => x > pivote);
    console.log("  ".repeat(nivel) + `Pivote: ${pivote}, Menores: ${menores}, Mayores: ${mayores}`);
    return [...quickSort(menores, nivel + 1), pivote, ...quickSort(mayores, nivel + 1)];
}

let numeros = [8, 3, 1, 7, 0, 10, 2];
console.log("Original:", numeros);
let ordenado = quickSort(numeros);
console.log("Ordenado:", ordenado);