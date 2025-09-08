let matriz2D = [[1,2,3],[4,5,6],[7,8,9]];
let matriz1D = [];

console.log("Matriz 2D original:");
matriz2D.forEach(fila => {
    console.log(fila);
    matriz1D.push(...fila);
});

console.log("Matriz 1D:");
console.log(matriz1D);

