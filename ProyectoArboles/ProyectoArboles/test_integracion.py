import unittest
import tempfile
import os
import shutil
from sistema_archivos import Arbol
from persistencia import Persistencia
from busqueda_trie import SistemaBusqueda
from papelera_manager import PapeleraManager

class TestIntegracionCompleta(unittest.TestCase):
    # Pruebas de integracion completa del sistema
    
    def setUp(self):
        # Configurar entorno de prueba
        self.test_dir = tempfile.mkdtemp()
        self.archivo_json = os.path.join(self.test_dir, "test_datos.json")
        self.persistencia = Persistencia(self.archivo_json)
    
    def tearDown(self):
        # Limpiar archivos de prueba
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_flujo_completo_creacion_busqueda(self):
        # Prueba flujo completo: crear, buscar, modificar
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear estructura compleja
        arbol.crear_nodo("documentos", "carpeta", "/")
        arbol.crear_nodo("trabajo", "carpeta", "/documentos")
        arbol.crear_nodo("personal", "carpeta", "/documentos")
        
        arbol.crear_nodo("reporte.txt", "archivo", "/documentos/trabajo", "Reporte final")
        arbol.crear_nodo("notas.txt", "archivo", "/documentos/personal", "Notas personales")
        arbol.crear_nodo("fotos", "carpeta", "/")
        arbol.crear_nodo("vacaciones.jpg", "archivo", "/fotos", "foto vacaciones")
        
        # Verificar creacion
        self.assertEqual(arbol.tamano(), 8)  # root + 7 nodos
        
        # Buscar con diferentes metodos
        resultados = arbol.buscar_exacta("reporte.txt")
        self.assertEqual(len(resultados["resultados"]), 1)
        self.assertEqual(resultados["resultados"][0]["ruta"], "/documentos/trabajo/reporte.txt")
        
        resultados = arbol.buscar_autocompletado("not", 10)
        self.assertEqual(len(resultados["resultados"]), 1)
        
        # Guardar y cargar
        self.persistencia.guardar_automatico(arbol)
        arbol_cargado = self.persistencia.cargar()
        
        # Verificar carga correcta
        self.assertEqual(arbol_cargado.tamano(), 8)
        
        # Verificar busqueda en arbol cargado
        resultados = arbol_cargado.buscar_exacta("vacaciones.jpg")
        self.assertEqual(len(resultados["resultados"]), 1)
    
    def test_flujo_completo_eliminacion_restauracion(self):
        # Prueba flujo completo: crear, eliminar, restaurar
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear archivos
        arbol.crear_nodo("importante.txt", "archivo", "/", "Contenido importante")
        arbol.crear_nodo("temporal.txt", "archivo", "/", "Contenido temporal")
        
        # Eliminar
        resultado, mensaje = arbol.eliminar_nodo("/importante.txt")
        self.assertTrue(resultado)
        
        # Verificar papelera
        items_papelera = arbol.listar_papelera()
        self.assertEqual(len(items_papelera), 1)
        self.assertEqual(items_papelera[0].nombre, "importante.txt")
        
        # Restaurar
        nodo_restaurado, mensaje = arbol.restaurar_de_papelera(0)
        self.assertIsNotNone(nodo_restaurado)
        self.assertEqual(nodo_restaurado.nombre, "importante.txt")
        
        # Verificar restauracion
        self.assertEqual(len(arbol.listar_papelera()), 0)
        nodo = arbol.buscar_por_ruta("/importante.txt")
        self.assertIsNotNone(nodo)
    
    def test_consistencia_arbol_busqueda(self):
        # Verifica consistencia entre arbol y sistema de busqueda
        arbol = Arbol()
        arbol.crear_raiz()
        
        nombres = ["alpha.txt", "beta.txt", "gamma.txt", "delta.doc", "epsilon.pdf"]
        
        # Crear archivos
        for nombre in nombres:
            arbol.crear_nodo(nombre, "archivo", "/", f"Contenido de {nombre}")
        
        # Verificar que todos estan en el sistema de busqueda
        for nombre in nombres:
            resultados = arbol.buscar_exacta(nombre)
            self.assertEqual(len(resultados["resultados"]), 1)
        
        # Eliminar algunos
        arbol.eliminar_nodo("/beta.txt")
        arbol.eliminar_nodo("/delta.doc")
        
        # Verificar que se eliminaron del sistema de busqueda
        resultados = arbol.buscar_exacta("beta.txt")
        self.assertEqual(len(resultados["resultados"]), 0)
        
        resultados = arbol.buscar_exacta("delta.doc")
        self.assertEqual(len(resultados["resultados"]), 0)
        
        # Los otros deberian seguir existiendo
        resultados = arbol.buscar_exacta("alpha.txt")
        self.assertEqual(len(resultados["resultados"]), 1)
    
    def test_persistencia_compleja(self):
        # Prueba persistencia con estructura compleja
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear estructura jerarquica compleja
        arbol.crear_nodo("nivel1", "carpeta", "/")
        arbol.crear_nodo("nivel2", "carpeta", "/nivel1")
        arbol.crear_nodo("nivel3", "carpeta", "/nivel1/nivel2")
        
        for i in range(5):
            arbol.crear_nodo(f"archivo_{i}.txt", "archivo", "/nivel1/nivel2/nivel3", f"contenido_{i}")
        
        # Eliminar algunos
        arbol.eliminar_nodo("/nivel1/nivel2/nivel3/archivo_0.txt")
        arbol.eliminar_nodo("/nivel1/nivel2/nivel3/archivo_1.txt")
        
        # Guardar
        self.persistencia.guardar_automatico(arbol)
        
        # Cargar
        arbol_cargado = self.persistencia.cargar()
        
        # Verificar estructura completa
        self.assertEqual(arbol_cargado.tamano(), 6)  # root + 3 carpetas + 3 archivos restantes
        
        # Verificar papelera cargada
        items_papelera = arbol_cargado.listar_papelera()
        self.assertEqual(len(items_papelera), 2)
        
        # Verificar busqueda cargada
        resultados = arbol_cargado.buscar_exacta("archivo_2.txt")
        self.assertEqual(len(resultados["resultados"]), 1)
    
    def test_estres_operaciones_mixtas(self):
        # Prueba de estres con operaciones mixtas
        arbol = Arbol()
        arbol.crear_raiz()
        
        operaciones_exitosas = 0
        total_operaciones = 100
        
        for i in range(total_operaciones):
            try:
                # Operaciones variadas
                if i % 4 == 0:
                    # Crear
                    arbol.crear_nodo(f"test_{i}.txt", "archivo", "/", f"data_{i}")
                    operaciones_exitosas += 1
                
                elif i % 4 == 1 and i > 0:
                    # Buscar
                    arbol.buscar_exacta(f"test_{i-1}.txt")
                    operaciones_exitosas += 1
                
                elif i % 4 == 2 and i > 1:
                    # Eliminar
                    arbol.eliminar_nodo(f"/test_{i-2}.txt")
                    operaciones_exitosas += 1
                
                elif i % 4 == 3 and i > 2:
                    # Restaurar si hay algo en papelera
                    if len(arbol.listar_papelera()) > 0:
                        arbol.restaurar_de_papelera(0)
                        operaciones_exitosas += 1
            
            except Exception:
                # Algunas operaciones pueden fallar (ej: restaurar papelera vacia)
                pass
        
        # Deberia haber completado la mayoria de operaciones
        tasa_exito = operaciones_exitosas / total_operaciones
        self.assertGreater(tasa_exito, 0.7)  # Al menos 70% de exito
        
        # El sistema deberia permanecer consistente
        tamano = arbol.tamano()
        self.assertGreater(tamano, 1)  # Al menos la raiz
        
        # Estadisticas deberian funcionar
        stats = arbol.estadisticas()
        self.assertIn("total_nodos", stats)
        self.assertIn("busqueda_palabras", stats)
    
    def test_recuperacion_errores(self):
        # Prueba recuperacion de archivo JSON corrupto
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear datos validos
        arbol.crear_nodo("valido.txt", "archivo", "/", "Datos validos")
        self.persistencia.guardar_automatico(arbol)
        
        # Corromper archivo
        with open(self.archivo_json, 'w') as f:
            f.write("{ esto no es JSON valido }")
        
        # Intentar cargar archivo corrupto
        arbol_cargado = self.persistencia.cargar()
        
        # Deberia crear un arbol nuevo (recuperacion)
        self.assertIsNotNone(arbol_cargado.raiz)
        self.assertEqual(arbol_cargado.tamano(), 1)  # Solo la raiz
        
        # Deberia poder seguir funcionando
        arbol_cargado.crear_nodo("nuevo.txt", "archivo", "/", "Nuevos datos")
        self.assertEqual(arbol_cargado.tamano(), 2)

class TestCasosLimite(unittest.TestCase):
    # Pruebas de casos limite y condiciones de borde
    
    def test_rutas_extremas(self):
        # Prueba rutas muy largas y complejas
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Ruta con muchos niveles
        ruta = ""
        for i in range(10):
            carpeta = f"carpeta_{i}"
            arbol.crear_nodo(carpeta, "carpeta", ruta if ruta else "/")
            ruta = f"{ruta}/{carpeta}" if ruta else f"/{carpeta}"
        
        # Verificar acceso a ruta profunda
        nodo = arbol.buscar_por_ruta(ruta)
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.tipo, "carpeta")
        
        # Ruta con caracteres especiales
        arbol.crear_nodo("archivo-con-guiones.txt", "archivo", "/", "contenido")
        arbol.crear_nodo("archivo.con.puntos.txt", "archivo", "/", "contenido")
        arbol.crear_nodo("archivo_con_guiones_bajones.txt", "archivo", "/", "contenido")
        
        # Verificar busqueda de nombres especiales
        resultados = arbol.buscar_exacta("archivo-con-guiones.txt")
        self.assertEqual(len(resultados["resultados"]), 1)
        
        resultados = arbol.buscar_exacta("archivo.con.puntos.txt")
        self.assertEqual(len(resultados["resultados"]), 1)
    
    def test_nombres_limite(self):
        # Prueba nombres en los limites
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Nombre muy largo
        nombre_largo = "a" * 255  # Maximo comun en sistemas de archivos
        resultado = arbol.crear_nodo(nombre_largo, "archivo", "/", "contenido")
        self.assertIsNotNone(resultado)
        
        # Nombre vacio (deberia fallar)
        resultado = arbol.crear_nodo("", "archivo", "/", "contenido")
        self.assertIsNone(resultado)
        
        # Nombre con solo espacios
        resultado = arbol.crear_nodo("   ", "archivo", "/", "contenido")
        self.assertIsNone(resultado)
        
        # Nombre con caracteres de control
        resultado = arbol.crear_nodo("archivo\nnuevalinea.txt", "archivo", "/", "contenido")
        self.assertIsNone(resultado)
    
    def test_contenido_limite(self):
        # Prueba contenido en los limites
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Contenido muy grande
        contenido_grande = "x" * 100000  # 100KB
        resultado = arbol.crear_nodo("grande.txt", "archivo", "/", contenido_grande)
        self.assertIsNotNone(resultado)
        
        if resultado:
            self.assertEqual(len(resultado.contenido), 100000)
        
        # Contenido vacio (deberia funcionar)
        resultado = arbol.crear_nodo("vacio.txt", "archivo", "/", "")
        self.assertIsNotNone(resultado)
        
        if resultado:
            self.assertEqual(len(resultado.contenido), 0)
        
        # Contenido con caracteres especiales
        contenido_especial = "Línea 1\nLínea 2\tcon tabulación\nLínea 3 con \\barra\\"
        resultado = arbol.crear_nodo("especial.txt", "archivo", "/", contenido_especial)
        self.assertIsNotNone(resultado)
    
    def test_operaciones_invalidas(self):
        # Prueba operaciones que deberian fallar elegantemente
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Mover a si mismo
        arbol.crear_nodo("carpeta", "carpeta", "/")
        resultado = arbol.mover_nodo("/carpeta", "/carpeta")
        self.assertFalse(resultado)
        
        # Mover a descendiente
        arbol.crear_nodo("subcarpeta", "carpeta", "/carpeta")
        resultado = arbol.mover_nodo("/carpeta", "/carpeta/subcarpeta")
        self.assertFalse(resultado)
        
        # Renombrar a nombre existente
        arbol.crear_nodo("archivo1.txt", "archivo", "/")
        arbol.crear_nodo("archivo2.txt", "archivo", "/")
        resultado = arbol.renombrar_nodo("/archivo1.txt", "archivo2.txt")
        self.assertFalse(resultado)
        
        # Eliminar raiz
        resultado, mensaje = arbol.eliminar_nodo("/")
        self.assertFalse(resultado)
        self.assertIn("No se puede eliminar la raiz", mensaje)
        
        # Restaurar indice invalido
        nodo, mensaje = arbol.restaurar_de_papelera(999)
        self.assertIsNone(nodo)
        self.assertIn("Indice fuera de rango", mensaje)
    
    def test_estado_consistente_tras_errores(self):
        # Verifica que el sistema permanece consistente tras errores
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear algunos datos validos
        arbol.crear_nodo("valido1.txt", "archivo", "/", "datos1")
        arbol.crear_nodo("valido2.txt", "archivo", "/", "datos2")
        
        estado_inicial = arbol.tamano()
        
        # Intentar operaciones que fallaran
        try:
            arbol.crear_nodo("", "archivo", "/ruta/inexistente", "datos")
        except:
            pass
        
        try:
            arbol.mover_nodo("/no_existe", "/")
        except:
            pass
        
        try:
            arbol.renombrar_nodo("/no_existe", "nuevo_nombre")
        except:
            pass
        
        # El sistema deberia permanecer consistente
        estado_final = arbol.tamano()
        self.assertEqual(estado_inicial, estado_final)
        
        # Los datos originales deberian seguir accesibles
        resultados = arbol.buscar_exacta("valido1.txt")
        self.assertEqual(len(resultados["resultados"]), 1)
        
        resultados = arbol.buscar_exacta("valido2.txt")
        self.assertEqual(len(resultados["resultados"]), 1)

class TestPerformance(unittest.TestCase):
    # Pruebas de rendimiento
    
    def test_creacion_rapida(self):
        # Prueba creacion rapida de muchos nodos
        arbol = Arbol()
        arbol.crear_raiz()
        
        import time
        inicio = time.time()
        
        num_nodos = 1000
        for i in range(num_nodos):
            arbol.crear_nodo(f"test_{i}.txt", "archivo", "/", f"data_{i}")
        
        fin = time.time()
        tiempo_total = fin - inicio
        
        # Verificar que se crearon todos
        self.assertEqual(arbol.tamano(), num_nodos + 1)  # +1 por la raiz
        
        # Tiempo aceptable (ajustar segun hardware)
        tiempo_maximo = 2.0  # 2 segundos para 1000 nodos
        self.assertLess(tiempo_total, tiempo_maximo)
        
        print(f"  Creacion de {num_nodos} nodos en {tiempo_total:.3f}s")
        print(f"  Velocidad: {num_nodos/tiempo_total:.1f} nodos/segundo")
    
    def test_busqueda_rapida(self):
        # Prueba busqueda rapida en muchos nodos
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear muchos nodos
        num_nodos = 500
        for i in range(num_nodos):
            arbol.crear_nodo(f"archivo_{i:04d}.txt", "archivo", "/", f"data_{i}")
        
        import time
        
        # Busqueda exacta
        inicio = time.time()
        for i in range(100):
            nombre = f"archivo_{i:04d}.txt"
            resultados = arbol.buscar_exacta(nombre)
            self.assertEqual(len(resultados["resultados"]), 1)
        fin = time.time()
        
        tiempo_exacta = fin - inicio
        print(f"  100 busquedas exactas en {tiempo_exacta:.3f}s")
        print(f"  Velocidad: {100/tiempo_exacta:.1f} busquedas/segundo")
        
        # Busqueda por prefijo
        inicio = time.time()
        for prefijo in ["arc", "file", "test", "doc"]:
            resultados = arbol.buscar_autocompletado(prefijo, 10)
        fin = time.time()
        
        tiempo_prefijo = fin - inicio
        print(f"  4 busquedas por prefijo en {tiempo_prefijo:.3f}s")
        
        # Tiempo aceptable
        self.assertLess(tiempo_exacta, 0.5)  # 0.5 segundos para 100 busquedas
    
    def test_memoria_eficiente(self):
        # Verifica uso eficiente de memoria
        arbol = Arbol()
        arbol.crear_raiz()
        
        # Crear muchos nodos con contenido
        num_nodos = 1000
        tamaño_contenido = 100  # bytes por archivo
        
        for i in range(num_nodos):
            contenido = "x" * tamaño_contenido
            arbol.crear_nodo(f"mem_test_{i}.txt", "archivo", "/", contenido)
        
        # Verificar tamaño
        tamano_total = arbol.tamano()
        self.assertEqual(tamano_total, num_nodos + 1)
        
        # Estadisticas de busqueda deberian ser correctas
        stats = arbol.estadisticas()
        self.assertEqual(stats["total_nodos"], tamano_total)
        self.assertEqual(stats["archivos"], num_nodos)
        
        # La papelera deberia estar vacia
        items_papelera = len(arbol.listar_papelera())
        self.assertEqual(items_papelera, 0)

if __name__ == "__main__":
    # Ejecutar pruebas especificas
    print("Ejecutando pruebas de integracion y casos limite...")
    
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    
    suite = loader.loadTestsFromTestCase(TestIntegracionCompleta)
    suite.addTests(loader.loadTestsFromTestCase(TestCasosLimite))
    suite.addTests(loader.loadTestsFromTestCase(TestPerformance))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Mostrar resumen
    print("\n" + "=" * 70)
    print("RESUMEN DE PRUEBAS DE INTEGRACION")
    print("=" * 70)
    print(f"Pruebas ejecutadas: {resultado.testsRun}")
    print(f"Fallos: {len(resultado.failures)}")
    print(f"Errores: {len(resultado.errors)}")
    
    if resultado.wasSuccessful():
        print("TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    else:
        print("ALGUNAS PRUEBAS FALLARON")
    
    print("=" * 70)