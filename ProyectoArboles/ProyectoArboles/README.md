# PROYECTO 1: SIMULADOR DE CMD CON ARBOLES

## Descripcion
Simulador completo de linea de comandos que implementa un sistema de archivos jerarquico basado en arboles generales. Desarrollado para la materia de Estructuras de Datos.

## Caracteristicas Principales

### Sistema de Archivos Jerarquico
- Arbol general con nodos para carpetas y archivos
- Persistencia en formato JSON
- Operaciones CRUD completas
- Recorridos en preorden para exportacion

### Sistema Avanzado de Busqueda
- Trie para autocompletado de nombres por prefijo
- HashMap para busqueda exacta case-insensitive
- Indexacion de todos los nodos creados
- Sincronizacion con operaciones del arbol

### Papelera de Reciclaje Avanzada
- Capacidad configurable (default: 100 items)
- Retencion temporal (30 dias)
- Restauracion inteligente con deteccion de conflictos
- Limpieza automatica de items antiguos
- Busqueda dentro de la papelera

### Interfaz de Consola Profesional
- Comandos tipo Windows
- Autocompletado con TAB
- Historial navegable
- Manejo robusto de errores
- Validacion de rutas y parametros

## Estructura del Proyecto
proyecto_arboles/
    
    cmd_simulator.py        # Interfaz principal de linea de comandos
    sistema_archivos.py     # Implementacion del arbol general
    persistencia.py         # Guardado y carga en JSON
    busqueda_trie.py        # Trie y HashMap para busqueda
    papelera_manager.py     # Gestion de papelera de reciclaje

    tests.py                # Pruebas unitarias completas
    test_integracion.py     # Pruebas de integracion
    benchmark.py            # Pruebas de rendimiento
    run_tests.py            # Script para ejecutar pruebas

    datos.json              # Archivo de persistencia
    README.md               # Esta documentacion


## Instalacion y Requisitos

### Requisitos del Sistema
- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS
- Sin dependencias externas obligatorias

### Instalacion
bash
# 1. Clonar o descargar el proyecto
git clone <repositorio>
cd proyecto_arboles

# 2. (Opcional) Instalar dependencias para funcionalidades extra
pip install pyreadline3    # Autocompletado mejorado en Windows
pip install psutil         # Para pruebas de memoria


# Ejecuion
## Modo iterativo
bash
python cmd_simulator.py

## Ejecutar todas las Pruebas
bash
python run_tests.py --todo

## Ejecutar Benchmark de Rendimiento
bash
python cmd_simulator.py
C:\> benchmark


## Comandos disponibles
### Sistema de archivos
bash
Comando                     Descripcion                 Ejemplo
-------------------------------------------------------------------------------
mkdir <nombre>	            Crear nueva carpeta	        mkdir documentos
touch <nombre> [contenido]	Crear archivo	            touch notas.txt "Hola mundo"
ls [ruta]	                Listar contenido	        ls /documentos
cd <ruta>	                Cambiar directorio	        cd documentos
pwd	                        Mostrar ruta actual	        pwd
cp <origen> <destino>	    Copiar archivo/carpeta	    cp archivo.txt backup/
mv <origen> <destino>	    Mover o renombrar	        mv viejo.txt nuevo.txt
rm <ruta>	                Eliminar (a papelera)	    rm archivo.txt
rename <viejo> <nuevo>	    Renombrar	                rename viejo.txt nuevo.txt

### Busqueda y Contenido
bash
Comando	                    Descripcion	                Ejemplo
-------------------------------------------------------------------------------
search <prefijo>	        Buscar por autocompletado	search doc
find <nombre>	            Busqueda exacta	find        notas.txt
whereis <nombre>	        Buscar en todo el sistema	whereis config.ini
type <archivo>	            Mostrar contenido	        type /documentos/notas.txt
cat <archivo>	            Alias de type	            cat archivo.txt

### Papelera de Reciclaje
bash
Comando	                    Descripcion	                Ejemplo
-------------------------------------------------------------------------------
trash	                    Listar cont. de papelera    trash
trash stats	                Estadisticas de papelera	trash stats
trash search <nombre>	    Buscar en papelera	trash   search documento
restore <numero>	        Restaurar desde papelera	restore 0
purge <numero>	            Eliminar permanentemente	purge 0
emptytrash	                Vaciar papelera	            emptytrash

### Informacion y Utilidades
bash
Comando	                    Descripcion	                Ejemplo
-------------------------------------------------------------------------------
tree [ruta]	                Mostrar arbol directorios   tree /
info [ruta]	                Informacion detallada	    info /documentos
stats	                    Estadisticas del sistema	stats
export preorden [archivo]	Exportar recorrido	        export preorden recorrido.txt
history	                    Mostrar historial	        history
help o ?	                Mostrar ayuda	            help


## Ejemplos 1 de uso
bash
#Crear estructura de archivos
C:\> mkdir documentos
C:\> cd documentos
C:\documentos> mkdir personal
C:\documentos> mkdir trabajo
C:\documentos> touch notas.txt "Notas importantes"
C:\documentos> cp notas.txt backup.txt
C:\documentos> ls
[DIR]   personal
[DIR]   trabajo
[FILE]  notas.txt      (18 bytes)
[FILE]  backup.txt     (18 bytes)

## Ejemplo 2 Busqueda avanzada
bash
C:\> search doc
Encontrados: 3
Mostrando: 3

1. [DIR] documentos -> /documentos
2. [FILE] documento1.txt -> /documento1.txt
3. [FILE] doc_especial.pdf -> /documentos/doc_especial.pdf

C:\> find notas.txt
Encontrados: 1

1. [FILE] notas.txt -> /documentos/notas.txt
    Contenido: Notas importantes

## Ejemplo 3: Manejo de Papelera
bash
C:\> rm /documentos/notas.txt
C:\> trash

C:\> restore 0
Item restaurado exitosamente: notas.txt

## Ejecutar suite completa de pruebas
### Todas las pruebas
bash
python run_tests.py --todo

### Solo pruebas unitarias
bash
python run_tests.py --unitarias

### Solo pruebas de integracion
bash
python run_tests.py --integracion

### Solo benchmark
bash
python run_tests.py --benchmark


## Componentes Principales
- *Arbol (sistema_archivos.py)*
    Gestiona la jerarquia de nodos
    Implementa operaciones CRUD
    Mantiene diccionario para busqueda rapida por ID
- *SistemaBusqueda (busqueda_trie.py)*
    Trie para autocompletado por prefijo
    HashMap para busqueda exacta
    Sincronizacion automatica con el arbol
- *PapeleraManager (papelera_manager.py)*
    Gestion de items eliminados
    Restauracion con verificacion
    Limpieza automatica por antiguedad
- *Persistencia (persistencia.py)*
    Serializacion/deserializacion JSON
    Exportacion de recorridos
    Recuperacion de errores


# Documentacion Tecnica del Proyecto
## 1. Sistema de Archivos (sistema_archivos.py)
### Clase nodo
bash
class Nodo:
    """
    Representa un elemento en el sistema de archivos.
    
    Atributos:
        id (str): Identificador unico del nodo
        nombre (str): Nombre del archivo/carpeta
        tipo (str): 'carpeta' o 'archivo'
        contenido (str): Contenido del archivo (vacio para carpetas)
        hijos (List[Nodo]): Lista de nodos hijos
        padre (Nodo): Referencia al nodo padre
    
    Metodos principales:
        agregar_hijo(hijo): Anade un nodo hijo
        eliminar_hijo(hijo): Elimina un hijo
        obtener_ruta(): Devuelve ruta completa desde raiz
        to_dict(): Serializa a diccionario para JSON
    """

### Clase arbol
bash
class Arbol:
    """
    Gestiona la jerarquia completa del sistema de archivos.
    
    Componentes:
        - raiz (Nodo): Nodo raiz del sistema
        - nodos (Dict[str, Nodo]): Diccionario para busqueda rapida por ID
        - papelera (PapeleraManager): Gestor de papelera
        - busqueda (SistemaBusqueda): Sistema de indices para busqueda
    
    Operaciones principales:
        - Crear, eliminar, mover y renombrar nodos
        - Busquedas por ruta y por ID
        - Recorridos y estadisticas
        - Integracion con papelera y sistema de busqueda
    """

### 2.- Clases de sistemas de busqueda
bash
class Trie:
    """
    Implementacion de arbol Trie para busqueda por prefijo.
    Complejidades:
        - Insercion: O(n) donde n = longitud del nombre
        - Busqueda por prefijo: O(n + k) donde k = numero de resultados
        - Eliminacion: O(n)
    """

class HashMapBusqueda:
    """
    HashMap para busqueda exacta case-insensitive.
    Usa nombres en minuscula como clave.
    Complejidades:
        - Insercion: O(1)
        - Busqueda: O(1)
        - Eliminacion: O(1)
    """

class SistemaBusqueda:
    """
    Integra Trie y HashMap manteniendo sincronizacion.
    Garantiza consistencia entre ambos indices.
    """

## 3.- Persistencia
bash
{
  "raiz": {
    "id": "abc123",
    "nombre": "root",
    "tipo": "carpeta",
    "contenido": "",
    "hijos": [
      {
        "id": "def456",
        "nombre": "documentos",
        "tipo": "carpeta",
        "contenido": "",
        "hijos": []
      }
    ]
  },
  "papelera": {
    "items": [],
    "capacidad_maxima": 100,
    "dias_retencion": 30
  },
  "busqueda": {
    "trie": {...},
    "hashmap": {...}
  }
}

### 4.- Papelera (papelera_manager.py)
bash
def limpiar_automaticamente(self):
    """
    Elimina items con mas de dias_retencion dias.
    Recorre la papelera en orden inverso para evitar
    problemas de indices al eliminar.
    """
    ahora = datetime.now()
    eliminados = 0
    
    for i in range(len(self.items) - 1, -1, -1):
        item = self.items[i]
        dias_pasados = (ahora - item.fecha_eliminacion).days
        
        if dias_pasados > self.dias_retencion:
            self.items.pop(i)
            eliminados += 1
    
    return eliminados

## Flujos de Datos
### Creacion de nodo
1. Usuario: mkdir documentos
2. CMD_Simulator: Valida ruta y parametros
3. Arbol.crear_nodo(): 
   - Busca padre en ruta "/"
   - Crea nuevo Nodo con ID unico
   - Agrega a hijos del padre
4. SistemaBusqueda.indexar_nodo():
   - Trie.insertar("documentos", id)
   - HashMap.insertar("documentos", id)
5. Persistencia.guardar_automatico():
   - Serializa arbol completo a JSON

### Busqueda por prefijo
1. Usuario: search doc
2. Arbol.buscar_autocompletado("doc", 10):
   - SistemaBusqueda.buscar_autocompletado("doc")
   - Trie.buscar_prefijo("doc") → [{"palabra": "documento", "id_nodo": "id1"}, ...]
   - Enriquecer con datos del nodo
3. Mostrar resultados formateados

## Estrategia de Pruebas
### Pruebas unitarias
bash
class TestSistemaArchivos(unittest.TestCase):
    # Prueba cada componente de forma aislada
    def test_crear_carpeta_raiz(self):
        self.arbol.crear_nodo("documentos", "carpeta", "/")
        nodo = self.arbol.buscar_por_ruta("/documentos")
        self.assertIsNotNone(nodo)

### Pruebas de integracion
bash
class TestIntegracionCompleta(unittest.TestCase):
    # Prueba flujos completos entre componentes
    def test_flujo_completo_creacion_busqueda(self):
        # Crear estructura
        # Realizar busquedas
        # Verificar consistencia

### Pruebas de rendimiento
bash
class Benchmark:
    # Evalua rendimiento con cargas grandes
    def prueba_insercion_masiva(self, num_nodos=1000):
        # Mide tiempos y memoria

# Guia de Usuario - Simulador de CMD
## Iniciar programa
bash
    python cmd_simulator.py

## comando basico de ayuda
    C:\> help

## Conceptos Basicos
### Rutas
Ruta absoluta: Comienza con / (ej: /documentos/trabajo)

Ruta relativa: Relativa al directorio actual (ej: trabajo/informe.txt)

.. Directorio padre

. Directorio actual

/ Raiz del sistema

### Tipos de Elementos
Carpetas ([DIR]): Contenedores que pueden tener hijos
Archivos ([FILE]): Contienen texto, no pueden tener hijos


## Tutorial Paso a Paso
### 1. Crear una Estructura Basica
#Crear carpetas principales
bash
C:\> mkdir documentos
C:\> mkdir imagenes
C:\> mkdir musica

#Navegar a documentos
C:\> cd documentos

#Crear subcarpetas
C:\documentos> mkdir personal
C:\documentos> mkdir trabajo

#Crear archivos
C:\documentos> touch notas.txt "Mis notas importantes"
C:\documentos> touch lista.txt "Compras: pan, leche, huevos"

### 2. Explorar el sistema
bash
#Ver donde estas
C:\documentos> pwd
Ruta: /documentos

#Listar contenido
C:\documentos> ls
[DIR]   personal
[DIR]   trabajo
[FILE]  notas.txt      (24 bytes)
[FILE]  lista.txt      (24 bytes)

#Ver estructura completa
C:\documentos> tree
documentos/
├── personal/
├── trabajo/
├── notas.txt
└── lista.txt

### 3. Buscar archivo
bash
 #Buscar por prefijo (autocompletado)
C:\> search not
Encontrados: 1
Mostrando: 1

1. [FILE] notas.txt -> /documentos/notas.txt

#Busqueda exacta
C:\> find lista.txt
Encontrados: 1

1. [FILE] lista.txt -> /documentos/lista.txt
    Contenido: Compras: pan, leche, huevos

#Buscar en todo el sistema
C:\> whereis notas
Busqueda exacta para: 'notas'
-------------------------------------------
[FILE] notas.txt
    Ruta: /documentos/notas.txt
    Tamaño: 24 bytes


### 4. Ver informacion del sistema
bash
#Estadisticas generales
C:\> stats
--- ESTADISTICAS DEL SISTEMA ---
Nodos totales: 8
Carpetas: 4
Archivos: 4
Bytes de contenido: 96
Altura del arbol: 3
Elementos en papelera: 0

#Informacion detallada de un elemento
C:\> info /documentos
INFORMACION DETALLADA
--------------------------------------------------
Nombre: documentos
Tipo: CARPETA
Ruta completa: /documentos
ID unico: abc123
Hijos directos: 4
Es raiz: No
Es hoja: No
Padre: root

## Especificaciones del programa

### Requerimientos basicos
- Modelo de nodo con id, nombre, tipo, contenido, children
- Persistencia en archivo JSON
- Operaciones: crear, mover, renombrar, eliminar con papelera
- Listar hijos y mostrar ruta completa
- Exportar recorrido en preorden
- Trie para autocompletado
- Busqueda exacta con HashMap
- Interfaz consola con comandos tipo mkdir, touch, mv, rm, search, export
- Pruebas de insercion, eliminacion, busqueda y consistencia

### Caracteristicas extras plementadas
- Papelera de reciclaje avanzada
- Sistema de benchmark integrado
- Autocompletado con TAB
- Historial de comandos
- Manejo robusto de errores
- Pruebas de integracion completas
- Documentacion profesional


## INTEGRANTES
- Carranza Ibarra Vanya Lucia
- Sandoval Ramirez Emily Guadalupe