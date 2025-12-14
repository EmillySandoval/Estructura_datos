import subprocess
import time
import sys
import os

class DemoReal:
    def _init_(self):
        # Verificar que estamos en la carpeta correcta
        self.verificar_archivos()
        
    def verificar_archivos(self):
        """Verifica que todos los archivos del proyecto existan"""
        archivos_requeridos = [
            'cmd_simulator.py',
            'sistema_archivos.py', 
            'persistencia.py',
            'busqueda_trie.py',
            'papelera_manager.py'
        ]
        
        for archivo in archivos_requeridos:
            if not os.path.exists(archivo):
                print(f"ERROR: No se encuentra {archivo}")
                print("Asegurate de ejecutar desde la carpeta del proyecto")
                sys.exit(1)
    
    def ejecutar_comando(self, comando, esperar=2, en_simulador=False):
        """Ejecuta un comando real en el sistema"""
        print(f"\n {comando}")
        
        if en_simulador:
            # Comando que se ejecuta DENTRO del simulador
            # Necesitamos una forma de enviar comandos al proceso del simulador
            # Por ahora, mostramos lo que debería hacer el usuario manualmente
            print(f"[EJECUTA MANUALMENTE en el simulador: {comando}]")
            time.sleep(esperar)
        else:
            # Comando del sistema (bash/cmd)
            try:
                resultado = subprocess.run(
                    comando,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if resultado.stdout:
                    print(resultado.stdout)
                if resultado.stderr:
                    print(f"Error: {resultado.stderr}")
            except subprocess.TimeoutExpired:
                print("Tiempo exedido")
            except Exception as e:
                print(f"Error ejecutando comando: {e}")
            
            time.sleep(esperar)
    
    def iniciar_simulador(self):
        """Inicia el simulador en un proceso separado"""
        print("\n" + "-"*60)
        print("INICIANDO SIMULADOR DE SISTEMA DE ARCHIVOS")
        print("-"*60)
        
        # Hacer backup de datos.json
        if os.path.exists('datos.json'):
            import shutil
            shutil.copy2('datos.json', 'datos_backup_demo.json')
            print(" Backup creado: datos_backup_demo.json")
        
        # Iniciar el simulador
        self.proceso_simulador = subprocess.Popen(
            [sys.executable, 'cmd_simulator.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(2)  # Esperar a que inicie
        
        # Leer salida inicial
        try:
            salida, _ = self.proceso_simulador.communicate(timeout=1)
            print(salida[:500])  # Mostrar primeros 500 caracteres
        except:
            pass
    
    def enviar_comando_simulador(self, comando):
        """Envia un comando al simulador (no funciona bien en todos los sistemas)"""
        try:
            self.proceso_simulador.stdin.write(comando + "\n")
            self.proceso_simulador.stdin.flush()
            time.sleep(1)
            
            # Intentar leer salida
            salida = ""
            while True:
                try:
                    linea = self.proceso_simulador.stdout.readline()
                    if not linea:
                        break
                    salida += linea
                    if "C:\\>" in linea or "C:>" in linea:
                        break
                except:
                    break
            
            print(salida)
            return salida
        except:
            print(f"[Simulando comando: {comando}]")
            return ""
    
    def demo_completa(self):
        print("\n" + "-"*70)
        print("DEMOSTRACIÓN DEL PROYECTO")
        print("-"*70)
        print("Este script ejecutará comandos REALES en tu sistema")
        print("-"*70)
        
        input("\nPresiona ENTER para comenzar...")
        
        # 1. LIMPIAR Y PREPARAR
        print("\n1. PREPARANDO DEMOSTRACIÓN...")
        self.ejecutar_comando("clear" if os.name != 'nt' else "cls", 1)
        
        # 2. EJECUTAR PRUEBAS RÁPIDAS (antes de empezar)
        print("\n2. VERIFICANDO SISTEMA...")
        self.ejecutar_comando(f"{sys.executable} run_tests.py --verificar", 2)
        
        # 3. INICIAR SIMULADOR
        print("\n3. INICIANDO SIMULADOR...")
        print("Abre una NUEVA terminal y ejecuta:")
        print(f"   {sys.executable} cmd_simulator.py")
        print("\nLuego vuelve a esta ventana y presiona ENTER...")
        input()
        
        # GUIA DE COMANDOS A EJECUTAR EN EL SIMULADOR
        print("\n4. EJECUTA ESTOS COMANDOS en el simulador (una terminal aparte):")
        print("-" * 60)
        
        comandos_demo = [
            ("mkdir ProyectoDemo", "Crear carpeta principal"),
            ("cd ProyectoDemo", "Entrar a la carpeta"),
            ("mkdir src docs tests", "Crear subcarpetas"),
            ("touch README.md '# Proyecto Demo'", "Crear README"),
            ("touch main.py 'print(\"Hola Mundo\")'", "Crear archivo Python"),
            ("tree", "Ver estructura completa"),
            ("ls", "Listar contenido"),
            ("cd /", "Volver a raíz"),
            ("mkdir Documentos", "Crear carpeta para búsqueda"),
            ("cd Documentos", "Entrar a Documentos"),
            ("touch archivo1.txt 'Contenido 1'", "Crear archivo 1"),
            ("touch archivo2.txt 'Contenido 2'", "Crear archivo 2"),
            ("touch documento.pdf 'PDF demo'", "Crear PDF"),
            ("search arc", "Buscar por prefijo 'arc'"),
            ("find archivo1.txt", "Búsqueda exacta"),
            ("whereis doc", "Buscar en todo el sistema"),
            ("rm /Documentos/archivo1.txt", "Eliminar archivo"),
            ("trash", "Ver papelera"),
            ("restore 0", "Restaurar archivo"),
            ("trash stats", "Estadísticas de papelera"),
            ("stats", "Estadísticas del sistema"),
            ("info /ProyectoDemo", "Información detallada"),
            ("export preorden demo_estructura.txt", "Exportar estructura"),
            ("exit", "Salir del simulador")
        ]
        
        for comando, descripcion in comandos_demo:
            print(f"\n{descripcion}:")
            print(f"   {comando}")
            input("   Presiona ENTER para continuar...")
        
        # 5. EJECUTAR PRUEBAS DESPUÉS DE LA DEMO
        print("\n5. EJECUTANDO PRUEBAS DE VALIDACIÓN...")
        self.ejecutar_comando(f"{sys.executable} run_tests.py --unitarias", 3)
        
        # 6. EJECUTAR BENCHMARK
        print("\n6. EJECUTANDO BENCHMARK...")
        self.ejecutar_comando(f"{sys.executable} benchmark.py", 5)
        
        # 7. RESTAURAR BACKUP
        print("\n7. RESTAURANDO DATOS ORIGINALES...")
        if os.path.exists('datos_backup_demo.json'):
            import shutil
            shutil.copy2('datos_backup_demo.json', 'datos.json')
            print(" Datos originales restaurados")
        
    
    def demo_rapida(self):
        """Versión rápida para practicar"""
        print("\nDEMOSTRACIÓN RAPIDA")
        print("-" * 40)
        
        pasos = [
            ("Iniciar simulador", f"{sys.executable} cmd_simulator.py"),
            ("[En simulador] Crear estructura", "mkdir Demo && cd Demo"),
            ("[En simulador] Crear archivos", "touch test1.txt test2.txt"),
            ("[En simulador] Buscar", "search test"),
            ("[En simulador] Ver stats", "stats"),
            ("[En simulador] Salir", "exit"),
            ("Ejecutar pruebas", f"{sys.executable} run_tests.py --unitarias")
        ]
        
        for desc, cmd in pasos:
            print(f"\n{desc}:")
            print(f"   {cmd}")
            if "[En simulador]" not in desc:
                ejecutar = input("   ¿Ejecutar? (s/n): ")
                if ejecutar.lower() == 's':
                    self.ejecutar_comando(cmd, 1)

def main():

    print("DEMOSTRADOR DEL PROYECTO")
    print("-" * 40)
    print("\nOpciones:")
    print("1. Demostración COMPLETA")
    print("2. Demostración RAPIDA")
    print("3. Guia de comandos")
    print("4. Salir")
    
    opcion = input("\nSelecciona (1-4): ").strip()
    
    demo = DemoReal()
    
    if opcion == "1":
        demo.demo_completa()
    elif opcion == "2":
        demo.demo_rapida()
    elif opcion == "3":
        mostrar_guia_comandos()
    else:
        print("Saliendo...")

def mostrar_guia_comandos():

    print("\n" + "-"*70)
    print("GUÍA DE COMANDOS")
    print("-"*70)
    print("\nEJECUTA EN ESTE ORDEN:")
    
    guia = """
        1. INICIAR:
        python cmd_simulator.py

        2. CREAR ESTRUCTURA BÁSICA:
        mkdir MiProyecto
        cd MiProyecto
        mkdir src docs tests
        touch README.md "# Mi Proyecto"
        touch main.py "print('Hola')"
        tree
        ls

        3. DEMOSTRAR BÚSQUEDA:
        cd /
        mkdir Documentos
        cd Documentos
        touch informe.txt "Informe final"
        touch presentacion.pdf "PDF"
        touch imagen.jpg "Imagen"
        search inf
        find informe.txt
        whereis pdf

        4. DEMOSTRAR PAPELERA:
        rm /Documentos/informe.txt
        trash
        restore 0
        trash stats

        5. MOSTRAR ESTADÍSTICAS:
        stats
        info /MiProyecto

        6. EXPORTAR Y SALIR:
        export preorden estructura.txt
        exit

        7. EJECUTAR PRUEBAS (fuera del simulador):
        python run_tests.py --unitarias
        python benchmark.py
    """
    
    print(guia)
    print("-"*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemostración cancelada por el usuario.")
        # Restaurar backup si existe
        if os.path.exists('datos_backup_demo.json'):
            import shutil
            shutil.copy2('datos_backup_demo.json', 'datos.json')
            print("Datos originales restaurados.")
        sys.exit(0)