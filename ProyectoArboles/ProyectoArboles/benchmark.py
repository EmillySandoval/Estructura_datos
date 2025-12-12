import time
import random
import string
import sys
from sistema_archivos import Arbol


class Benchmark:
    """Versión limpia y compacta del benchmark.

    Conserva las pruebas principales: inserción, búsqueda, eliminación, memoria
    y casos límite. Esta versión evita duplicados y errores de sintaxis.
    """

    def __init__(self):
        self.resultados = []

    def generar_nombre_aleatorio(self, longitud=10):
        return ''.join(random.choices(string.ascii_lowercase, k=longitud))

    def generar_contenido_aleatorio(self, longitud=100):
        return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=longitud))

    def prueba_insercion_masiva(self, num_nodos=1000):
        print(f"\n[PRUEBA] Insercion masiva: {num_nodos} nodos")
        arbol = Arbol()
        arbol.crear_raiz()

        tiempos = []
        for i in range(num_nodos):
            inicio = time.time()
            tipo = "archivo" if i % 3 == 0 else "carpeta"
            nombre = f"nodo_{i}_{self.generar_nombre_aleatorio(5)}"
            contenido = self.generar_contenido_aleatorio(50) if tipo == "archivo" else ""

            ruta_padre = "/" if i < max(1, num_nodos // 10) else f"/carpeta_{i % 10}"
            arbol.crear_nodo(nombre, tipo, ruta_padre, contenido)
            fin = time.time()
            tiempos.append(fin - inicio)

        tiempo_total = sum(tiempos)
        tiempo_promedio = (tiempo_total / num_nodos) if num_nodos > 0 else 0
        tamano_real = arbol.tamano()

        resultado = {
            "prueba": "insercion_masiva",
            "nodos": num_nodos,
            "tiempo_total": tiempo_total,
            "tiempo_promedio": tiempo_promedio,
            "nodos_por_segundo": (num_nodos / tiempo_total) if tiempo_total > 0 else 0,
            "tamano_verificado": tamano_real,
        }

        print(f"  Nodos insertados: {num_nodos}")
        print(f"  Tiempo total: {tiempo_total:.4f}s, promedio: {tiempo_promedio:.6f}s")
        print(f"  Tamano verificado: {tamano_real}")
        return resultado

    def prueba_busqueda_masiva(self, num_busquedas=1000, num_nodos=5000):
        print(f"\n[PRUEBA] Busqueda masiva: {num_busquedas} busquedas en {num_nodos} nodos")
        arbol = Arbol()
        arbol.crear_raiz()

        nombres_insertados = []
        for i in range(num_nodos):
            nombre = f"archivo_{i}_{self.generar_nombre_aleatorio(4)}"
            nombres_insertados.append(nombre)
            arbol.crear_nodo(nombre, "archivo", "/", f"contenido_{i}")

        tiempos_exacta = []
        tiempos_prefijo = []
        for i in range(num_busquedas):
            if i % 2 == 0:
                nombre_buscar = random.choice(nombres_insertados) if random.random() > 0.3 else "no_existe"
                inicio = time.time()
                arbol.buscar_exacta(nombre_buscar)
                fin = time.time()
                tiempos_exacta.append(fin - inicio)
            else:
                prefijo = random.choice(["arc", "file", "doc", "img", "no_"])
                inicio = time.time()
                arbol.buscar_autocompletado(prefijo, 10)
                fin = time.time()
                tiempos_prefijo.append(fin - inicio)

        tiempo_promedio_exacta = (sum(tiempos_exacta) / len(tiempos_exacta)) if tiempos_exacta else 0
        tiempo_promedio_prefijo = (sum(tiempos_prefijo) / len(tiempos_prefijo)) if tiempos_prefijo else 0
        tiempo_total = sum(tiempos_exacta) + sum(tiempos_prefijo)

        resultado = {
            "prueba": "busqueda_masiva",
            "nodos": num_nodos,
            "busquedas": num_busquedas,
            "tiempo_total": tiempo_total,
            "tiempo_promedio_exacta": tiempo_promedio_exacta,
            "tiempo_promedio_prefijo": tiempo_promedio_prefijo,
        }

        print(f"  Tiempo total busquedas: {tiempo_total:.4f}s")
        return resultado

    def prueba_eliminacion_masiva(self, num_nodos=1000):
        print(f"\n[PRUEBA] Eliminacion masiva: {num_nodos} nodos")
        arbol = Arbol()
        arbol.crear_raiz()

        rutas = []
        for i in range(num_nodos):
            nombre = f"temp_{i}"
            arbol.crear_nodo(nombre, "archivo", "/", f"temp_{i}")
            rutas.append(f"/{nombre}")

        tiempos = []
        for ruta in rutas:
            inicio = time.time()
            arbol.eliminar_nodo(ruta)
            fin = time.time()
            tiempos.append(fin - inicio)

        tiempo_total = sum(tiempos)
        items_papelera = len(arbol.listar_papelera())

        resultado = {
            "prueba": "eliminacion_masiva",
            "nodos": num_nodos,
            "tiempo_total": tiempo_total,
            "items_papelera": items_papelera,
        }

        print(f"  Items en papelera: {items_papelera}")
        return resultado

    def prueba_memoria(self, num_nodos=5000):
        print(f"\n[PRUEBA] Uso de memoria: {num_nodos} nodos")
        try:
            import psutil  # type: ignore
        except Exception:
            print("psutil no disponible; omitiendo prueba de memoria")
            return {"prueba": "memoria", "skipped": True}

        import os
        proceso = psutil.Process(os.getpid())
        memoria_inicial = proceso.memory_info().rss / 1024 / 1024

        arbol = Arbol()
        arbol.crear_raiz()
        for i in range(num_nodos):
            nombre = f"mem_test_{i}"
            arbol.crear_nodo(nombre, "archivo", "/", "x" * 100)

        memoria_final = proceso.memory_info().rss / 1024 / 1024
        memoria_usada = memoria_final - memoria_inicial

        resultado = {
            "prueba": "memoria",
            "nodos": num_nodos,
            "memoria_usada_mb": memoria_usada,
        }
        print(f"  Memoria usada: {memoria_usada:.2f} MB")
        return resultado

    def prueba_casos_limite(self):
        print("\n[PRUEBA] Casos limite")
        resultados = []

        arbol_vacio = Arbol()
        try:
            r = arbol_vacio.buscar_por_ruta("/")
            resultados.append(("buscar_raiz_en_vacio", r is None or r == arbol_vacio.raiz))
        except Exception:
            resultados.append(("buscar_raiz_en_vacio", False))

        arbol_largo = Arbol()
        arbol_largo.crear_raiz()
        ruta = "/"
        for i in range(20):
            nombre = f"nivel_{i}"
            arbol_largo.crear_nodo(nombre, "carpeta", ruta)
            ruta = ruta.rstrip("/") + "/" + nombre
        nodo = arbol_largo.buscar_por_ruta(ruta)
        resultados.append(("ruta_profunda", nodo is not None))

        return {"prueba": "casos_limite", "detalles": resultados}

    def ejecutar_suite_completa(self):
        resultados = []
        resultados.append(self.prueba_insercion_masiva(100))
        resultados.append(self.prueba_busqueda_masiva(200, 500))
        resultados.append(self.prueba_eliminacion_masiva(100))
        resultados.append(self.prueba_casos_limite())
        try:
            resultados.append(self.prueba_memoria(500))
        except Exception:
            pass
        self.mostrar_resumen(resultados)
        return resultados

    def mostrar_resumen(self, resultados):
        print("\n=== RESUMEN BENCHMARK ===")
        for r in resultados:
            print(f"- {r.get('prueba')}: keys={list(r.keys())}")

def ejecutar_benchmark():
    b = Benchmark()
    b.ejecutar_suite_completa()


if __name__ == "__main__":
    ejecutar_benchmark()
