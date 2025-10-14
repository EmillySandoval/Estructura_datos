function mergeSort(arreglo) {
    if (arreglo.length > 1) {
        const medio = Math.floor(arreglo.length / 2);
        const izquierda = arreglo.slice(0, medio);
        const derecha = arreglo.slice(medio);

        mergeSort(izquierda);
        mergeSort(derecha);

        let i = 0, j = 0, k = 0;

        while (i < izquierda.length && j < derecha.length) {
            if (izquierda[i] < derecha[j]) {
                arreglo[k++] = izquierda[i++];
            } else {
                arreglo[k++] = derecha[j++];
            }
        }

        while (i < izquierda.length) {
            arreglo[k++] = izquierda[i++];
        }

        while (j < derecha.length) {
            arreglo[k++] = derecha[j++];
        }
    }
}


let arreglo = [38, 27, 43, 3, 9, 82, 10];
mergeSort(arreglo);
console.log("Arreglo ordenado:", arreglo);