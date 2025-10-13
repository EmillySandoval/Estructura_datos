def funcion_hash(valor, minimo, tamaño_intervalo):
    return (valor - minimo) // tamaño_intervalo

def ordenar_por_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_actual

def ordenamiento_hash(lista_numeros):
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    cantidad_de_cubetas = len(lista_numeros)
    tamaño_intervalo = ((maximo - minimo) // cantidad_de_cubetas) + 1

    cubetas = [[] for _ in range(cantidad_de_cubetas)]
    
    for numero in lista_numeros:
        indice = funcion_hash(numero, minimo, tamaño_intervalo)
        cubetas[indice].append(numero)

    for cubeta in cubetas:
        ordenar_por_insercion(cubeta)

    lista_ordenada = []
    for cubeta in cubetas:
        lista_ordenada.extend(cubeta)

    return lista_ordenada


numeros = [36, 34, 43, 11, 15, 20, 28]
resultado = ordenamiento_hash(numeros)
print("Lista ordenada:", resultado)