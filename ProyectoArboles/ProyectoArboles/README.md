# PROYECTO 1: SIMULADOR DE CMD CON ARBOLES

## Descripcion
Simulador de linea de comandos que implementa un sistema de archivos jerarquico basado en arboles. El sistema permite crear, mover, renombrar y eliminar archivos y carpetas, con persistencia automatica en archivo JSON.

## Caracteristicas Implementadas (Dia 1-4)

### Estructuras de datos:
- Arbol general con nodos (carpetas/archivos)
- Persistencia automatica en archivo JSON
- Papelera temporal para eliminaciones

### Comandos implementados:
1. **mkdir** - Crear nueva carpeta
2. **touch** - Crear nuevo archivo
3. **ls / dir** - Listar contenido de directorio
4. **cd** - Cambiar directorio actual
5. **pwd** - Mostrar ruta completa
6. **mv** - Mover archivo/carpeta
7. **rm** - Eliminar archivo/carpeta
8. **rename** - Renombrar archivo/carpeta
9. **export preorden** - Exportar recorrido en preorden
10. **tree** - Mostrar arbol de directorios
11. **stats** - Mostrar estadisticas del sistema
12. **clear / cls** - Limpiar pantalla
13. **history** - Mostrar historial de comandos
14. **help / ?** - Mostrar ayuda
15. **exit / quit** - Salir del programa

## Instalacion y Ejecucion

### Requisitos:
- Python 3.6 o superior
- No se requieren librerias externas

### Ejecucion:
```bash
# Clonar o descargar los archivos
# Ejecutar el simulador
python cmd_simulator.py
## AVANCES DIA 7-9: INTERFAZ COMPLETA Y MANEJO DE ERRORES

### Nuevas Caracteristicas Implementadas:

#### 1. Sistema de Papelera Mejorado:
- **Papelera de reciclaje** con capacidad configurable
- **Restauracion** de archivos eliminados
- **Busqueda** dentro de la papelera
- **Eliminacion permanente** selectiva
- **Limpieza automatica** de items antiguos
- **Estadisticas** de uso de papelera

#### 2. Nuevos Comandos:
- `trash` - Listar contenido de papelera
- `trash stats` - Estadisticas de papelera
- `trash search <nombre>` - Buscar en papelera
- `restore <numero>` - Restaurar desde papelera
- `purge <numero>` - Eliminar permanentemente
- `emptytrash` - Vaciar papelera completa
- `whereis <nombre>` - Buscar en todo el sistema
- `type <archivo>` - Mostrar contenido de archivo
- `cat <archivo>` - Alias de type (Unix)
- `copy <origen> <destino>` - Copiar archivos/carpetas
- `cp <origen> <destino>` - Alias de copy
- `info [ruta]` - Informacion detallada de nodo
- `path` - Mostrar variable PATH
- `echo <texto>` - Mostrar texto/variables

#### 3. Mejoras de Interfaz:
- **Autocompletado** de comandos con TAB
- **Historial** navegable con flechas
- **Mensajes de error** formateados y descriptivos
- **Banner** de bienvenida mejorado
- **Ayuda contextual** organizada por categorias
- **Prompt** con ruta actual visualmente clara

#### 4. Manejo Robusto de Errores:
- **Validacion** de rutas y parametros
- **Mensajes de error** especificos y utiles
- **Manejo de excepciones** controlado
- **Sugerencias** cuando fallan operaciones
- **Modo debug** opcional con traceback

### Comandos de Papelera - Ejemplos:
## AVANCES DIA 10-11: PRUEBAS DE INTEGRACION Y PERFORMANCE

### Nuevas Caracteristicas Implementadas:

#### 1. Sistema Completo de Pruebas:
- **Pruebas de integracion** completa del sistema
- **Casos limite** y condiciones de borde
- **Pruebas de stress** con miles de operaciones
- **Pruebas de consistencia** entre arbol y busqueda
- **Pruebas de recuperacion** de errores

#### 2. Sistema de Benchmark:
- **benchmark.py** - Pruebas de rendimiento automatizadas
- **Medicion de tiempos** de operaciones
- **Uso de memoria** y eficiencia
- **Pruebas escalables** (100 a 10,000 nodos)
- **Resultados detallados** en archivo de texto

#### 3. Scripts de Prueba Automatizados:
- **run_tests.py** - Script principal para ejecutar todas las pruebas
- **test_integracion.py** - Pruebas de integracion completas
- **Comando benchmark** integrado en el CMD

#### 4. Mejoras de Performance:
- **Optimizacion de busqueda** en arboles grandes
- **Manejo eficiente de memoria**
- **Validacion de limites** de rendimiento
- **Tolerancia a fallos** y recuperacion

### Archivos Nuevos Día 10-11:

1. **benchmark.py** - Sistema de pruebas de rendimiento
2. **test_integracion.py** - Pruebas de integracion completa
3. **run_tests.py** - Script para ejecutar todas las pruebas

### Comandos Nuevos:
