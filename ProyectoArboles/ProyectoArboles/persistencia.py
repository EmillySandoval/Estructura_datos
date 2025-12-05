import json
import os
from sistema_archivos import Arbol, Nodo

class Persistencia:
    # Maneja la carga y guardado automatico en archivo JSON
    
    def __init__(self, archivo="datos.json"):
        self.archivo = archivo
    
    def guardar_automatico(self, arbol):
        # Guarda el arbol automaticamente en JSON
        try:
            if arbol.raiz:
                datos = {
                    "raiz": arbol.raiz.to_dict(),
                    "papelera": arbol.papelera
                }
                
                with open(self.archivo, 'w', encoding='utf-8') as f:
                    json.dump(datos, f, indent=2, ensure_ascii=False)
                
                return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False
    
    def cargar(self):
        # Carga el arbol desde archivo JSON
        try:
            if not os.path.exists(self.archivo):
                return Arbol()
            
            with open(self.archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            arbol = Arbol()
            
            # Cargar raiz
            if "raiz" in datos:
                arbol.raiz = Nodo.from_dict(datos["raiz"])
                # Reconstruir diccionario de nodos
                self._reconstruir_diccionario(arbol, arbol.raiz)
            
            # Cargar papelera
            if "papelera" in datos:
                arbol.papelera = datos["papelera"]
            
            return arbol
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