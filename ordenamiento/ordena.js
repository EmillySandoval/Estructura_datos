function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

let arr = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100) + 1);
console.log("Antes de ordenar:", arr);

insertionSort(arr);
console.log("Después de ordenar:", arr);