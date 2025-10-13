
def construir_monticulo(lista, tamaño, índice_raíz):
    índice_mayor = índice_raíz          # Asumimos que la raíz es el mayor
    índice_izquierdo = 2 * índice_raíz + 1  # Hijo izquierdo
    índice_derecho = 2 * índice_raíz + 2   # Hijo derecho

    # Verificamos si el hijo izquierdo existe y es mayor que la raíz
    if índice_izquierdo < tamaño and lista[índice_izquierdo] > lista[índice_mayor]:
        índice_mayor = índice_izquierdo

    # Verificamos si el hijo derecho existe y es mayor que el mayor actual
    if índice_derecho < tamaño and lista[índice_derecho] > lista[índice_mayor]:
        índice_mayor = índice_derecho

    # Si el mayor no es la raíz, intercambiamos y seguimos construyendo el montículo
    if índice_mayor != índice_raíz:
        lista[índice_raíz], lista[índice_mayor] = lista[índice_mayor], lista[índice_raíz]
        construir_monticulo(lista, tamaño, índice_mayor)

# Función principal para ordenar usando Heap Sort
def ordenar_por_monticulo(lista):
    tamaño = len(lista)

    # Paso 1: Construir el montículo máximo
    for índice in range(tamaño // 2 - 1, -1, -1):
        construir_monticulo(lista, tamaño, índice)

    # Paso 2: Extraer elementos uno por uno del montículo
    for índice_final in range(tamaño - 1, 0, -1):
        # Mover el mayor (raíz) al final
        lista[0], lista[índice_final] = lista[índice_final], lista[0]
        # Reconstruir el montículo con los elementos restantes
        construir_monticulo(lista, índice_final, 0)

# Ejemplo de uso
if __name__ == "__main__":
    lista_numeros = [12, 4, 7, 9, 1, 15, 3]
    print("Lista original:", lista_numeros)
    ordenar_por_monticulo(lista_numeros)
    print("Lista ordenada:", lista_numeros)