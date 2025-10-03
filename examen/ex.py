
def busqueda_lineal(arreglo, numero_buscado):
    """Busca el número en el arreglo usando búsqueda lineal."""
    for posicion in range(len(arreglo)):
        if arreglo[posicion] == numero_buscado:
            return posicion  
    return -1  


arreglo_numeros = []

print(" Ingresa 10 números:")
for i in range(10):
    numero = int(input(f"Número {i+1}: "))
    arreglo_numeros.append(numero)


print("\n Arreglo original:", arreglo_numeros)


numero_a_buscar = int(input("\n ¿Qué número deseas buscar?: "))


posicion = busqueda_lineal(arreglo_numeros, numero_a_buscar)


if posicion != -1:
    print(f" El número {numero_a_buscar} se encuentra en la posición {posicion} del arreglo.")
    print(f" Valor encontrado: {arreglo_numeros[posicion]}")
else:
    print(f"❌ El número {numero_a_buscar} no se encuentra en el arreglo.")