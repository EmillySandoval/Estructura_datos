function ordenarCubetas(arreglo) {
    const tamaño = arreglo.length;
    const cubetas = Array.from({ length: tamaño }, () => []);

    for (const numero of arreglo) {
        const indice = Math.floor(numero * tamaño);
        cubetas[indice].push(numero);
    }

 
    for (const cubeta of cubetas) {
        cubeta.sort((a, b) => a - b);
    }


    const arregloOrdenado = [];
    for (const cubeta of cubetas) {
        arregloOrdenado.push(...cubeta);
    }

    return arregloOrdenado;
}


const datos = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47];
console.log(ordenarCubetas(datos));