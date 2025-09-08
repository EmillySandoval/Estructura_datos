matriz2D = [[1,2,3],[4,5,6],[7,8,9]]
matriz1D = []

print("Matriz 2D original:")
for fila in matriz2D:
    print(fila)
    matriz1D.extend(fila)

print("\nMatriz 1D:")
print(matriz1D)

