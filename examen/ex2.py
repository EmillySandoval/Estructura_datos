
def ordenamiento_burbuja(lista):
    """Ordena la lista usando el método de burbuja."""
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


matriz = []

print(" Ingresa los valores para una matriz de 6x6:")
for fila in range(6):
    fila_actual = []
    for columna in range(6):
        valor = int(input(f"Valor en posición [{fila}][{columna}]: "))
        fila_actual.append(valor)
    matriz.append(fila_actual)


print("\n Matriz original:")
for fila in matriz:
    print(fila)


lista_valores = [valor for fila in matriz for valor in fila]


lista_ordenada = ordenamiento_burbuja(lista_valores.copy())


valor_maximo = lista_ordenada[-1]

print(f"\nEl valor máximo en la matriz es: {valor_maximo}")