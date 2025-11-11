def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar la frecuencia de cada dígito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Cambiar count[i] para que contenga la posición actual
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el array de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copiar el array de salida al array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el número máximo para saber el número de dígitos
    max_num = max(arr)
    
    # Aplicar counting sort para cada dígito
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 2, 802, 24, 66]
    print("Array original:", arr)
    radix_sort(arr)
    print("Array ordenado:", arr)