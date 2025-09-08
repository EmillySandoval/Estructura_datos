let matriz2D = [[1,2,3],[4,5,6],[7,8,9]];
let matriz1D = [];

console.log("Matriz 2D original:");
matriz2D.forEach(fila => console.log(fila));

for (let col = 0; col < matriz2D[0].length; col++) {
    for (let fila = 0; fila < matriz2D.length; fila++) {
        matriz1D.push(matriz2D[fila][col]);
    }
}

console.log("\nMatriz 1D (por columnas):");
console.log(matriz1D);
