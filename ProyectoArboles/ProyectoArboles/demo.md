
# PROYECTO: SIMULADOR DE SISTEMA DE ARCHIVOS CON ÁRBOLES


## INTRODUCCIÓN


### Iniciar programa
```bash
python cmd_simulator.py
```

Simulador de Sistema de Archivos con Arboles. Este proyecto implementa un sistema completo de archivos jerárquico desarrollado en Python.


- Proyecto suite con arboles


## CARACTERISTICAS PRINCIPALES

### A. Sistema de archivos básico


```bash
# Estructura basica
C:\> mkdir ProyectoFinal
C:\> cd ProyectoFinal
C:\ProyectoFinal> mkdir src
C:\ProyectoFinal> mkdir docs
C:\ProyectoFinal> mkdir tests
C:\ProyectoFinal> touch README.md "Proyecto Arboles"
C:\ProyectoFinal> touch main.py "print('Sistema de Archivos')"

# Mostrar estructura creada
C:\ProyectoFinal> tree
C:\ProyectoFinal> ls
```

Primero  implementamos comandos como mkdir, touch, ls y tree. El sistema usa un árbol general donde cada nodo puede ser carpeta o archivo.

Puntos:

- Comandos tipo Unix/Windows familiares
- Estructura jerarquica basada en árboles
- Navegación completa por rutas

### B. Persistencia automatica


```bash
# Mostrar que los datos persisten
C:\ProyectoFinal> exit

# Reiniciar el programa
python cmd_simulator.py

# Verificar que la estructura se mantiene
C:\> ls
C:\> cd ProyectoFinal
C:\ProyectoFinal> ls
C:\ProyectoFinal> type README.md
```

Todos los cambios se guardan en un archivo JSON. Al reiniciar el programa, toda la estructura se recupera automáticamente sin pérdida de datos.


## SISTEMA AVANZADO DE BUSQUEDA

### A. Busqueda por prefijo usando Trie 

```bash
# Crear archivos con nombres similares
C:\> mkdir Documentos
C:\> cd Documentos
C:\Documentos> touch documento1.txt "Informe trimestral"
C:\Documentos> touch documento2.txt "Presentacion ejecutiva"
C:\Documentos> touch documentacion.pdf "Manual de usuario"
C:\Documentos> touch doc_backup.zip "Respaldo"

# Demostrar busqueda por prefijo
C:\Documentos> search doc

# Mostrar resultados con autocompletado
```

Para busquedas eficientes se implemento un árbol Trie. Esto permite busqueda por prefijo en tiempo O(m + k), donde m es la longitud del prefijo y k el número de resultados. Es extremadamente rapido incluso con miles de archivos.


### B. Busqueda exacta con HashMap 


```bash
# Busqueda exacta
C:\> find documento1.txt

# Busqueda case-insensitive
C:\> find DOCUMENTO1.TXT

# Busqueda en todo el sistema
C:\> whereis doc

# Ver contenido encontrado
C:\> type /Documentos/documento1.txt
```


Combinamos el Trie con unHashMap para busquedas exactas en tiempo O(1). El sistema es case-insensitive y puede buscar en toda la jerarquia. Esta combinación nos da autocompletado rapido y búsqueda exacta instantanea.

Puntos a destacar:

- HashMap para busqueda O(1)
- Case-insensitive por diseño
- Integración perfecta entre ambas estructuras


## PAPELERA DE RECICLAJE 

### A. Eliminación y restauración inteligente


```bash
# Eliminar un archivo importante
C:\> rm /Documentos/documento1.txt
¿Eliminar '/Documentos/documento1.txt'? (s/n): s

# Verificar que desaparecio
C:\> ls /Documentos

# Examinar la papelera
C:\> trash

# Restaurar el archivo
C:\> restore 0

# Confirmar restauracion
C:\> ls /Documentos
C:\> type /Documentos/documento1.txt
```

Implementamos una papelera de reciclaje con capacidad configurable. Los archivos eliminados no se borran permanentemente, sino que van a la papelera donde pueden ser restaurados.

Puntos a destacar:

- Eliminación segura con confirmación
- Capacidad configurable (default: 100 items)

### B. Características avanzadas de papelera

```bash
# Ver estadisticas de la papelera
C:\> trash stats

# Buscar dentro de la papelera
C:\> trash search doc

# Crear mas elementos y eliminarlos
C:\> touch temporal1.txt "Temporal 1"
C:\> touch temporal2.txt "Temporal 2"
C:\> rm temporal1.txt
C:\> rm temporal2.txt

# Mostrar papelera con multiples items
C:\> trash

# Vaciar papelera
C:\> emptytrash
¿Estás seguro de vaciar la papelera? (s/n): s

# Verificar que esta vacia
C:\> trash
```

La papelera incluye caracteristicas avanzadas:estadisticas de uso, busqueda interna y limpieza automática despues de 30 dias. También tiene un limite configurable para evitar uso excesivo de memoria.


## PRUEBAS Y RENDIMIENTO

### A. Ejecutar pruebas rapidas

```bash
# Salir del simulador
C:\> exit

# Ejecutar suite de pruebas unitarias
python run_tests.py --unitarias

```

Para garantizar calidad,desarrollamos una suite completa de pruebas. Tenemos 78 pruebas unitarias que cubren gran parte del codigo. Todas las operaciones estan validadas, incluyendo casos limite y manejo de errores.


### B. Demostración de benchmark

```bash
# Volver al simulador
python cmd_simulator.py

# Ejecutar benchmark integrado
C:\> benchmark

# Salir y mostrar archivo de resultados
C:\> exit

# Mostrar archivo de resultados
cat benchmark_resultados.txt | head -20
```

El benchmark integrado muestra el rendimiento del sistema. Podemos manejar varios nodos rapidamente, al igual que con busquedas.


##  FIN
### PROYECTO (usando arboles)

Caracteristicas:
- Sistema de archivos jerarquico
- Busqueda Trie + HashMap
- Papelera
- Persistencia automatica
- Comandos
- Pruebas

