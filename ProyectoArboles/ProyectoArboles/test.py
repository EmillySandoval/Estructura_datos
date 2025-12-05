import unittest
import os
from sistema_archivos import Arbol
from persistencia import Persistencia

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

if __name__ == "__main__":
    unittest.main()