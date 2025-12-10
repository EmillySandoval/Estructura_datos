import json
import os
import sys
from pathlib import Path

# Añadir el directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))

from sistema_archivos import Arbol, Nodo

class Persistencia:
    # Maneja la carga y guardado automatico en archivo JSON
    
    def __init__(self, archivo="datos.json"):
        self.archivo = archivo
    
    def guardar_automatico(self, arbol):
        try:
            # Construir un diccionario serializable y consistente
            datos = {}

            # Raiz
            raiz = getattr(arbol, 'raiz', None)
            datos['raiz'] = raiz.to_dict() if raiz is not None else None

            # Papelera (usar to_dict si existe)
            papelera = getattr(arbol, 'papelera', None)
            if papelera is not None and hasattr(papelera, 'to_dict'):
                try:
                    datos['papelera'] = papelera.to_dict()
                except Exception:
                    datos['papelera'] = None
            else:
                datos['papelera'] = None

            # Sistema de búsqueda
            busqueda = getattr(arbol, 'busqueda', None)
            if busqueda is not None and hasattr(busqueda, 'to_dict'):
                try:
                    datos['busqueda'] = busqueda.to_dict()
                except Exception:
                    datos['busqueda'] = None
            else:
                datos['busqueda'] = None

            # Guardar en JSON
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False
    
    def cargar(self):
        try:
            if not os.path.exists(self.archivo):
                return Arbol()
            
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            arbol = Arbol()
            
            # Cargar raiz
            if "raiz" in datos and datos["raiz"] is not None:
                arbol.raiz = Nodo.from_dict(datos["raiz"])
                self._reconstruir_diccionario(arbol, arbol.raiz)
            
            # CAMBIO: Cargar papelera usando PapeleraManager
            if "papelera" in datos:
                # Si el valor es None, mantener la instancia por defecto
                if datos["papelera"] is None:
                    arbol.papelera = getattr(arbol, 'papelera', None) or arbol.papelera
                else:
                    from papelera_manager import PapeleraManager
                    arbol.papelera = PapeleraManager.from_dict(datos["papelera"])
            
            # Cargar sistema de busqueda
            if "busqueda" in datos and datos["busqueda"] is not None:
                from busqueda_trie import SistemaBusqueda
                arbol.busqueda = SistemaBusqueda.from_dict(datos["busqueda"])
            
            return arbol
        # ... resto del codigo igual ... 
       
           
        except Exception as e:
            print(f"Error al cargar archivo: {e}")
            return Arbol()
    
    def _reconstruir_diccionario(self, arbol, nodo):
        # Reconstruye el diccionario de nodos recursivamente
        arbol.nodos[nodo.id] = nodo
        for hijo in nodo.hijos:
            self._reconstruir_diccionario(arbol, hijo)
    
    def exportar_preorden(self, arbol, archivo_salida="preorden.txt"):
        # Exporta el recorrido en preorden a un archivo
        try:
            recorrido = arbol.recorrido_preorden()
            
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                f.write("Recorrido en preorden del sistema de archivos\n")
                f.write("=" * 50 + "\n\n")
                
                for item in recorrido:
                    tipo = "DIR" if item["tipo"] == "carpeta" else "FILE"
                    f.write(f"{tipo}\t{item['ruta']}\n")
                    if item["tipo"] == "archivo" and item["contenido"]:
                        f.write(f"\tContenido: {item['contenido']}\n")
                
                f.write(f"\nTotal de elementos: {len(recorrido)}\n")
            
            return True
        except Exception as e:
            print(f"Error al exportar: {e}")
            return False