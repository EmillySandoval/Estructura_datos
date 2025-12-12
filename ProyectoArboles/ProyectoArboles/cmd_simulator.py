import os
import sys
import readline  # Para autocompletado y historial
import traceback  # Para manejo de errores detallado
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
        self.comandos_autocompletar = [  # NUEVO: Lista para autocompletado
            "mkdir", "touch", "ls", "dir", "cd", "pwd", "mv", "rm",
            "rename", "search", "find", "export", "tree", "stats",
            "clear", "cls", "history", "help", "?", "exit", "quit",
            "trash", "restore", "emptytrash", "purge", "whereis",
            "type", "cat", "copy", "cp", "info", "path", "echo","benchmark"
        ]
        self.setup_autocompletado()  # NUEVO: Configurar autocompletado
    
    
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
        
        try:
            # Diccionario de comandos para mejor organizacion
            comandos = {
                "exit": self.salir,
                "quit": self.salir,
                "help": self.mostrar_ayuda,
                "?": self.mostrar_ayuda,
                "mkdir": lambda: self.comando_mkdir(args),
                "touch": lambda: self.comando_touch(args),
                "ls": lambda: self.comando_ls(args),
                "dir": lambda: self.comando_ls(args),
                "pwd": lambda: self.comando_pwd(args),
                "cd": lambda: self.comando_cd(args),
                "mv": lambda: self.comando_mv(args),
                "rm": lambda: self.comando_rm(args),
                "rename": lambda: self.comando_rename(args),
                "export": lambda: self.comando_export(args),
                "stats": lambda: self.comando_stats(args),
                "clear": lambda: self.comando_clear(),
                "cls": lambda: self.comando_clear(),
                "history": lambda: self.comando_history(),
                "tree": lambda: self.comando_tree(args),
                "search": lambda: self.comando_search(args),
                "find": lambda: self.comando_find(args),
                "test-trie": lambda: self.comando_test_trie(args),
                "trash": lambda: self.comando_trash(args),  # NUEVO
                "restore": lambda: self.comando_restore(args),  # NUEVO
                "emptytrash": lambda: self.comando_emptytrash(args),  # NUEVO
                "purge": lambda: self.comando_purge(args),  # NUEVO
                "whereis": lambda: self.comando_whereis(args),  # NUEVO
                "type": lambda: self.comando_type(args),  # NUEVO
                "cat": lambda: self.comando_cat(args),  # NUEVO
                "copy": lambda: self.comando_copy(args),  # NUEVO
                "cp": lambda: self.comando_copy(args),  # NUEVO
                "info": lambda: self.comando_info(args),  # NUEVO
                "path": lambda: self.comando_path(args),  # NUEVO
                "echo": lambda: self.comando_echo(args),  # NUEVO
                 "benchmark": lambda: self.comando_benchmark(args),  # NUEVO
            }
            
            if cmd in comandos:
                comandos[cmd]()
            else:
                print(self.formatear_error(f"Comando no reconocido: '{cmd}'. Escribe 'help' para ver comandos disponibles."))
                
        except Exception as e:
            self.manejar_excepcion(e, f"ejecutar comando '{cmd}'")
    
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
        
    def comando_trash(self, args):
        # Muestra el contenido de la papelera
        if len(args) == 0:
            # Listar toda la papelera
            items = self.arbol.listar_papelera()
            
            if not items:
                print("La papelera esta vacia.")
                return
            
            print("\n   PAPELERA DE RECICLAJE")
            print("   " + "-" * 70)
            print("   #  Tipo       Nombre                         Ruta Original              Fecha")
            print("   " + "-" * 70)
            
            for i, item in enumerate(items):
                tipo = "DIR " if item.tipo == "carpeta" else "FILE"
                nombre = item.nombre[:30] + "..." if len(item.nombre) > 30 else item.nombre.ljust(30)
                ruta = item.ruta_original[:30] + "..." if len(item.ruta_original) > 30 else item.ruta_original.ljust(30)
                fecha = item.fecha_eliminacion.strftime("%Y-%m-%d %H:%M")
                
                print(f"   {i:2}  {tipo}    {nombre}  {ruta}  {fecha}")
            
            print("   " + "-" * 70)
            print(f"   Total: {len(items)} items")
            
        elif args[0] == "stats":
            # Estadisticas de la papelera
            stats = self.arbol.estadisticas_papelera()
            
            print("\n   ESTADISTICAS DE LA PAPELERA")
            print("   " + "-" * 40)
            print(f"   Items totales: {stats['total_items']}")
            print(f"   Tamaño total: {stats['tamano_bytes']} bytes")
            print(f"   Capacidad utilizada: {stats['capacidad_utilizada']}")
            
            if stats['tipos']:
                print("\n   Distribucion por tipo:")
                for tipo, cantidad in stats['tipos'].items():
                    print(f"     {tipo}: {cantidad}")
            
            print("   " + "-" * 40)
            
        elif args[0] == "search" and len(args) > 1:
            # Buscar en la papelera
            criterio = args[1]
            items = self.arbol.buscar_en_papelera(criterio, "nombre")
            
            if not items:
                print(f"No se encontraron items con '{criterio}' en la papelera.")
                return
            
            print(f"\n   Resultados de busqueda: '{criterio}'")
            print("   " + "-" * 60)
            
            for i, item in enumerate(items):
                tipo = "DIR " if item.tipo == "carpeta" else "FILE"
                print(f"   {i:2}  {tipo}  {item.nombre} -> {item.ruta_original}")
            
            print("   " + "-" * 60)
            
        else:
            print("Uso: trash                          (listar papelera)")
            print("     trash stats                    (estadisticas)")
            print("     trash search <nombre>          (buscar en papelera)")
    
    def comando_restore(self, args):
        # Restaura un item desde la papelera
        if len(args) < 1:
            print("Uso: restore <numero>")
            print("     restore 0  (restaura el primer item de la papelera)")
            print("\nUsa 'trash' primero para ver los numeros de los items.")
            return
        
        try:
            indice = int(args[0])
            resultado, mensaje = self.arbol.restaurar_de_papelera(indice)
            
            if resultado:
                print(f"Item restaurado exitosamente: {resultado.nombre}")
                self.persistencia.guardar_automatico(self.arbol)
            else:
                print(f"No se pudo restaurar: {mensaje}")
                
        except ValueError:
            print("Error: El numero debe ser un valor entero.")
        except Exception as e:
            self.manejar_excepcion(e, "restaurar item")
    
    def comando_emptytrash(self, args):
        # Vacía toda la papelera
        if args and args[0] == "-confirm":
            confirmacion = "s"
        else:
            confirmacion = input("¿Estas seguro de vaciar la papelera? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            cantidad = self.arbol.vaciar_papelera()
            print(f"Papelera vaciada. {cantidad} items eliminados permanentemente.")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print("Operacion cancelada.")
    
    def comando_purge(self, args):
        # Elimina permanentemente un item especifico de la papelera
        if len(args) < 1:
            print("Uso: purge <numero>")
            print("     purge 0  (elimina permanentemente el primer item)")
            print("\nUsa 'trash' primero para ver los numeros de los items.")
            return
        
        try:
            indice = int(args[0])
            confirmacion = input(f"¿Eliminar permanentemente el item {indice}? (s/n): ").strip().lower()
            
            if confirmacion == 's':
                resultado, mensaje = self.arbol.eliminar_permanentemente(indice)
                
                if resultado:
                    print(f"Item eliminado permanentemente: {mensaje}")
                    self.persistencia.guardar_automatico(self.arbol)
                else:
                    print(f"No se pudo eliminar: {mensaje}")
            else:
                print("Operacion cancelada.")
                
        except ValueError:
            print("Error: El numero debe ser un valor entero.")
        except Exception as e:
            self.manejar_excepcion(e, "eliminar permanentemente")
    
    def comando_whereis(self, args):
        # Busca un archivo en todo el sistema
        if len(args) < 1:
            print("Uso: whereis <nombre>")
            print("     whereis notas.txt  (busca en todo el sistema)")
            return
        
        nombre = args[0]
        
        # Busqueda exacta primero
        resultados_exactos = self.arbol.buscar_exacta(nombre)
        
        if resultados_exactos["resultados"]:
            print(f"\nBusqueda exacta para: '{nombre}'")
            print("-" * 60)
            
            for item in resultados_exactos["resultados"]:
                tipo = "[DIR]" if item["tipo"] == "carpeta" else "[FILE]"
                print(f"{tipo} {item['nombre']}")
                print(f"    Ruta: {item['ruta']}")
                if item["tipo"] == "archivo" and item["contenido"]:
                    print(f"    Tamaño: {len(item['contenido'])} bytes")
                print()
        
        # Busqueda por autocompletado
        resultados_parciales = self.arbol.buscar_autocompletado(nombre, 20)
        
        if resultados_parciales["resultados"] and resultados_parciales["total_encontrados"] > len(resultados_exactos["resultados"]):
            print(f"\nResultados parciales (que contienen '{nombre}'):")
            print("-" * 60)
            
            for item in resultados_parciales["resultados"]:
                # Evitar duplicados de busqueda exacta
                if not any(r["ruta"] == item["ruta"] for r in resultados_exactos["resultados"]):
                    tipo = "[DIR]" if item["tipo"] == "carpeta" else "[FILE]"
                    print(f"{tipo} {item['nombre']} -> {item['ruta']}")
            
            if resultados_parciales["total_encontrados"] > len(resultados_parciales["resultados"]):
                print(f"\n... y {resultados_parciales['total_encontrados'] - len(resultados_parciales['resultados'])} resultados mas.")
        
        if not resultados_exactos["resultados"] and not resultados_parciales["resultados"]:
            print(f"No se encontro '{nombre}' en el sistema.")
    
    def comando_type(self, args):
        # Muestra el contenido de un archivo
        if len(args) < 1:
            print("Uso: type <ruta_archivo>")
            print("     type /documentos/notas.txt")
            return
        
        ruta = args[0]
        nodo = self.arbol.buscar_por_ruta(ruta)
        
        if not nodo:
            print(f"Archivo no encontrado: {ruta}")
            return
        
        if nodo.tipo != "archivo":
            print(f"Error: '{ruta}' no es un archivo.")
            return
        
        print(f"\nContenido de '{ruta}':")
        print("-" * 60)
        print(nodo.contenido if nodo.contenido else "(archivo vacio)")
        print("-" * 60)
        print(f"Tamaño: {len(nodo.contenido)} bytes")
    
    def comando_cat(self, args):
        # Alias para type (comando Unix)
        self.comando_type(args)
    
    def comando_copy(self, args):
        # Copia un archivo o carpeta
        if len(args) < 2:
            print("Uso: copy <origen> <destino>")
            print("     copy notas.txt documentos/")
            print("     copy /original /backup/copia")
            return
        
        origen = args[0]
        destino = args[1]
        
        # Si origen es relativo, hacerlo absoluto
        if not origen.startswith("/"):
            if self.ruta_actual == "/":
                origen = "/" + origen
            else:
                origen = self.ruta_actual + "/" + origen
        
        nodo_origen = self.arbol.buscar_por_ruta(origen)
        if not nodo_origen:
            print(f"Error: Origen no encontrado: {origen}")
            return
        
        # Determinar nombre de copia
        if destino.endswith("/"):
            # Destino es carpeta, copiar con mismo nombre
            ruta_destino = destino
            nombre_copia = nodo_origen.nombre
        else:
            # Destino incluye nuevo nombre
            if "/" in destino:
                partes = destino.rsplit("/", 1)
                ruta_destino = partes[0] if partes[0] else "/"
                nombre_copia = partes[1]
            else:
                ruta_destino = self.ruta_actual
                nombre_copia = destino
        
        # Verificar que no exista ya
        destino_completo = f"{ruta_destino}/{nombre_copia}".replace("//", "/")
        if self.arbol.buscar_por_ruta(destino_completo):
            print(f"Error: Ya existe un item en: {destino_completo}")
            return
        
        # Crear copia
        nuevo_nodo = self.arbol.crear_nodo(
            nombre_copia,
            nodo_origen.tipo,
            ruta_destino,
            nodo_origen.contenido
        )
        
        if nuevo_nodo:
            # Si es carpeta, copiar recursivamente el contenido
            if nodo_origen.tipo == "carpeta":
                self._copiar_recursivo(nodo_origen, nuevo_nodo)
            
            print(f"Copiado: {origen} -> {destino_completo}")
            self.persistencia.guardar_automatico(self.arbol)
        else:
            print(f"Error: No se pudo copiar {origen}")
    
    def _copiar_recursivo(self, origen, destino):
        # Copia recursiva de carpetas
        for hijo in origen.hijos:
            nuevo_hijo = self.arbol.crear_nodo(
                hijo.nombre,
                hijo.tipo,
                destino.obtener_ruta(),
                hijo.contenido
            )
            
            if nuevo_hijo and hijo.tipo == "carpeta":
                self._copiar_recursivo(hijo, nuevo_hijo)
    
    def comando_info(self, args):
        # Muestra informacion detallada de un nodo
        if len(args) < 1:
            ruta = self.ruta_actual
        else:
            ruta = args[0]
        
        nodo = self.arbol.buscar_por_ruta(ruta)
        
        if not nodo:
            print(f"Error: Nodo no encontrado: {ruta}")
            return
        
        print(f"\nINFORMACION DETALLADA")
        print("-" * 50)
        print(f"Nombre: {nodo.nombre}")
        print(f"Tipo: {'CARPETA' if nodo.tipo == 'carpeta' else 'ARCHIVO'}")
        print(f"Ruta completa: {nodo.obtener_ruta()}")
        print(f"ID unico: {nodo.id}")
        
        if nodo.tipo == "archivo":
            print(f"Tamaño: {len(nodo.contenido)} bytes")
            print(f"Lineas: {len(nodo.contenido.splitlines())}")
        
        print(f"Hijos directos: {len(nodo.hijos)}")
        print(f"Es raiz: {'Si' if nodo.es_raiz() else 'No'}")
        print(f"Es hoja: {'Si' if nodo.es_hoja() else 'No'}")
        
        if nodo.padre:
            print(f"Padre: {nodo.padre.nombre}")
        
        print("-" * 50)
    
    def comando_path(self, args):
        # Muestra o cambia la variable PATH (simulada)
        if len(args) == 0:
            print("PATH actual: /;./")
            print("(En este simulador, PATH siempre incluye / y directorio actual)")
        else:
            print("Nota: En este simulador, PATH no es configurable.")
    
    def comando_echo(self, args):
        # Muestra texto o variables
        if len(args) == 0:
            return
        
        texto = " ".join(args)
        
        # Variables especiales
        if texto == "$PATH":
            print("/;./")
        elif texto == "$PWD":
            print(self.ruta_actual)
        elif texto.startswith("$"):
            print("(Variable no definida)")
        else:
            print(texto)
        
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
        # Muestra la ayuda con todos los comandos disponibles
        print("\n" + "=" * 70)
        print("SISTEMA DE ARCHIVOS JERARQUICO - SIMULADOR CMD")
        print("=" * 70)
        print("COMANDOS DISPONIBLES (Dia 7-9)")
        print("-" * 70)
        
        categorias = {
            "Sistema de archivos": [
                 ("benchmark", "Pruebas de rendimiento"),  
                ("mkdir <nombre>", "Crear nueva carpeta"),
                ("touch <nombre> [contenido]", "Crear archivo"),
                ("ls [ruta]", "Listar contenido"),
                ("cd <ruta>", "Cambiar directorio"),
                ("pwd", "Mostrar ruta actual"),
                ("cp <origen> <destino>", "Copiar archivo/carpeta"),
                ("mv <origen> <destino>", "Mover/renombrar"),
                ("rm <ruta>", "Eliminar (a papelera)"),
                ("rename <viejo> <nuevo>", "Renombrar"),
            ],
            "Busqueda y contenido": [
                ("search <prefijo>", "Buscar con autocompletado"),
                ("find <nombre>", "Busqueda exacta"),
                ("whereis <nombre>", "Buscar en todo el sistema"),
                ("type <archivo>", "Mostrar contenido"),
                ("cat <archivo>", "Alias de type"),
            ],
            "Papelera de reciclaje": [
                ("trash", "Mostrar contenido de papelera"),
                ("trash stats", "Estadisticas de papelera"),
                ("trash search <nombre>", "Buscar en papelera"),
                ("restore <numero>", "Restaurar de papelera"),
                ("purge <numero>", "Eliminar permanentemente"),
                ("emptytrash", "Vaciar papelera"),
            ],
            "Informacion y utilidades": [
                ("tree [ruta]", "Mostrar arbol de directorios"),
                ("info [ruta]", "Informacion detallada"),
                ("stats", "Estadisticas del sistema"),
                ("export preorden [archivo]", "Exportar recorrido"),
                ("path", "Mostrar variable PATH"),
                ("echo <texto>", "Mostrar texto/variables"),
            ],
            "Sistema y ayuda": [
                ("clear / cls", "Limpiar pantalla"),
                ("history", "Mostrar historial"),
                ("help / ?", "Mostrar esta ayuda"),
                ("test-trie", "Probar sistema de busqueda"),
                ("exit / quit", "Salir del programa"),
            ]
        }
        
        for categoria, comandos in categorias.items():
            print(f"\n{categoria}:")
            print("-" * 40)
            for comando, descripcion in comandos:
                print(f"  {comando:25} - {descripcion}")
        
        print("\n" + "=" * 70)
        print("TIPS:")
        print("  - Usa TAB para autocompletar comandos")
        print("  - Usa flechas arriba/abajo para navegar historial")
        print("  - Los archivos eliminados van a la papelera")
        print("  - Usa 'emptytrash -confirm' para evitar confirmacion")
        print("=" * 70)
    def salir(self):
        # Guarda y sale del programa
        print("Guardando datos...")
        self.persistencia.guardar_automatico(self.arbol)
        print("Saliendo del simulador CMD. ¡Hasta luego!")
        self.ejecutando = False
    
    def iniciar(self):
        # Inicia el simulador de linea de comandos
        self.mostrar_banner()
        
        # Limpieza automatica de papelera
        eliminados = self.arbol.limpiar_papelera_automatico()
        if eliminados > 0:
            print(self.formatear_error(f"Se limpiaron {eliminados} items antiguos de la papelera automaticamente.", "INFO"))
        
        print(self.formatear_error("Escribe 'help' para ver comandos disponibles", "INFO"))
        print(self.formatear_error("Escribe 'exit' para salir", "INFO"))
        print("")
        
        while self.ejecutando:
            try:
                # Mostrar prompt con ruta actual
                prompt = self.mostrar_prompt()
                entrada = input(prompt)
                
                if entrada.strip():
                    self.ejecutar_comando(entrada)
                    
            except KeyboardInterrupt:
                print("\n" + self.formatear_error("Interrumpido por usuario.", "ADVERTENCIA"))
                print(self.formatear_error("Use 'exit' para salir correctamente.", "INFO"))
            except EOFError:
                print("\n")
                self.salir()
            except Exception as e:
                self.manejar_excepcion(e, "bucle principal")
def main():
    # Funcion principal
    simulador = CMD_Simulator()
    simulador.iniciar()

if __name__ == "__main__":
    main()
    def comando_benchmark(self, args):
        # Ejecuta pruebas de rendimiento
        print("\n[INFO] Iniciando pruebas de rendimiento...")
        print("[INFO] Esto puede tomar varios segundos/minutos")
        print("[INFO] Presiona Ctrl+C para cancelar")
        
        try:
            # Importar y ejecutar benchmark
            from benchmark import ejecutar_benchmark
            
            # Ejecutar benchmark
            ejecutar_benchmark()
            
            print("\n[COMPLETADO] Benchmark finalizado")
            print("[INFO] Los resultados se guardaron en 'benchmark_resultados.txt'")
            
        except ImportError:
            print("[ERROR] No se encontro benchmark.py")
            print("[INFO] Asegurate de que el archivo benchmark.py este en la carpeta")
        except KeyboardInterrupt:
            print("\n[INFO] Benchmark cancelado por el usuario")
        except Exception as e:
            print(f"[ERROR] Error ejecutando benchmark: {e}")