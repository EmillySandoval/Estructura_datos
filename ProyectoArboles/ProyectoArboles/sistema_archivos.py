import uuid
from busqueda_trie import SistemaBusqueda

class Nodo:
    # Clase que representa un nodo en el sistema de archivos
    # Un nodo puede ser carpeta (DIR) o archivo (FILE)
    
    def __init__(self, id_nodo, nombre, tipo, contenido=""):
        self.id = id_nodo
        self.nombre = nombre
        self.tipo = tipo  # 'carpeta' o 'archivo'
        self.contenido = contenido
        self.hijos = []  # Lista de nodos hijos
        self.padre = None  # Referencia al nodo padre
    
    def agregar_hijo(self, hijo):
        # Agrega un nodo hijo a este nodo
        hijo.padre = self
        self.hijos.append(hijo)
    
    def eliminar_hijo(self, hijo):
        # Elimina un hijo de la lista de hijos
        if hijo in self.hijos:
            self.hijos.remove(hijo)
            hijo.padre = None
    
    def obtener_ruta(self):
        # Obtiene la ruta completa desde la raiz
        ruta = []
        actual = self
        while actual is not None:
            ruta.insert(0, actual.nombre)
            actual = actual.padre
        return "/".join(ruta) if ruta else "/"
    
    def to_dict(self):
        # Convierte el nodo a diccionario para JSON
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "contenido": self.contenido,
            "hijos": [hijo.to_dict() for hijo in self.hijos]
        }
    
    @classmethod
    def from_dict(cls, data, padre=None):
        # Crea un nodo desde un diccionario
        nodo = cls(data["id"], data["nombre"], data["tipo"], data.get("contenido", ""))
        nodo.padre = padre
        
        # Crear hijos recursivamente
        for hijo_data in data.get("hijos", []):
            hijo = cls.from_dict(hijo_data, nodo)
            nodo.hijos.append(hijo)
        
        return nodo

class Arbol:
    # Clase principal que maneja el arbol de archivos y carpetas
    
    
    def __init__(self):
        self.raiz = None
        self.nodos = {}
        self.papelera = []
        self.busqueda = SistemaBusqueda()  
        
    def  crear_raiz(self, nombre="root"):
        id_nodo = str(uuid.uuid4())[:8]
        self.raiz = Nodo(id_nodo, nombre, "carpeta")
        self.nodos[id_nodo] = self.raiz
        
        # NUEVO: Indexar la raiz en el sistema de busqueda
        self.busqueda.indexar_nodo(nombre, id_nodo)
        
        return self.raiz
    
    def crear_nodo(self, nombre, tipo, ruta_padre="/", contenido=""):
        # Crea un nuevo nodo en la ruta especificada
        if not self.raiz:
            self.crear_raiz()
        
        # Buscar el nodo padre
        padre = self.buscar_por_ruta(ruta_padre)
        
        if not padre or padre.tipo != "carpeta":
            return None
        
        # Verificar si ya existe un hijo con ese nombre
        for hijo in padre.hijos:
            if hijo.nombre == nombre:
                return None
        
        id_nodo = str(uuid.uuid4())[:8]
        nuevo_nodo = Nodo(id_nodo, nombre, tipo, contenido)
        padre.agregar_hijo(nuevo_nodo)
        self.nodos[id_nodo] = nuevo_nodo
        
        # NUEVO: Indexar en sistema de busqueda
        self.busqueda.indexar_nodo(nombre, id_nodo)
        
        return nuevo_nodo
    
    def buscar_por_id(self, id_nodo):
        # Busca un nodo por su ID
        return self.nodos.get(id_nodo)
    
    def buscar_por_ruta(self, ruta):
        # Busca un nodo por su ruta completa
        if not ruta or ruta == "/" or ruta == ".":
            return self.raiz
        
        # Limpiar y dividir la ruta
        if ruta.startswith("/"):
            ruta = ruta[1:]
        
        partes = ruta.split("/")
        actual = self.raiz
        
        for parte in partes:
            if parte == "" or parte == ".":
                continue
            elif parte == "..":
                actual = actual.padre if actual.padre else self.raiz
                continue
            
            encontrado = False
            for hijo in actual.hijos:
                if hijo.nombre == parte:
                    actual = hijo
                    encontrado = True
                    break
            
            if not encontrado:
                return None
        
        return actual
    
    def buscar_autocompletado(self, prefijo, max_resultados=10):
        resultado_busqueda = self.busqueda.buscar_autocompletado(prefijo, max_resultados)
        
        resultados_enriquecidos = []
        for item in resultado_busqueda["resultados"]:
            nodo = self.buscar_por_id(item["id_nodo"])
            if nodo:
                resultados_enriquecidos.append({
                    "nombre": nodo.nombre,
                    "tipo": nodo.tipo,
                    "ruta": nodo.obtener_ruta(),
                    "id": nodo.id
                })
        
        return {
            "prefijo": resultado_busqueda["prefijo"],
            "resultados": resultados_enriquecidos,
            "total_encontrados": resultado_busqueda["total_encontrados"],
            "mostrando": len(resultados_enriquecidos)
        }
    
    def buscar_exacta(self, nombre):
        resultado_busqueda = self.busqueda.buscar_exacta(nombre)
        
        resultados_enriquecidos = []
        for id_nodo in resultado_busqueda["ids_nodos"]:
            nodo = self.buscar_por_id(id_nodo)
            if nodo:
                resultados_enriquecidos.append({
                    "nombre": nodo.nombre,
                    "tipo": nodo.tipo,
                    "ruta": nodo.obtener_ruta(),
                    "id": nodo.id,
                    "contenido": nodo.contenido if nodo.tipo == "archivo" else ""
                })
        
        return {
            "nombre": resultado_busqueda["nombre"],
            "resultados": resultados_enriquecidos,
            "total_encontrados": len(resultados_enriquecidos)
        }
    
    def eliminar_nodo(self, ruta):
        # Elimina un nodo moviendolo a la papelera
        nodo = self.buscar_por_ruta(ruta)
        if not nodo or nodo == self.raiz:
            return False
        
        # Remover de los hijos del padre
        nodo.padre.eliminar_hijo(nodo)
        
        # Mover a la papelera
        self.papelera.append({
            "id": nodo.id,
            "nombre": nodo.nombre,
            "tipo": nodo.tipo,
            "contenido": nodo.contenido,
            "ruta_original": nodo.obtener_ruta()
        })
        
        self.busqueda.eliminar_nodo(nodo.nombre, nodo.id)
        
        # Eliminar recursivamente del diccionario
        self._eliminar_recursivo(nodo)
        
        return True
    
    def _eliminar_recursivo(self, nodo):
        if nodo.id in self.nodos:
            # NUEVO: Eliminar este nodo y sus hijos del sistema de busqueda
            for hijo in nodo.hijos:
                self._eliminar_recursivo(hijo)
            
            # NUEVO: Eliminar este nodo
            self.busqueda.eliminar_nodo(nodo.nombre, nodo.id)
            del self.nodos[nodo.id]
    
    def mover_nodo(self, ruta_origen, ruta_destino):
        # Mueve un nodo a una nueva ubicacion
        nodo = self.buscar_por_ruta(ruta_origen)
        nuevo_padre = self.buscar_por_ruta(ruta_destino)
        
        if not nodo or not nuevo_padre or nuevo_padre.tipo != "carpeta":
            return False
        
        # Verificar que no se mueva a si mismo o a descendiente
        if self._es_descendiente(nuevo_padre, nodo):
            return False
        
        # Verificar que no exista ya un nodo con ese nombre en el destino
        for hijo in nuevo_padre.hijos:
            if hijo.nombre == nodo.nombre:
                return False
        
        # Remover del padre actual
        nodo.padre.eliminar_hijo(nodo)
        
        # Agregar al nuevo padre
        nuevo_padre.agregar_hijo(nodo)
        
        return True
    
    def _es_descendiente(self, posible_descendiente, ancestro):
        # Verifica si un nodo es descendiente de otro
        actual = posible_descendiente
        while actual:
            if actual == ancestro:
                return True
            actual = actual.padre
        return False
    
    def renombrar_nodo(self, ruta, nuevo_nombre):
        # Renombra un nodo
        nodo = self.buscar_por_ruta(ruta)
        if not nodo or nodo == self.raiz:
            return False
        
        # Verificar que no exista otro nodo con ese nombre en la misma carpeta
        for hermano in nodo.padre.hijos:
            if hermano != nodo and hermano.nombre == nuevo_nombre:
                return False
        
        nombre_viejo = nodo.nombre
        self.busqueda.actualizar_nodo(nombre_viejo, nuevo_nombre, nodo.id)
        
        # Actualizar nombre
        nodo.nombre = nuevo_nombre
        return True
    
    def listar_hijos(self, ruta="/"):
        # Lista los hijos de un nodo
        nodo = self.buscar_por_ruta(ruta)
        if not nodo:
            return None
        
        resultado = []
        for hijo in nodo.hijos:
            resultado.append({
                "nombre": hijo.nombre,
                "tipo": hijo.tipo,
                "tamano": len(hijo.contenido) if hijo.tipo == "archivo" else 0
            })
        
        return resultado
    
    def obtener_ruta_completa(self, ruta):
        # Obtiene la ruta completa de un nodo
        nodo = self.buscar_por_ruta(ruta)
        if nodo:
            return nodo.obtener_ruta()
        return None
    
    def recorrido_preorden(self, nodo=None, resultado=None):
        # Realiza recorrido en preorden del arbol
        if resultado is None:
            resultado = []
        
        if nodo is None:
            if self.raiz:
                nodo = self.raiz
            else:
                return resultado
        
        resultado.append({
            "nombre": nodo.nombre,
            "tipo": nodo.tipo,
            "ruta": nodo.obtener_ruta(),
            "contenido": nodo.contenido if nodo.tipo == "archivo" else ""
        })
        
        for hijo in nodo.hijos:
            self.recorrido_preorden(hijo, resultado)
        
        return resultado
    
    def altura(self, nodo=None):
        # Calcula la altura del arbol
        if nodo is None:
            nodo = self.raiz
        
        if not nodo or not nodo.hijos:
            return 0
        
        altura_max = 0
        for hijo in nodo.hijos:
            altura_hijo = self.altura(hijo)
            altura_max = max(altura_max, altura_hijo)
        
        return altura_max + 1
    
    def tamano(self, nodo=None):
        # Calcula el numero total de nodos
        if nodo is None:
            nodo = self.raiz
        
        if not nodo:
            return 0
        
        contador = 1
        for hijo in nodo.hijos:
            contador += self.tamano(hijo)
        
        return contador
    
    def estadisticas(self):
        # Retorna estadisticas del sistema
        total_nodos = self.tamano()
        total_carpetas = 0
        total_archivos = 0
        total_contenido = 0
        
        def contar_nodos(nodo):
            nonlocal total_carpetas, total_archivos, total_contenido
            if nodo.tipo == "carpeta":
                total_carpetas += 1
            else:
                total_archivos += 1
                total_contenido += len(nodo.contenido)
            
            for hijo in nodo.hijos:
                contar_nodos(hijo)
        
        if self.raiz:
            contar_nodos(self.raiz)
        
        # NUEVO: Estadisticas de busqueda
        stats_busqueda = self.busqueda.estadisticas()
        
        return {
            "total_nodos": total_nodos,
            "carpetas": total_carpetas,
            "archivos": total_archivos,
            "bytes_contenido": total_contenido,
            "altura": self.altura(),
            "papelera": len(self.papelera),
            "busqueda_palabras": stats_busqueda["total_palabras_trie"],  # NUEVO
            "busqueda_entradas": stats_busqueda["total_entradas_hashmap"]  # NUEVO
        }