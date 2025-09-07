def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


lista = [3, 8, 1, 5, 9]
print(busqueda_lineal(lista, 5)) 