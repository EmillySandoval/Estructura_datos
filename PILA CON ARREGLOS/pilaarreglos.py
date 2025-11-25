class Pila:
    def _init_(self, tamanio_maximo=100):
        self.TAMANIO_MAXIMO = tamanio_maximo
        self.pila = [None] * self.TAMANIO_MAXIMO
        self.tope = -1
    
    def apilar(self, numero):
        if self.tope == self.TAMANIO_MAXIMO - 1:
            print("Desbordamiento de Pila")
            return False
        self.tope += 1
        self.pila[self.tope] = numero
        return True
    
    def desapilar(self):
        if self.tope == -1:
            print("Subdesbordamiento de Pila")
            return -1
        elemento = self.pila[self.tope]
        self.tope -= 1
        return elemento
    
    def mirar(self):
        if self.tope == -1:
            print("La pila está vacía")
            return -1
        return self.pila[self.tope]
    
    def esta_vacia(self):
        return self.tope == -1
    
    def esta_llena(self):
        return self.tope == self.TAMANIO_MAXIMO - 1
    
    def mostrar(self):
        if self.esta_vacia():
            return "[]"
        return str(self.pila[:self.tope + 1])

# Ejemplo de uso
if __name__ == "_main_":
    p = Pila(5)
    
    print("=== PILA CON ARREGLOS ===")
    p.apilar(10)
    p.apilar(20)
    p.apilar(30)
    
    print("Pila:", p.mostrar())
    print("Elemento Superior:", p.mirar())
    print("Extrae elemento:", p.desapilar())
    print("Elemento Superior:", p.mirar())
    print("Pila después:", p.mostrar())
    print("¿Está vacía?", p.esta_vacia())
    print("¿Está llena?", p.esta_llena())