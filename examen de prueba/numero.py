numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma = sum(numeros)
promedio = suma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print(f"La suma del vector es: {suma}")
print(f"El promedio del vector es: {promedio}")
print(f"El número máximo del vector es: {maximo}")
print(f"El número mínimo del vector es: {minimo}")