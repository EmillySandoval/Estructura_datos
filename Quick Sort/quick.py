def quick_sort(lista, nivel=0):
    if len(lista) <= 1:
        print("  " * nivel + f"Retorno: {lista}")
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    print("  " * nivel + f"Pivote: {pivote}, Menores: {menores}, Mayores: {mayores}")
    return quick_sort(menores, nivel + 1) + [pivote] + quick_sort(mayores, nivel + 1)

numeros = [8, 3, 1, 7, 0, 10, 2]
print("Original:", numeros)
ordenado = quick_sort(numeros)
print("Ordenado:", ordenado)