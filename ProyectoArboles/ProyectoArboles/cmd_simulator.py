import os
import sys
from pathlib import Path

# Añadir el directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))

from sistema_archivos import Arbol
from persistencia import Persistencia

class CMD_Simulator:
    # Simulador de linea de comandos tipo CMD/Unix
    
    def __init__(self):
        self.persistencia = Persistencia()
        self.arbol = self.persistencia.cargar()
        
        # Crear raiz si no existe
        if not self.arbol.raiz:
            self.arbol.crear_raiz()
            self.persistencia.guardar_automatico(self.arbol)
        
        self.ruta_actual = "/"
        self.historial = []
        self.ejecutando = True
    
    def mostrar_prompt(self):
        # Muestra el prompt con la ruta actual
        if self.ruta_actual == "/":
            prompt = "C:\\> "
        else:
            ruta_windows = self.ruta_actual.replace('/', '\\')
            prompt = f"C:{ruta_windows}> "
        return prompt
    
    def ejecutar_comando(self, comando):
        # Ejecuta un comando ingresado por el usuario
        partes = comando.strip().split()
        if not partes:
            return
        
        cmd = partes[0].lower()
        args = partes[1:]
        
        self.historial.append(comando)
        
        if cmd == "exit" or cmd == "quit":
            self.salir()
        elif cmd == "help" or cmd == "?":
            self.mostrar_ayuda()
        elif cmd == "mkdir":
            self.comando_mkdir(args)
        elif cmd == "touch":
            self.comando_touch(args)
        elif cmd == "ls" or cmd == "dir":
            self.comando_ls(args)
        elif cmd == "pwd":
            self.comando_pwd(args)
        elif cmd == "cd":
            self.comando_cd(args)
        elif cmd == "mv":
            self.comando_mv(args)
        elif cmd == "rm":
            self.comando_rm(args)
        elif cmd == "rename":
            self.comando_rename(args)
        elif cmd == "export":
            self.comando_export(args)
        elif cmd == "stats":
            self.comando_stats(args)
        elif cmd == "clear" or cmd == "cls":
            self.comando_clear()
        elif cmd == "history":
            self.comando_history()
        elif cmd == "tree":
            self.comando_tree(args)
        elif cmd == "search":  # NUEVO: comando de busqueda
            self.comando_search(args)
        elif cmd == "find":    # NUEVO: alias para busqueda exacta
            self.comando_find(args)
        elif cmd == "test-trie":  # NUEVO: comando de prueba del Trie
            self.comando_test_trie(args)
        else:
            print(f"Comando no reconocido: '{cmd}'. Escribe 'help' para ver comandos disponibles.")
    
    def comando_mkdir(self, args):
        # Crea una nueva carpeta
        if len(args) < 1:
            print("Uso: mkdir <nombre_carpeta>")
            print("     mkdir <ruta>/<nombre_carpeta>")
            return
        
        ruta_completa = args[0]
        
        # Determinar ruta del padre y nombre
        if "/" in ruta_completa:
            partes = ruta_completa.rsplit("/", 1)
            ruta_padre = partes[0] if partes[0] else "/"
            nombre = partes[1]
        else:
            ruta_padre = self.ruta_actual
            nombre = ruta_completa
        
        resultado = self.arbol.crear_nodo(nombre, "carpeta", ruta_padre)
        
        if resultado:
            print(f"Directorio creado: {nombre}")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print(f"Error: No se pudo crear el directorio '{nombre}'")
    
    def comando_touch(self, args):
        # Crea un nuevo archivo
        if len(args) < 1:
            print("Uso: touch <nombre_archivo> [contenido]")
            print("     touch <ruta>/<nombre_archivo> [contenido]")
            return
        
        ruta_completa = args[0]
        contenido = " ".join(args[1:]) if len(args) > 1 else ""
        
        # Determinar ruta del padre y nombre
        if "/" in ruta_completa:
            partes = ruta_completa.rsplit("/", 1)
            ruta_padre = partes[0] if partes[0] else "/"
            nombre = partes[1]
        else:
            ruta_padre = self.ruta_actual
            nombre = ruta_completa
        
        resultado = self.arbol.crear_nodo(nombre, "archivo", ruta_padre, contenido)
        
        if resultado:
            print(f"Archivo creado: {nombre}")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print(f"Error: No se pudo crear el archivo '{nombre}'")
    
    def comando_ls(self, args):
        # Lista el contenido del directorio actual o especificado
        ruta = args[0] if args else self.ruta_actual
        
        contenido = self.arbol.listar_hijos(ruta)
        
        if contenido is None:
            print(f"Error: Ruta no encontrada: {ruta}")
            return
        
        if not contenido:
            print("El directorio esta vacio")
            return
        
        print(f"\nContenido de {ruta}:")
        print("-" * 40)
        for item in contenido:
            tipo = "[DIR]" if item["tipo"] == "carpeta" else "[FILE]"
            nombre = item["nombre"]
            tamano = f"{item['tamano']} bytes" if item["tipo"] == "archivo" else ""
            print(f"{tipo}\t{nombre}\t{tamano}")
        print(f"\nTotal: {len(contenido)} elementos")
    
    def comando_pwd(self, args):
        # Muestra la ruta actual completa
        ruta = args[0] if args else self.ruta_actual
        ruta_completa = self.arbol.obtener_ruta_completa(ruta)
        
        if ruta_completa:
            print(f"Ruta: {ruta_completa}")
        else:
            print(f"Error: Ruta no valida")
    
    def comando_cd(self, args):
        # Cambia el directorio actual
        if len(args) < 1:
            print("Uso: cd <ruta>")
            print("     cd ..   (directorio padre)")
            print("     cd /    (raiz)")
            return
        
        nueva_ruta = args[0]
        
        if nueva_ruta == "/":
            self.ruta_actual = "/"
        elif nueva_ruta == "..":
            # Ir al padre
            if self.ruta_actual == "/":
                print("Ya estas en la raiz")
                return
            
            partes = self.ruta_actual.strip("/").split("/")
            if len(partes) > 1:
                self.ruta_actual = "/" + "/".join(partes[:-1])
            else:
                self.ruta_actual = "/"
        else:
            # Verificar si la ruta existe
            if nueva_ruta.startswith("/"):
                ruta_absoluta = nueva_ruta
            else:
                if self.ruta_actual == "/":
                    ruta_absoluta = "/" + nueva_ruta
                else:
                    ruta_absoluta = self.ruta_actual + "/" + nueva_ruta
            
            nodo = self.arbol.buscar_por_ruta(ruta_absoluta)
            if nodo and nodo.tipo == "carpeta":
                self.ruta_actual = ruta_absoluta
            else:
                print(f"Error: Directorio no encontrado: {nueva_ruta}")
    
    def comando_mv(self, args):
        # Mueve un nodo a otra ubicacion
        if len(args) < 2:
            print("Uso: mv <origen> <destino>")
            print("     mv <archivo> <directorio_destino>")
            return
        
        origen = args[0]
        destino = args[1]
        
        # Si origen es relativo, hacerlo absoluto
        if not origen.startswith("/"):
            if self.ruta_actual == "/":
                origen = "/" + origen
            else:
                origen = self.ruta_actual + "/" + origen
        
        resultado = self.arbol.mover_nodo(origen, destino)
        
        if resultado:
            print(f"Movido: {origen} -> {destino}")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print(f"Error: No se pudo mover {origen} a {destino}")
    
    def comando_rm(self, args):
        # Elimina un nodo (lo envia a la papelera)
        if len(args) < 1:
            print("Uso: rm <ruta>")
            print("     rm <archivo_o_carpeta>")
            return
        
        ruta = args[0]
        
        # Si la ruta es relativa, hacerla absoluta
        if not ruta.startswith("/"):
            if self.ruta_actual == "/":
                ruta = "/" + ruta
            else:
                ruta = self.ruta_actual + "/" + ruta
        
        confirmacion = input(f"¿Eliminar '{ruta}'? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("Operacion cancelada")
            return
        
        resultado = self.arbol.eliminar_nodo(ruta)
        
        if resultado:
            print(f"Eliminado: {ruta} (enviado a papelera)")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print(f"Error: No se pudo eliminar {ruta}")
    
    def comando_rename(self, args):
        # Renombra un nodo
        if len(args) < 2:
            print("Uso: rename <ruta_actual> <nuevo_nombre>")
            return
        
        ruta_actual = args[0]
        nuevo_nombre = args[1]
        
        # Si la ruta es relativa, hacerla absoluta
        if not ruta_actual.startswith("/"):
            if self.ruta_actual == "/":
                ruta_actual = "/" + ruta_actual
            else:
                ruta_actual = self.ruta_actual + "/" + ruta_actual
        
        resultado = self.arbol.renombrar_nodo(ruta_actual, nuevo_nombre)
        
        if resultado:
            print(f"Renombrado: {ruta_actual} -> {nuevo_nombre}")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print(f"Error: No se pudo renombrar {ruta_actual}")
    
    def comando_export(self, args):
        # Exporta recorrido en preorden
        if len(args) > 0 and args[0] == "preorden":
            archivo_salida = args[1] if len(args) > 1 else "preorden.txt"
            
            resultado = self.persistencia.exportar_preorden(self.arbol, archivo_salida)
            
            if resultado:
                print(f"Recorrido en preorden exportado a: {archivo_salida}")
            else:
                print("Error al exportar el recorrido")
        else:
            print("Uso: export preorden [archivo_salida]")
            print("     export preorden mi_arbol.txt")
    
    def comando_stats(self, args):
        # Muestra estadisticas del sistema
        stats = self.arbol.estadisticas()
        
        print("\n=== ESTADISTICAS DEL SISTEMA ===")
        print(f"Nodos totales: {stats['total_nodos']}")
        print(f"Carpetas: {stats['carpetas']}")
        print(f"Archivos: {stats['archivos']}")
        print(f"Bytes de contenido: {stats['bytes_contenido']}")
        print(f"Altura del arbol: {stats['altura']}")
        print(f"Elementos en papelera: {stats['papelera']}")
        print("=" * 30)
    
    def comando_clear(self):
        # Limpia la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def comando_history(self):
        # Muestra el historial de comandos
        print("\n=== HISTORIAL DE COMANDOS ===")
        for i, cmd in enumerate(self.historial[-20:], 1):
            print(f"{i:3}. {cmd}")
        print("=" * 30)
    
    def comando_tree(self, args):
        # Muestra el arbol de directorios
        ruta = args[0] if args else self.ruta_actual
        
        def comando_search(self, args):
         if len(args) < 1:
            print("Uso: search <prefijo> [max_resultados]")
            print("     search doc  (busca nombres que empiecen con 'doc')")
            print("     search doc 5  (maximo 5 resultados)")
            return
        
        prefijo = args[0]
        max_resultados = int(args[1]) if len(args) > 1 else 10
        
        print(f"\nBuscando nombres que empiecen con: '{prefijo}'")
        print("-" * 50)
        
        resultados = self.arbol.buscar_autocompletado(prefijo, max_resultados)
        
        if resultados["resultados"]:
            print(f"Encontrados: {resultados['total_encontrados']}")
            print(f"Mostrando: {resultados['mostrando']}\n")
            
            for i, item in enumerate(resultados["resultados"], 1):
                tipo = "[DIR]" if item["tipo"] == "carpeta" else "[FILE]"
                print(f"{i:2}. {tipo} {item['nombre']}")
                print(f"    Ruta: {item['ruta']}")
                print()
        else:
            print("No se encontraron resultados.")
        
        print("-" * 50)
    
    def comando_find(self, args):
        if len(args) < 1:
            print("Uso: find <nombre_exacto>")
            print("     find notas.txt  (busca exactamente 'notas.txt')")
            return
        
        nombre = args[0]
        
        print(f"\nBuscando nombre exacto: '{nombre}'")
        print("-" * 50)
        
        resultados = self.arbol.buscar_exacta(nombre)
        
        if resultados["resultados"]:
            print(f"Encontrados: {resultados['total_encontrados']}\n")
            
            for i, item in enumerate(resultados["resultados"], 1):
                tipo = "[DIR]" if item["tipo"] == "carpeta" else "[FILE]"
                print(f"{i:2}. {tipo} {item['nombre']}")
                print(f"    Ruta: {item['ruta']}")
                
                if item["tipo"] == "archivo" and item["contenido"]:
                    contenido_preview = item["contenido"][:50]
                    print(f"    Contenido: {contenido_preview}")
                    if len(item["contenido"]) > 50:
                        print("             ...")
                print()
        else:
            print("No se encontraron resultados.")
        
        print("-" * 50)
    
    def comando_test_trie(self, args):
        print("\n=== PRUEBA DEL SISTEMA DE BUSQUEDA ===")
        
        if self.arbol.tamano() < 5:
            print("Creando datos de prueba...")
            self.arbol.crear_nodo("documento1.txt", "archivo", "/", "Contenido 1")
            self.arbol.crear_nodo("documento2.txt", "archivo", "/", "Contenido 2")
            self.arbol.crear_nodo("documentos", "carpeta", "/")
            self.arbol.crear_nodo("doc_especial.pdf", "archivo", "/documentos", "PDF especial")
            self.arbol.crear_nodo("imagen.jpg", "archivo", "/", "Imagen JPEG")
        
        stats = self.arbol.busqueda.estadisticas()
        print(f"Palabras en Trie: {stats['total_palabras_trie']}")
        print(f"Entradas en HashMap: {stats['total_entradas_hashmap']}")
        
        print("\nProbando autocompletado con prefijo 'doc':")
        resultados = self.arbol.buscar_autocompletado("doc", 10)
        print(f"Encontrados: {resultados['total_encontrados']}")
        
        for item in resultados["resultados"]:
            tipo = "[DIR]" if item["tipo"] == "carpeta" else "[FILE]"
            print(f"  {tipo} {item['nombre']} -> {item['ruta']}")
        
        print("\nProbando busqueda exacta 'documento1.txt':")
        resultados_exacta = self.arbol.buscar_exacta("documento1.txt")
        print(f"Encontrados: {resultados_exacta['total_encontrados']}")
        
        print("\n=== FIN DE PRUEBA ===")
        
        def mostrar_arbol_rec(nodo, nivel=0, prefijo=""):
            if nivel == 0:
                print(f"{nodo.nombre}/")
            
            for i, hijo in enumerate(nodo.hijos):
                es_ultimo = (i == len(nodo.hijos) - 1)
                nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
                
                if hijo.tipo == "carpeta":
                    print(f"{prefijo}{'└── ' if es_ultimo else '├── '}{hijo.nombre}/")
                    mostrar_arbol_rec(hijo, nivel + 1, nuevo_prefijo)
                else:
                    print(f"{prefijo}{'└── ' if es_ultimo else '├── '}{hijo.nombre}")
        
        nodo = self.arbol.raiz
        if nodo and nodo.tipo == "carpeta":
            mostrar_arbol_rec(nodo)
        else:
            print("Error: No hay carpeta raiz en el arbol")
    
    def mostrar_ayuda(self):
        print("\n=== COMANDOS DISPONIBLES ===")
        print("Sistema de archivos jerarquico - Simulador CMD")
        print("=" * 50)
        
        comandos = [
            ("mkdir <nombre>", "Crear nueva carpeta"),
            ("touch <nombre> [contenido]", "Crear nuevo archivo"),
            ("ls [ruta]", "Listar contenido de directorio"),
            ("dir [ruta]", "Alias de ls"),
            ("cd <ruta>", "Cambiar directorio actual"),
            ("pwd [ruta]", "Mostrar ruta completa"),
            ("mv <origen> <destino>", "Mover archivo/carpeta"),
            ("rm <ruta>", "Eliminar archivo/carpeta (papelera)"),
            ("rename <ruta> <nuevo_nombre>", "Renombrar archivo/carpeta"),
            ("search <prefijo> [max]", "Buscar con autocompletado"),  # NUEVO
            ("find <nombre_exacto>", "Busqueda exacta"),  # NUEVO
            ("export preorden [archivo]", "Exportar recorrido preorden"),
            ("tree [ruta]", "Mostrar arbol de directorios"),
            ("stats", "Mostrar estadisticas del sistema"),
            ("test-trie", "Probar sistema de busqueda"),  # NUEVO
            ("clear / cls", "Limpiar pantalla"),
            ("history", "Mostrar historial de comandos"),
            ("help / ?", "Mostrar esta ayuda"),
            ("exit / quit", "Salir del programa")
        ]
        
        for comando, descripcion in comandos:
            print(f"{comando:30} - {descripcion}")
        
        print("\n=== NUEVOS COMANDOS DIA 5-6 ===")  # NUEVA SECCION
        print("search <prefijo>    - Busqueda con autocompletado (Trie)")
        print("find <nombre>       - Busqueda exacta (HashMap)")
        print("test-trie           - Probar sistema de busqueda")
        print("=" * 50)
        
    def salir(self):
        # Guarda y sale del programa
        print("Guardando datos...")
        self.persistencia.guardar_automatico(self.arbol)
        print("Saliendo del simulador CMD. ¡Hasta luego!")
        self.ejecutando = False
    
    def iniciar(self):
           
        print("========================================")
        print("   SIMULADOR CMD - SISTEMA DE ARCHIVOS")
        print("========================================")
        print("DIA 5-6: Trie y Busqueda implementados")  # NUEVO
        print("========================================")
        print("Nuevos comandos: search, find, test-trie")  # NUEVO
        print("========================================")
        print("Escribe 'help' para ver comandos disponibles")
        print("Escribe 'exit' para salir")
        print("========================================\n")
        
       
        while self.ejecutando:
            try:
                entrada = input(self.mostrar_prompt())
                self.ejecutar_comando(entrada)
            except KeyboardInterrupt:
                print("\n\nInterrumpido por usuario. Use 'exit' para salir correctamente.")
            except EOFError:
                print("\n")
                self.salir()
            except Exception as e:
                print(f"Error inesperado: {e}")

def main():
    # Funcion principal
    simulador = CMD_Simulator()
    simulador.iniciar()

if __name__ == "__main__":
    main()