import json
import os
from datetime import datetime

class ItemPapelera:
    # Clase para representar un item en la papelera
    
    def __init__(self, id_nodo, nombre, tipo, contenido, ruta_original, fecha_eliminacion=None):
        self.id = id_nodo
        self.nombre = nombre
        self.tipo = tipo
        self.contenido = contenido
        self.ruta_original = ruta_original
        self.fecha_eliminacion = fecha_eliminacion or datetime.now()
    
    def to_dict(self):
        # Convierte a diccionario para JSON
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "contenido": self.contenido,
            "ruta_original": self.ruta_original,
            "fecha_eliminacion": self.fecha_eliminacion.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    @classmethod
    def from_dict(cls, data):
        # Crea desde diccionario
        fecha_str = data.get("fecha_eliminacion")
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S") if fecha_str else datetime.now()
        
        return cls(
            data["id"],
            data["nombre"],
            data["tipo"],
            data["contenido"],
            data["ruta_original"],
            fecha
        )

class PapeleraManager:
    # Gestiona la papelera de reciclaje del sistema
    
    def __init__(self, capacidad_maxima=100, dias_retencion=30):
        self.items = []
        self.capacidad_maxima = capacidad_maxima
        self.dias_retencion = dias_retencion
    
    def agregar_item(self, id_nodo, nombre, tipo, contenido, ruta_original):
        # Agrega un item a la papelera
        if len(self.items) >= self.capacidad_maxima:
            # Eliminar el item mas antiguo
            self.items.pop(0)
        
        nuevo_item = ItemPapelera(id_nodo, nombre, tipo, contenido, ruta_original)
        self.items.append(nuevo_item)
        return True
    
    def listar_items(self):
        # Lista todos los items en la papelera
        return self.items
    
    def buscar_por_nombre(self, nombre):
        # Busca items por nombre (partial match)
        resultados = []
        nombre_lower = nombre.lower()
        
        for item in self.items:
            if nombre_lower in item.nombre.lower():
                resultados.append(item)
        
        return resultados
    
    def buscar_por_ruta_original(self, ruta):
        # Busca items por ruta original
        resultados = []
        ruta_lower = ruta.lower()
        
        for item in self.items:
            if ruta_lower in item.ruta_original.lower():
                resultados.append(item)
        
        return resultados
    
    def restaurar_item(self, indice, arbol):
        # Restaura un item desde la papelera al arbol
        if indice < 0 or indice >= len(self.items):
            return None, "Indice fuera de rango"
        
        item = self.items[indice]
        
        # Verificar si la ruta original existe
        partes_ruta = item.ruta_original.split("/")
        if len(partes_ruta) < 2:
            return None, "Ruta original no valida"
        
        # Obtener nombre y ruta padre
        nombre_archivo = partes_ruta[-1]
        ruta_padre = "/".join(partes_ruta[:-1]) if len(partes_ruta) > 1 else "/"
        
        # Verificar si el padre existe
        padre = arbol.buscar_por_ruta(ruta_padre)
        if not padre or padre.tipo != "carpeta":
            return None, f"La ruta padre no existe o no es carpeta: {ruta_padre}"
        
        # Verificar que no exista ya un nodo con ese nombre
        for hijo in padre.hijos:
            if hijo.nombre == nombre_archivo:
                # Sugerir nuevo nombre
                nuevo_nombre = f"{nombre_archivo}_restaurado"
                return None, f"Ya existe un archivo con ese nombre. Prueba con: {nuevo_nombre}"
        
        # Crear nodo restaurado
        nodo_restaurado = arbol.crear_nodo(
            nombre_archivo,
            item.tipo,
            ruta_padre,
            item.contenido
        )
        
        if nodo_restaurado:
            # Eliminar de la papelera
            self.items.pop(indice)
            return nodo_restaurado, "Restaurado exitosamente"
        else:
            return None, "No se pudo restaurar el item"
    
    def eliminar_permanentemente(self, indice):
        # Elimina permanentemente un item de la papelera
        if indice < 0 or indice >= len(self.items):
            return False, "Indice fuera de rango"
        
        self.items.pop(indice)
        return True, "Eliminado permanentemente"
    
    def vaciar_papelera(self):
        # Vacía toda la papelera
        cantidad = len(self.items)
        self.items.clear()
        return cantidad
    
    def limpiar_automaticamente(self):
        # Limpia items antiguos automaticamente
        ahora = datetime.now()
        eliminados = 0
        
        for i in range(len(self.items) - 1, -1, -1):
            item = self.items[i]
            dias_pasados = (ahora - item.fecha_eliminacion).days
            
            if dias_pasados > self.dias_retencion:
                self.items.pop(i)
                eliminados += 1
        
        return eliminados
    
    def estadisticas(self):
        # Retorna estadisticas de la papelera
        total_items = len(self.items)
        tamano_total = sum(len(item.contenido) for item in self.items)
        
        tipos = {}
        for item in self.items:
            tipos[item.tipo] = tipos.get(item.tipo, 0) + 1
        
        return {
            "total_items": total_items,
            "tamano_bytes": tamano_total,
            "tipos": tipos,
            "capacidad_utilizada": f"{(total_items / self.capacidad_maxima) * 100:.1f}%"
        }
    
    def to_dict(self):
        # Convierte a diccionario para JSON
        return {
            "items": [item.to_dict() for item in self.items],
            "capacidad_maxima": self.capacidad_maxima,
            "dias_retencion": self.dias_retencion
        }
    
    @classmethod
    def from_dict(cls, data):
        # Crea desde diccionario
        manager = cls(
            data.get("capacidad_maxima", 100),
            data.get("dias_retencion", 30)
        )
        
        if "items" in data:
            for item_data in data["items"]:
                item = ItemPapelera.from_dict(item_data)
                manager.items.append(item)
        
        return manager