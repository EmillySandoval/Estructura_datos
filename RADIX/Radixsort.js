function countingSort(arr, exp) {
    const n = arr.length;
    const output = new Array(n);
    const count = new Array(10).fill(0);
    
    // Contar la frecuencia de cada dígito
    for (let i = 0; i < n; i++) {
        const index = Math.floor(arr[i] / exp) % 10;
        count[index]++;
    }
    
    // Cambiar count[i] para que contenga la posición actual
    for (let i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    // Construir el array de salida
    for (let i = n - 1; i >= 0; i--) {
        const index = Math.floor(arr[i] / exp) % 10;
        output[count[index] - 1] = arr[i];
        count[index]--;
    }
    
    // Copiar el array de salida al array original
    for (let i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

function radixSort(arr) {
    // Encontrar el número máximo para saber el número de dígitos
    const maxNum = Math.max(...arr);
    
    // Aplicar counting sort para cada dígito
    for (let exp = 1; Math.floor(maxNum / exp) > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

// Ejemplo de uso
const arr = [170, 45, 75, 90, 2, 802, 24, 66];
console.log("Array original:", arr);
radixSort(arr);
console.log("Array ordenado:", arr);