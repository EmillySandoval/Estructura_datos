def ordenamiento_por_seleccion(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
numeros = [64, 25, 12, 22, 11]
print("Lista original:", numeros)
ordenamiento_por_seleccion(numeros)
print("Lista ordenada:", numeros)