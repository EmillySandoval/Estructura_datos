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