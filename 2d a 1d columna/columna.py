matriz2D = [[1,2,3],[4,5,6],[7,8,9]]
matriz1D = []

print("Matriz 2D original:")
for fila in matriz2D:
    print(fila)

for col in range(len(matriz2D[0])):
    for fila in range(len(matriz2D)):
        matriz1D.append(matriz2D[fila][col])

print("\nMatriz 1D (por columnas):")
print(matriz1D)
