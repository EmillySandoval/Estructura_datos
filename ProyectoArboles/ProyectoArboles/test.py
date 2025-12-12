import unittest
import os
import sys
from pathlib import Path
import tempfile
import shutil

# Añadir el directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))

from sistema_archivos import Arbol
from persistencia import Persistencia
from busqueda_trie import Trie, HashMapBusqueda, SistemaBusqueda

class TestSistemaArchivos(unittest.TestCase):
    # Pruebas unitarias para el sistema de archivos
    
    def setUp(self):
        self.arbol = Arbol()
        self.arbol.crear_raiz()
    
    def test_crear_carpeta_raiz(self):
        self.arbol.crear_nodo("documentos", "carpeta", "/")
        nodo = self.arbol.buscar_por_ruta("/documentos")
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.nombre, "documentos")
        self.assertEqual(nodo.tipo, "carpeta")
    
    def test_crear_archivo_con_contenido(self):
        self.arbol.crear_nodo("notas.txt", "archivo", "/", "Contenido de prueba")
        nodo = self.arbol.buscar_por_ruta("/notas.txt")
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.contenido, "Contenido de prueba")
    
    def test_busqueda_rutas(self):
        self.arbol.crear_nodo("carpeta1", "carpeta", "/")
        self.arbol.crear_nodo("archivo1", "archivo", "/carpeta1")
        
        nodo = self.arbol.buscar_por_ruta("/carpeta1/archivo1")
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.nombre, "archivo1")
    
    def test_mover_nodo(self):
        self.arbol.crear_nodo("carpeta1", "carpeta", "/")
        self.arbol.crear_nodo("carpeta2", "carpeta", "/")
        self.arbol.crear_nodo("archivo1", "archivo", "/carpeta1")
        
        resultado = self.arbol.mover_nodo("/carpeta1/archivo1", "/carpeta2")
        self.assertTrue(resultado)
        
        nodo = self.arbol.buscar_por_ruta("/carpeta2/archivo1")
        self.assertIsNotNone(nodo)
    
    def test_eliminar_nodo(self):
        self.arbol.crear_nodo("archivo1", "archivo", "/", "contenido")
        
        resultado = self.arbol.eliminar_nodo("/archivo1")
        self.assertTrue(resultado)
        self.assertEqual(len(self.arbol.papelera), 1)
        
        nodo = self.arbol.buscar_por_ruta("/archivo1")
        self.assertIsNone(nodo)
    
    def test_renombrar_nodo(self):
        self.arbol.crear_nodo("viejo.txt", "archivo", "/")
        
        resultado = self.arbol.renombrar_nodo("/viejo.txt", "nuevo.txt")
        self.assertTrue(resultado)
        
        nodo = self.arbol.buscar_por_ruta("/nuevo.txt")
        self.assertIsNotNone(nodo)
    
    def test_recorrido_preorden(self):
        self.arbol.crear_nodo("carpeta1", "carpeta", "/")
        self.arbol.crear_nodo("archivo1", "archivo", "/carpeta1")
        
        recorrido = self.arbol.recorrido_preorden()
        self.assertEqual(len(recorrido), 3)  # root + carpeta1 + archivo1
    
    def test_estadisticas(self):
        self.arbol.crear_nodo("carpeta1", "carpeta", "/")
        self.arbol.crear_nodo("archivo1", "archivo", "/", "12345")
        
        stats = self.arbol.estadisticas()
        self.assertEqual(stats["total_nodos"], 3)  # root + carpeta1 + archivo1
        self.assertEqual(stats["archivos"], 1)
        self.assertEqual(stats["bytes_contenido"], 5)

class TestPersistencia(unittest.TestCase):
    # Pruebas para la persistencia
    
    def setUp(self):
        self.archivo_test = "test_datos.json"
        self.persistencia = Persistencia(self.archivo_test)
    
    def tearDown(self):
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)
    
    def test_guardar_y_cargar(self):
        arbol = Arbol()
        arbol.crear_raiz()
        arbol.crear_nodo("carpeta1", "carpeta", "/")
        arbol.crear_nodo("archivo1", "archivo", "/carpeta1", "test")
        
        # Guardar
        resultado = self.persistencia.guardar_automatico(arbol)
        self.assertTrue(resultado)
        
        # Cargar
        arbol_cargado = self.persistencia.cargar()
        self.assertIsNotNone(arbol_cargado.raiz)
        
        # Verificar que se cargo correctamente
        nodo = arbol_cargado.buscar_por_ruta("/carpeta1/archivo1")
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.contenido, "test")
    
    def test_exportar_preorden(self):
        arbol = Arbol()
        arbol.crear_raiz()
        arbol.crear_nodo("carpeta1", "carpeta", "/")
        
        archivo_export = "test_export.txt"
        resultado = self.persistencia.exportar_preorden(arbol, archivo_export)
        
        self.assertTrue(resultado)
        self.assertTrue(os.path.exists(archivo_export))
        
        # Limpiar
        if os.path.exists(archivo_export):
            os.remove(archivo_export)
            
class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
    
    def test_insertar_y_buscar(self):
        self.trie.insertar("documento", "id1")
        self.trie.insertar("docencia", "id2")
        self.trie.insertar("doctor", "id3")
        
        resultados = self.trie.buscar_prefijo("doc")
        self.assertEqual(len(resultados), 3)
        
        resultados = self.trie.buscar_prefijo("doct")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["id_nodo"], "id3")
    
    def test_buscar_exacto(self):
        self.trie.insertar("notas.txt", "id1")
        self.trie.insertar("notas.txt", "id2")
        
        ids = self.trie.buscar_exacto("notas.txt")
        self.assertEqual(len(ids), 2)
        self.assertIn("id1", ids)
        self.assertIn("id2", ids)
    
    def test_eliminar(self):
        self.trie.insertar("archivo.txt", "id1")
        
        resultado = self.trie.eliminar("archivo.txt", "id1")
        self.assertTrue(resultado)
        
        ids = self.trie.buscar_exacto("archivo.txt")
        self.assertEqual(len(ids), 0)
    
    def test_contar_palabras(self):
        self.assertEqual(self.trie.contar_palabras(), 0)
        
        self.trie.insertar("uno", "id1")
        self.trie.insertar("dos", "id2")
        self.trie.insertar("tres", "id3")
        
        self.assertEqual(self.trie.contar_palabras(), 3)

class TestHashMapBusqueda(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMapBusqueda()
    
    def test_insertar_y_buscar(self):
        self.hashmap.insertar("notas.txt", "id1")
        self.hashmap.insertar("notas.txt", "id2")
        
        ids = self.hashmap.buscar_exacto("notas.txt")
        self.assertEqual(len(ids), 2)
        self.assertIn("id1", ids)
        self.assertIn("id2", ids)
    
    def test_case_insensitive(self):
        self.hashmap.insertar("Archivo.txt", "id1")
        
        ids1 = self.hashmap.buscar_exacto("archivo.txt")
        ids2 = self.hashmap.buscar_exacto("ARCHIVO.TXT")
        
        self.assertEqual(len(ids1), 1)
        self.assertEqual(len(ids2), 1)
        self.assertEqual(ids1, ids2)
    
    def test_actualizar(self):
        self.hashmap.insertar("viejo.txt", "id1")
        self.hashmap.actualizar("viejo.txt", "nuevo.txt", "id1")
        
        ids_viejo = self.hashmap.buscar_exacto("viejo.txt")
        self.assertEqual(len(ids_viejo), 0)
        
        ids_nuevo = self.hashmap.buscar_exacto("nuevo.txt")
        self.assertEqual(len(ids_nuevo), 1)
        self.assertEqual(ids_nuevo[0], "id1")

class TestSistemaBusqueda(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaBusqueda()
    
    def test_indexacion_completa(self):
        self.sistema.indexar_nodo("documento.txt", "id1")
        self.sistema.indexar_nodo("imagen.jpg", "id2")
        
        resultados_trie = self.sistema.buscar_autocompletado("doc", 10)
        self.assertEqual(len(resultados_trie["resultados"]), 1)
        
        resultados_hash = self.sistema.buscar_exacta("imagen.jpg")
        self.assertEqual(len(resultados_hash["ids_nodos"]), 1)
    
    def test_eliminacion_completa(self):
        self.sistema.indexar_nodo("archivo.txt", "id1")
        
        resultado = self.sistema.eliminar_nodo("archivo.txt", "id1")
        self.assertTrue(resultado)
        
        resultados_trie = self.sistema.buscar_autocompletado("arch", 10)
        self.assertEqual(len(resultados_trie["resultados"]), 0)
        
        resultados_hash = self.sistema.buscar_exacta("archivo.txt")
        self.assertEqual(len(resultados_hash["ids_nodos"]), 0)
    
    def test_actualizacion_completa(self):
        self.sistema.indexar_nodo("viejo.txt", "id1")
        self.sistema.actualizar_nodo("viejo.txt", "nuevo.txt", "id1")
        
        resultados_viejo = self.sistema.buscar_exacta("viejo.txt")
        self.assertEqual(len(resultados_viejo["ids_nodos"]), 0)
        
        resultados_nuevo = self.sistema.buscar_exacta("nuevo.txt")
        self.assertEqual(len(resultados_nuevo["ids_nodos"]), 1)

class TestArbolConBusqueda(unittest.TestCase):
    def setUp(self):
        self.arbol = Arbol()
        self.arbol.crear_raiz()
    
    def test_crear_y_buscar(self):
        self.arbol.crear_nodo("documentos", "carpeta", "/")
        self.arbol.crear_nodo("notas.txt", "archivo", "/documentos", "Contenido")
        
        resultados = self.arbol.buscar_autocompletado("not", 10)
        self.assertEqual(len(resultados["resultados"]), 1)
        self.assertEqual(resultados["resultados"][0]["nombre"], "notas.txt")
        
        resultados_exacta = self.arbol.buscar_exacta("notas.txt")
        self.assertEqual(len(resultados_exacta["resultados"]), 1)
        self.assertEqual(resultados_exacta["resultados"][0]["nombre"], "notas.txt")
    
    def test_renombrar_y_buscar(self):
        nodo = self.arbol.crear_nodo("viejo.txt", "archivo", "/")
        self.arbol.renombrar_nodo("/viejo.txt", "nuevo.txt")
        
        resultados_viejo = self.arbol.buscar_exacta("viejo.txt")
        self.assertEqual(len(resultados_viejo["resultados"]), 0)
        
        resultados_nuevo = self.arbol.buscar_exacta("nuevo.txt")
        self.assertEqual(len(resultados_nuevo["resultados"]), 1)
        self.assertEqual(resultados_nuevo["resultados"][0]["nombre"], "nuevo.txt")
    
    def test_eliminar_y_buscar(self):
        self.arbol.crear_nodo("eliminar.txt", "archivo", "/", "Contenido")
        self.arbol.eliminar_nodo("/eliminar.txt")
        
        resultados = self.arbol.buscar_exacta("eliminar.txt")
        self.assertEqual(len(resultados["resultados"]), 0)
    
    def test_estadisticas_busqueda(self):
        self.arbol.crear_nodo("doc1.txt", "archivo", "/")
        self.arbol.crear_nodo("doc2.txt", "archivo", "/")
        self.arbol.crear_nodo("documentos", "carpeta", "/")
        
        stats = self.arbol.estadisticas()
        self.assertEqual(stats["busqueda_palabras"], 3)
        self.assertEqual(stats["busqueda_entradas"], 3)

class TestPersistenciaConBusqueda(unittest.TestCase):
    def setUp(self):
        self.archivo_test = "test_datos_busqueda.json"
        self.persistencia = Persistencia(self.archivo_test)
    
    def tearDown(self):
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)
    
    def test_guardar_y_cargar_con_busqueda(self):
        arbol = Arbol()
        arbol.crear_raiz()
        arbol.crear_nodo("documento.txt", "archivo", "/", "test")
        arbol.crear_nodo("imagen.jpg", "archivo", "/", "imagen")
        
        resultado = self.persistencia.guardar_automatico(arbol)
        self.assertTrue(resultado)
        
        arbol_cargado = self.persistencia.cargar()
        
        self.assertIsNotNone(arbol_cargado.busqueda)
        
        resultados = arbol_cargado.buscar_autocompletado("doc", 10)
        self.assertEqual(len(resultados["resultados"]), 1)
        self.assertEqual(resultados["resultados"][0]["nombre"], "documento.txt")
        
        resultados_exacta = arbol_cargado.buscar_exacta("imagen.jpg")
        self.assertEqual(len(resultados_exacta["resultados"]), 1)
        self.assertEqual(resultados_exacta["resultados"][0]["nombre"], "imagen.jpg")
        
if __name__ == "__main__":
    
    unittest.main()
    class TestPapeleraManager(unittest.TestCase):
     def setUp(self):
        self.papelera = TestPapeleraManager(capacidad_maxima=10)
    
    def test_agregar_item(self):
        resultado = self.papelera.agregar_item("id1", "archivo.txt", "archivo", "contenido", "/archivo.txt")
        self.assertTrue(resultado)
        self.assertEqual(len(self.papelera.items), 1)
    
    def test_capacidad_maxima(self):
        for i in range(15):
            self.papelera.agregar_item(f"id{i}", f"archivo{i}.txt", "archivo", "contenido", f"/archivo{i}.txt")
        
        self.assertEqual(len(self.papelera.items), 10)
    
    def test_buscar_por_nombre(self):
        self.papelera.agregar_item("id1", "notas.txt", "archivo", "contenido", "/notas.txt")
        self.papelera.agregar_item("id2", "documento.pdf", "archivo", "contenido", "/documento.pdf")
        
        resultados = self.papelera.buscar_por_nombre("nota")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].nombre, "notas.txt")
    
    def test_restaurar_item(self):
        # Necesitamos un arbol para probar restauracion
        arbol = Arbol()
        arbol.crear_raiz()
        
        self.papelera.agregar_item("id1", "archivo.txt", "archivo", "contenido", "/archivo.txt")
        
        nodo_restaurado, mensaje = self.papelera.restaurar_item(0, arbol)
        self.assertIsNotNone(nodo_restaurado)
        self.assertEqual(nodo_restaurado.nombre, "archivo.txt")
        self.assertEqual(len(self.papelera.items), 0)
    
    def test_eliminar_permanentemente(self):
        self.papelera.agregar_item("id1", "archivo.txt", "archivo", "contenido", "/archivo.txt")
        
        resultado, mensaje = self.papelera.eliminar_permanentemente(0)
        self.assertTrue(resultado)
        self.assertEqual(len(self.papelera.items), 0)
    
    def test_vaciar_papelera(self):
        for i in range(5):
            self.papelera.agregar_item(f"id{i}", f"archivo{i}.txt", "archivo", "contenido", f"/archivo{i}.txt")
        
        cantidad = self.papelera.vaciar_papelera()
        self.assertEqual(cantidad, 5)
        self.assertEqual(len(self.papelera.items), 0)

class TestManejoErrores(unittest.TestCase):
    def setUp(self):
        self.arbol = Arbol()
        self.arbol.crear_raiz()
    
    def test_eliminar_raiz(self):
        resultado, mensaje = self.arbol.eliminar_nodo("/")
        self.assertFalse(resultado)
        self.assertIn("No se puede eliminar la raiz", mensaje)
    
    def test_crear_nodo_ruta_invalida(self):
        resultado = self.arbol.crear_nodo("archivo.txt", "archivo", "/ruta/inexistente")
        self.assertIsNone(resultado)
    
    def test_mover_a_si_mismo(self):
        self.arbol.crear_nodo("carpeta1", "carpeta", "/")
        resultado = self.arbol.mover_nodo("/carpeta1", "/carpeta1")
        self.assertFalse(resultado)
    
    def test_renombrar_nombre_existente(self):
        self.arbol.crear_nodo("archivo1.txt", "archivo", "/")
        self.arbol.crear_nodo("archivo2.txt", "archivo", "/")
        
        resultado = self.arbol.renombrar_nodo("/archivo1.txt", "archivo2.txt")
        self.assertFalse(resultado)

class TestComandosNuevos(unittest.TestCase):
    def setUp(self):
        self.arbol = Arbol()
        self.arbol.crear_raiz()
    
    def test_papelera_integrada(self):
        # Crear y eliminar archivo
        self.arbol.crear_nodo("test.txt", "archivo", "/", "contenido")
        resultado, mensaje = self.arbol.eliminar_nodo("/test.txt")
        
        self.assertTrue(resultado)
        self.assertEqual(len(self.arbol.listar_papelera()), 1)
        
        # Restaurar
        nodo_restaurado, mensaje = self.arbol.restaurar_de_papelera(0)
        self.assertIsNotNone(nodo_restaurado)
        self.assertEqual(nodo_restaurado.nombre, "test.txt")
        self.assertEqual(len(self.arbol.listar_papelera()), 0)
    
    def test_busqueda_avanzada(self):
        self.arbol.crear_nodo("documentos", "carpeta", "/")
        self.arbol.crear_nodo("notas.txt", "archivo", "/documentos", "contenido1")
        self.arbol.crear_nodo("notas_viejas.txt", "archivo", "/documentos", "contenido2")
        
        # Busqueda parcial
        resultados = self.arbol.buscar_autocompletado("not", 10)
        self.assertEqual(len(resultados["resultados"]), 2)
        
        # Busqueda exacta
        resultados_exactos = self.arbol.buscar_exacta("notas.txt")
        self.assertEqual(len(resultados_exactos["resultados"]), 1)