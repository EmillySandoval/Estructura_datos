def insertar_en_indice(lista, valor, indice):
    lista.insert(indice, valor)
    return lista


mi_lista = [1, 2, 3 ,  5]
print(insertar_en_indice(mi_lista, 4, 3)) 