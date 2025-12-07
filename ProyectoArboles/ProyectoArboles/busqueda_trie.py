import json

class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.es_final = False
        self.nodos_sistema = []

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()
        self.total_palabras = 0
    
    def insertar(self, palabra, id_nodo):
        actual = self.raiz
        
        for caracter in palabra.lower():
            if caracter not in actual.hijos:
                actual.hijos[caracter] = NodoTrie()
            actual = actual.hijos[caracter]
        
        actual.es_final = True
        if id_nodo not in actual.nodos_sistema:
            actual.nodos_sistema.append(id_nodo)
        self.total_palabras += 1
    
    def buscar_prefijo(self, prefijo):
        actual = self.raiz
        
        for caracter in prefijo.lower():
            if caracter not in actual.hijos:
                return []
            actual = actual.hijos[caracter]
        
        return self._recopilar_palabras(actual, prefijo)
    
    def _recopilar_palabras(self, nodo, prefijo_actual):
        resultados = []
        
        if nodo.es_final:
            for id_nodo in nodo.nodos_sistema:
                resultados.append({
                    "palabra": prefijo_actual,
                    "id_nodo": id_nodo
                })
        
        for caracter, hijo in nodo.hijos.items():
            resultados.extend(
                self._recopilar_palabras(hijo, prefijo_actual + caracter)
            )
        
        return resultados
    
    def eliminar(self, palabra, id_nodo):
        actual = self.raiz
        ruta = [self.raiz]
        
        for caracter in palabra.lower():
            if caracter not in actual.hijos:
                return False
            actual = actual.hijos[caracter]
            ruta.append(actual)
        
        if actual.es_final and id_nodo in actual.nodos_sistema:
            actual.nodos_sistema.remove(id_nodo)
            
            if not actual.nodos_sistema:
                actual.es_final = False
                self.total_palabras -= 1
            
            self._limpiar_ruta(ruta, palabra)
            return True
        
        return False
    
    def _limpiar_ruta(self, ruta, palabra):
        for i in range(len(ruta)-1, 0, -1):
            nodo_actual = ruta[i]
            
            if not nodo_actual.hijos and not nodo_actual.es_final:
                caracter = palabra[i-1].lower()
                padre = ruta[i-1]
                del padre.hijos[caracter]
            else:
                break
    
    def buscar_exacto(self, palabra):
        actual = self.raiz
        
        for caracter in palabra.lower():
            if caracter not in actual.hijos:
                return []
            actual = actual.hijos[caracter]
        
        if actual.es_final:
            return actual.nodos_sistema
        return []
    
    def contar_palabras(self):
        return self.total_palabras
    
    def to_dict(self):
        return self._nodo_a_dict(self.raiz)
    
    def _nodo_a_dict(self, nodo):
        resultado = {
            "es_final": nodo.es_final,
            "nodos_sistema": nodo.nodos_sistema,
            "hijos": {}
        }
        
        for caracter, hijo in nodo.hijos.items():
            resultado["hijos"][caracter] = self._nodo_a_dict(hijo)
        
        return resultado
    
    @classmethod
    def from_dict(cls, data):
        trie = cls()
        trie.raiz = cls._dict_a_nodo(data)
        trie.total_palabras = cls._contar_palabras(trie.raiz)
        return trie
    
    @classmethod
    def _dict_a_nodo(cls, data):
        nodo = NodoTrie()
        nodo.es_final = data.get("es_final", False)
        nodo.nodos_sistema = data.get("nodos_sistema", [])
        
        for caracter, hijo_data in data.get("hijos", {}).items():
            nodo.hijos[caracter] = cls._dict_a_nodo(hijo_data)
        
        return nodo
    
    @classmethod
    def _contar_palabras(cls, nodo):
        contador = 1 if nodo.es_final else 0
        
        for hijo in nodo.hijos.values():
            contador += cls._contar_palabras(hijo)
        
        return contador

class HashMapBusqueda:
    def __init__(self):
        self.tabla = {}
    
    def insertar(self, nombre, id_nodo):
        clave = nombre.lower()
        
        if clave not in self.tabla:
            self.tabla[clave] = []
        
        if id_nodo not in self.tabla[clave]:
            self.tabla[clave].append(id_nodo)
    
    def buscar_exacto(self, nombre):
        clave = nombre.lower()
        return self.tabla.get(clave, [])
    
    def eliminar(self, nombre, id_nodo):
        clave = nombre.lower()
        
        if clave in self.tabla:
            if id_nodo in self.tabla[clave]:
                self.tabla[clave].remove(id_nodo)
                
                if not self.tabla[clave]:
                    del self.tabla[clave]
                return True
        
        return False
    
    def actualizar(self, nombre_viejo, nombre_nuevo, id_nodo):
        self.eliminar(nombre_viejo, id_nodo)
        self.insertar(nombre_nuevo, id_nodo)
    
    def to_dict(self):
        return self.tabla
    
    @classmethod
    def from_dict(cls, data):
        mapa = cls()
        mapa.tabla = data
        return mapa

class SistemaBusqueda:
    def __init__(self):
        self.trie = Trie()
        self.hashmap = HashMapBusqueda()
    
    def indexar_nodo(self, nombre, id_nodo):
        self.trie.insertar(nombre, id_nodo)
        self.hashmap.insertar(nombre, id_nodo)
    
    def eliminar_nodo(self, nombre, id_nodo):
        trie_resultado = self.trie.eliminar(nombre, id_nodo)
        hashmap_resultado = self.hashmap.eliminar(nombre, id_nodo)
        return trie_resultado or hashmap_resultado
    
    def actualizar_nodo(self, nombre_viejo, nombre_nuevo, id_nodo):
        self.trie.eliminar(nombre_viejo, id_nodo)
        self.trie.insertar(nombre_nuevo, id_nodo)
        self.hashmap.actualizar(nombre_viejo, nombre_nuevo, id_nodo)
    
    def buscar_autocompletado(self, prefijo, max_resultados=10):
        resultados_trie = self.trie.buscar_prefijo(prefijo)
        resultados_limitados = resultados_trie[:max_resultados]
        
        return {
            "prefijo": prefijo,
            "resultados": resultados_limitados,
            "total_encontrados": len(resultados_trie),
            "mostrando": len(resultados_limitados)
        }
    
    def buscar_exacta(self, nombre):
        ids_nodos = self.hashmap.buscar_exacto(nombre)
        
        return {
            "nombre": nombre,
            "ids_nodos": ids_nodos,
            "total_encontrados": len(ids_nodos)
        }
    
    def estadisticas(self):
        return {
            "total_palabras_trie": self.trie.contar_palabras(),
            "total_entradas_hashmap": len(self.hashmap.tabla),
            "trie_vacio": self.trie.contar_palabras() == 0,
            "hashmap_vacio": len(self.hashmap.tabla) == 0
        }
    
    def to_dict(self):
        return {
            "trie": self.trie.to_dict(),
            "hashmap": self.hashmap.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data):
        sistema = cls()
        
        if "trie" in data:
            sistema.trie = Trie.from_dict(data["trie"])
        
        if "hashmap" in data:
            sistema.hashmap = HashMapBusqueda.from_dict(data["hashmap"])
        
        return sistema