// --- Lógica de Algoritmos ---

/**
 * Función auxiliar para Insertion Sort.
 * La extraemos para poder reutilizarla en Bucket Sort.
 */
function standaloneInsertionSort(arr) {
    let n = arr.length;
    for (let i = 1; i < n; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    return arr;
}

const algorithms = {
    bubbleSort: {
        name: "Bubble Sort",
        sort: function(arr) {
            let n = arr.length;
            for (let i = 0; i < n - 1; i++) {
                for (let j = 0; j < n - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        let temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
            return arr;
        }
    },

    insertionSort: {
        name: "Insertion Sort",
        sort: function(arr) {
            return standaloneInsertionSort(arr);
        }
    },

    selectionSort: {
        name: "Selection Sort",
        sort: function(arr) {
            let n = arr.length;
            for (let i = 0; i < n - 1; i++) {
                let minIdx = i;
                for (let j = i + 1; j < n; j++) {
                    if (arr[j] < arr[minIdx]) {
                        minIdx = j;
                    }
                }
                let temp = arr[i];
                arr[i] = arr[minIdx];
                arr[minIdx] = temp;
            }
            return arr;
        }
    },

    // *** CORRECCIÓN DE RECURSIVIDAD AQUÍ ***
    quickSort: {
        name: "QuickSort",
        // Definimos la función de sort por separado
        sort: (function() {
            // "sortFunction" será la función recursiva
            function sortFunction(arr) {
                if (arr.length <= 1) return arr;
    
                let pivot = arr[Math.floor(arr.length / 2)];
                let left = [];
                let right = [];
                let equal = [];
    
                for (let i = 0; i < arr.length; i++) {
                    if (arr[i] < pivot) left.push(arr[i]);
                    else if (arr[i] > pivot) right.push(arr[i]);
                    else equal.push(arr[i]);
                }
                
                // Ahora se llama a sí misma de forma segura (sin 'this')
                return sortFunction(left).concat(equal, sortFunction(right));
            }
            return sortFunction; // Asignamos la función al objeto
        })() // IIFE (Immediately Invoked Function Expression)
    },

    // *** CORRECCIÓN DE RECURSIVIDAD AQUÍ ***
    mergeSort: {
        name: "MergeSort",
        // Hacemos lo mismo para mergeSort
        sort: (function() {
            function merge(left, right) {
                let result = [];
                let leftIndex = 0;
                let rightIndex = 0;
    
                while (leftIndex < left.length && rightIndex < right.length) {
                    if (left[leftIndex] < right[rightIndex]) {
                        result.push(left[leftIndex]);
                        leftIndex++;
                    } else {
                        result.push(right[rightIndex]);
                        rightIndex++;
                    }
                }
    
                return result.concat(left.slice(leftIndex), right.slice(rightIndex));
            }
            
            // "sortFunction" será la función recursiva
            function sortFunction(arr) {
                if (arr.length <= 1) return arr;
    
                let mid = Math.floor(arr.length / 2);
                let left = arr.slice(0, mid);
                let right = arr.slice(mid);
    
                // Se llama a sí misma de forma segura (sin 'this')
                return merge(sortFunction(left), sortFunction(right));
            }
            return sortFunction; // Asignamos la función
        })()
    },

    heapSort: {
        name: "HeapSort",
        sort: function(arr) {
            let n = arr.length;

            function heapify(arr, n, i) {
                let largest = i;
                let left = 2 * i + 1;
                let right = 2 * i + 2;

                if (left < n && arr[left] > arr[largest]) {
                    largest = left;
                }

                if (right < n && arr[right] > arr[largest]) {
                    largest = right;
                }

                if (largest !== i) {
                    let temp = arr[i];
                    arr[i] = arr[largest];
                    arr[largest] = temp;
                    heapify(arr, n, largest);
                }
            }

            for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
                heapify(arr, n, i);
            }

            for (let i = n - 1; i > 0; i--) {
                let temp = arr[0];
                arr[0] = arr[i];
                arr[i] = temp;
                heapify(arr, i, 0);
            }

            return arr;
        }
    },

    countingSort: {
        name: "hash Sort",
        sort: function(arr) {
            if (arr.length === 0) return arr;

            let max = Math.max(...arr);
            let min = Math.min(...arr);
            let range = max - min + 1;
            let count = new Array(range).fill(0);
            let output = new Array(arr.length);

            for (let i = 0; i < arr.length; i++) {
                count[arr[i] - min]++;
            }

            for (let i = 1; i < count.length; i++) {
                count[i] += count[i - 1];
            }

            for (let i = arr.length - 1; i >= 0; i--) {
                output[count[arr[i] - min] - 1] = arr[i];
                count[arr[i] - min]--;
            }

            for (let i = 0; i < arr.length; i++) {
                arr[i] = output[i];
            }

            return arr;
        }
    },

    bucketSort: {
        name: "Bucket Sort",
        sort: function(arr) {
            if (arr.length === 0) return arr;

            let min = Math.min(...arr);
            let max = Math.max(...arr);
            let bucketSize = 5;
            let bucketCount = Math.floor((max - min) / bucketSize) + 1;
            let buckets = new Array(bucketCount);

            for (let i = 0; i < buckets.length; i++) {
                buckets[i] = [];
            }

            for (let i = 0; i < arr.length; i++) {
                buckets[Math.floor((arr[i] - min) / bucketSize)].push(arr[i]);
            }

            arr.length = 0;
            for (let i = 0; i < buckets.length; i++) {
                standaloneInsertionSort(buckets[i]);
                for (let j = 0; j < buckets[i].length; j++) {
                    arr.push(buckets[i][j]);
                }
            }

            return arr;
        }
    },

    radixSort: {
        name: "Radix Sort",
        sort: function(arr) {
            if (arr.length === 0) return arr;
            
            let max = Math.max(...arr);
            let exp = 1;

            while (Math.floor(max / exp) > 0) {
                let output = new Array(arr.length);
                let count = new Array(10).fill(0);

                for (let i = 0; i < arr.length; i++) {
                    let digit = Math.floor(arr[i] / exp) % 10;
                    count[digit]++;
                }

                for (let i = 1; i < 10; i++) {
                    count[i] += count[i - 1];
                }

                for (let i = arr.length - 1; i >= 0; i--) {
                    let digit = Math.floor(arr[i] / exp) % 10;
                    output[count[digit] - 1] = arr[i];
                    count[digit]--;
                }

                for (let i = 0; i < arr.length; i++) {
                    arr[i] = output[i];
                }

                exp *= 10;
            }

            return arr;
        }
    }
};

// --- Lógica de la Aplicación ---

let currentResults = {};
let currentArray = [];

function generateArray(size, type) {
    let arr = [];
    for (let i = 0; i < size; i++) {
        arr.push(Math.floor(Math.random() * 10000));
    }
    switch (type) {
        case 'sorted':
            arr.sort((a, b) => a - b);
            break;
        case 'partially':
            arr.sort((a, b) => a - b);
            for (let i = 0; i < size * 0.1; i++) {
                let idx1 = Math.floor(Math.random() * size);
                let idx2 = Math.floor(Math.random() * size);
                let temp = arr[idx1];
                arr[idx1] = arr[idx2];
                arr[idx2] = temp;
            }
            break;
        case 'reversed':
            arr.sort((a, b) => a - b);
            arr.reverse();
            break;
    }
    return arr;
}

function measureTime(algorithm, arr) {
    let arrCopy = [...arr]; 
    let start = performance.now();
    let sortedArray = algorithm.sort(arrCopy);
    let end = performance.now();
    return {
        time: end - start,
        sortedArray: sortedArray 
    };
}

function runTestsForScenario(type) {
    let size = parseInt(document.getElementById('dataSize').value);
    if (isNaN(size) || size <= 0) {
        alert("Por favor, introduce un tamaño de datos válido.");
        return null;
    }
    
    let results = {};
    let testArray = generateArray(size, type);

    currentArray = [...testArray]; 
    window.sortedArrayExample = null; 

    Object.keys(algorithms).forEach(algoName => {
        if (size >= 20000 && (algoName === 'bubbleSort' || algoName === 'selectionSort' || algoName === 'insertionSort')) {
            results[algoName] = null; 
        } else {
            try {
                let result = measureTime(algorithms[algoName], testArray);
                results[algoName] = result.time;
                if (!window.sortedArrayExample) {
                    window.sortedArrayExample = result.sortedArray;
                }
            } catch (error) {
                console.error('Error en ' + algoName + ': ' + error);
                results[algoName] = null;
            }
        }
    });

    return results;
}

function showResults(results, scenario) {
    let tbody = document.getElementById('results-body');
    tbody.innerHTML = '';

    let sortedAlgos = Object.keys(results)
        .filter(algo => results[algo] !== null) 
        .map(algo => ({
            name: algo,
            time: results[algo]
        }))
        .sort((a, b) => a.time - b.time); 

    if (sortedAlgos.length === 0) {
        tbody.innerHTML = '<tr><td colspan="3" class="no-data">No hay datos (algoritmos lentos se omiten para tamaños grandes).</td></tr>';
    } else {
        sortedAlgos.forEach((algo, index) => {
            let row = document.createElement('tr');
            if (index === 0) row.className = 'pos-1';
            else if (index === 1) row.className = 'pos-2';
            else if (index === 2) row.className = 'pos-3';

            row.innerHTML = `
                <td>${index + 1}°</td>
                <td>${algorithms[algo.name].name}</td>
                <td>${algo.time.toFixed(2)} ms</td>
            `;
            tbody.appendChild(row);
        });
    }

    updateChart(results, scenario);
    showSortedArray();
}

function showSortedArray() {
    let arrayContent = document.getElementById('array-content');
    if (window.sortedArrayExample) {
        let displayArray = window.sortedArrayExample.length > 500
            ? window.sortedArrayExample.slice(0, 500).join(', ') + '... (y más)'
            : window.sortedArrayExample.join(', ');
            
        arrayContent.textContent = '[' + displayArray + ']';
    } else {
        arrayContent.textContent = '[No se pudo generar el array ordenado]';
    }
}

function updateChart(results, scenario) {
    let scenarioName = getScenarioName(scenario);

    // Mostramos siempre todos los algoritmos (barras delgadas)
    let algorithmNames = Object.keys(algorithms).map(algo => algorithms[algo].name);
    // Ponemos 0 si el resultado es null (como en el código de ejemplo)
    let times = Object.keys(algorithms).map(algo => results[algo] || 0);

    let backgroundColor;
    switch (scenario) {
        case 'sorted':
            backgroundColor = 'rgba(75, 192, 192, 0.8)';
            break;
        case 'partially':
            backgroundColor = 'rgba(255, 159, 64, 0.8)';
            break;
        case 'reversed':
            backgroundColor = 'rgba(255, 99, 132, 0.8)';
            break;
        default:
            backgroundColor = 'rgba(54, 162, 235, 0.8)';
    }

    // Actualizamos los datos de la gráfica existente
    window.performanceChart.data.labels = algorithmNames;
    window.performanceChart.data.datasets[0].label = 'Tiempo (ms) - ' + scenarioName;
    window.performanceChart.data.datasets[0].data = times;
    window.performanceChart.data.datasets[0].backgroundColor = backgroundColor;
    window.performanceChart.data.datasets[0].borderColor = backgroundColor.replace('0.8', '1');
    
    window.performanceChart.update();
}


function getScenarioName(scenario) {
    switch (scenario) {
        case 'sorted': return 'Ordenados';
        case 'partially': return 'Medianamente Ordenados';
        case 'reversed': return 'Inversos';
        default: return 'Desconocido'; // Dejado como en tu ejemplo
    }
}

function runScenarioTest(scenario, scenarioName) {
    let loading = document.getElementById('loading');
    let loadingText = document.getElementById('loading-text');
    let size = parseInt(document.getElementById('dataSize').value);

    loadingText.textContent = `Procesando ${scenarioName} (${size} elementos)...`;
    loading.style.display = 'block';

    document.querySelectorAll('.test-btn').forEach(btn => {
        btn.disabled = true;
    });

    setTimeout(() => {
        try {
            let results = runTestsForScenario(scenario);
            if (results) {
                currentResults = results;
                showResults(results, scenario);
            }
        } catch (error) {
            alert('Error: ' + error.message);
            console.error(error);
        } finally {
            loading.style.display = 'none';
            document.querySelectorAll('.test-btn').forEach(btn => {
                btn.disabled = false;
            });
        }
    }, 100);
}


// --- Inicialización ---
document.addEventListener('DOMContentLoaded', function() {
    let ctx = document.getElementById('chart').getContext('2d');
    
    window.performanceChart = new Chart(ctx, {
        type: 'bar', 
        data: {
            labels: Object.keys(algorithms).map(algo => algorithms[algo].name),
            datasets: [{
                label: 'Selecciona un escenario para ver resultados',
                data: [],
                backgroundColor: 'rgba(200, 200, 200, 0.5)',
                borderColor: 'rgba(200, 200, 200, 1)',
                borderWidth: 1
            }]
        },
        options: {
            // responsive: true por defecto
            // maintainAspectRatio: true por defecto (esto es lo que la hace pequeña)
            
            scales: {
                x: { 
                    title: {
                        display: true,
                        text: 'Algoritmos'
                    }
                },
                y: { 
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Tiempo (milisegundos)'
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                }
            }
        }
    });

    // Configurar botones
    document.getElementById('testSorted').addEventListener('click', function() {
        runScenarioTest('sorted', 'Array Ordenado');
    });

    document.getElementById('testPartially').addEventListener('click', function() {
        runScenarioTest('partially', 'Array Medianamente Ordenado');
    });

    document.getElementById('testReversed').addEventListener('click', function() {
        runScenarioTest('reversed', 'Array Inverso');
    });
    
});