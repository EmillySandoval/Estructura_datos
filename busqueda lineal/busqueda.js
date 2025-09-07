function busquedaLineal(arr, objetivo) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === objetivo)
            return i;
    }
    return -1;
}


const arreglo = [3, 8, 1, 5, 9];
console.log(busquedaLineal(arreglo, 5));  