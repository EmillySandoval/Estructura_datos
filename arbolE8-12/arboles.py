"""
GESTOR DE NÚMEROS CON ÁRBOL BINARIO
DE BÚSQUEDA (BST) EN PYTHON
(versión corregida)
"""

import os
import time
import sys

# ============================================================================ 
# CLASE NODO CON FUNCIONALIDADES VISUALES
# ============================================================================ 
class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.seleccionado = False  # Para resaltar nodo

# ============================================================================ 
# CLASE BST CON VISUALIZACIÓN
# ============================================================================ 
class BST:
    def _init_(self):
        self.raiz = None

    # Métodos auxiliares privados
    def _insertar_recursivo(self, nodo, valor, nivel):
        if nodo is None:
            print(f"\n[Nivel {nivel}] Creando nuevo nodo con valor: {valor}")
            time.sleep(0.25)
            return Nodo(valor)

        print(f"\n[Nivel {nivel}] Nodo actual: {nodo.valor}")
        nodo.seleccionado = True
        self._mostrar_arbol_animado()
        nodo.seleccionado = False
        time.sleep(0.25)

        if valor < nodo.valor:
            print(f"\n{valor} < {nodo.valor} -> Vamos al subarbol izquierdo")
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor, nivel + 1)
        elif valor > nodo.valor:
            print(f"\n{valor} > {nodo.valor} -> Vamos al subarbol derecho")
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor, nivel + 1)
        else:
            print(f"\n¡El valor {valor} ya existe en el arbol!")

        return nodo

    def _buscar_recursivo(self, nodo, valor, camino):
        if nodo is None:
            return None

        camino.append(nodo.valor)
        nodo.seleccionado = True
        self._mostrar_arbol_animado()
        time.sleep(0.25)
        nodo.seleccionado = False

        if nodo.valor == valor:
            return nodo

        if valor < nodo.valor:
            print(f"\n{valor} < {nodo.valor} -> Buscando en izquierdo")
            return self._buscar_recursivo(nodo.izquierdo, valor, camino)
        else:
            print(f"\n{valor} > {nodo.valor} -> Buscando en derecho")
            return self._buscar_recursivo(nodo.derecho, valor, camino)

    def _encontrar_minimo(self, nodo):
        while nodo and nodo.izquierdo is not None:
            print(f"\nBuscando minimo: {nodo.valor} -> vamos a izquierdo")
            nodo.seleccionado = True
            self._mostrar_arbol_animado()
            time.sleep(0.25)
            nodo.seleccionado = False
            nodo = nodo.izquierdo
        return nodo

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        print(f"\nVisitando nodo: {nodo.valor}")
        nodo.seleccionado = True
        self._mostrar_arbol_animado()
        time.sleep(0.25)

        if valor < nodo.valor:
            print(f"{valor} < {nodo.valor} -> Vamos al izquierdo")
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            print(f"{valor} > {nodo.valor} -> Vamos al derecho")
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # ¡Nodo encontrado!
            print(f"\n¡NODO ENCONTRADO PARA ELIMINAR: {nodo.valor}!")
            print("Analizando tipo de nodo...")
            time.sleep(0.5)

            nodo.seleccionado = False

            # CASO 1: Nodo hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                print("CASO 1: Nodo hoja -> Eliminacion directa")
                time.sleep(0.25)
                return None
            # CASO 2: Nodo con un hijo
            elif nodo.izquierdo is None:
                print("CASO 2: Nodo con hijo derecho")
                temp = nodo.derecho
                time.sleep(0.25)
                return temp
            elif nodo.derecho is None:
                print("CASO 2: Nodo con hijo izquierdo")
                temp = nodo.izquierdo
                time.sleep(0.25)
                return temp
            # CASO 3: Nodo con dos hijos
            else:
                print("CASO 3: Nodo con dos hijos")
                print("Buscando sucesor inorden (minimo del subarbol derecho)...")

                temp = self._encontrar_minimo(nodo.derecho)
                if temp is None:
                    return nodo  # protección
                print(f"\nSucesor encontrado: {temp.valor}")
                print(f"Reemplazando {nodo.valor} por {temp.valor}")

                nodo.valor = temp.valor
                print("Eliminando el sucesor duplicado...")

                nodo.derecho = self._eliminar_recursivo(nodo.derecho, temp.valor)
                time.sleep(0.25)

            print("\n¡Nodo eliminado exitosamente!")

        return nodo

    def _limpiar_seleccionados(self, nodo):
        if nodo is None:
            return
        nodo.seleccionado = False
        self._limpiar_seleccionados(nodo.izquierdo)
        self._limpiar_seleccionados(nodo.derecho)

    def _mostrar_arbol_recursivo(self, nodo, espacio):
        if nodo is None:
            return

        espacio += 5

        self._mostrar_arbol_recursivo(nodo.derecho, espacio)

        print()
        for i in range(5, espacio):
            print(" ", end="")

        # Marcar según tipo de nodo
        if nodo == self.raiz:
            print(f"[R:{nodo.valor}]", end="")
        elif nodo.izquierdo is None and nodo.derecho is None:
            print(f"[H:{nodo.valor}]", end="")
        else:
            print(f"[N:{nodo.valor}]", end="")

        self._mostrar_arbol_recursivo(nodo.izquierdo, espacio)

    def _mostrar_arbol_animado_recursivo(self, nodo, espacio):
        if nodo is None:
            return

        espacio += 5

        self._mostrar_arbol_animado_recursivo(nodo.derecho, espacio)

        print()
        for i in range(5, espacio):
            print(" ", end="")

        # Resaltar si está seleccionado
        if nodo.seleccionado:
            print(f"[{nodo.valor}]*", end="")
        elif nodo == self.raiz:
            print(f"[R:{nodo.valor}]", end="")
        else:
            print(f"[{nodo.valor}]", end="")

        self._mostrar_arbol_animado_recursivo(nodo.izquierdo, espacio)

    def _mostrar_arbol_animado(self):
        # evita prints enormes si el arbol es None
        if self.raiz is None:
            print("\n(Árbol vacío)\n")
            return
        print("\nEstado actual del arbol:\n")
        self._mostrar_arbol_animado_recursivo(self.raiz, 0)
        print()
        time.sleep(0.15)

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def _preorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def _posorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._posorden_recursivo(nodo.izquierdo, resultado)
            self._posorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)

    def _altura_recursivo(self, nodo):
        if nodo is None:
            return 0
        return max(self._altura_recursivo(nodo.izquierdo),
                   self._altura_recursivo(nodo.derecho)) + 1

    def _tamanio_recursivo(self, nodo):
        if nodo is None:
            return 0
        return (self._tamanio_recursivo(nodo.izquierdo) +
                self._tamanio_recursivo(nodo.derecho) + 1)

    def _limpiar_recursivo(self, nodo):
        if nodo is not None:
            self._limpiar_recursivo(nodo.izquierdo)
            self._limpiar_recursivo(nodo.derecho)
            # no es necesario del nodo explícito en Python

    def _guardar_recursivo(self, nodo, archivo):
        if nodo is None:
            archivo.write("N")  # N representa nodo nulo
            return

        archivo.write(f"[{nodo.valor}")

        # si tiene hijos, guardarlos recursivamente
        if nodo.izquierdo is not None or nodo.derecho is not None:
            archivo.write(",")
            self._guardar_recursivo(nodo.izquierdo, archivo)
            archivo.write(",")
            self._guardar_recursivo(nodo.derecho, archivo)

        archivo.write("]")

    def _cargar_recursivo(self, entrada_str, idx):
        # maneja 'N' o '[valor,...]'
        if idx >= len(entrada_str):
            return None, idx

        if entrada_str[idx] == 'N':
            return None, idx + 1

        if entrada_str[idx] != '[':
            # carácter inesperado
            return None, idx + 1

        idx += 1  # consumir '['

        # leer número (soporta negativos)
        signo = 1
        if idx < len(entrada_str) and entrada_str[idx] == '-':
            signo = -1
            idx += 1

        valor_str = ""
        while idx < len(entrada_str) and entrada_str[idx].isdigit():
            valor_str += entrada_str[idx]
            idx += 1

        if not valor_str:
            return None, idx

        valor = int(valor_str) * signo
        nodo = Nodo(valor)

        # si siguiente es ']', es hoja
        if idx < len(entrada_str) and entrada_str[idx] == ']':
            return nodo, idx + 1

        # si es coma, cargar izquierdo
        if idx < len(entrada_str) and entrada_str[idx] == ',':
            idx += 1
            nodo.izquierdo, idx = self._cargar_recursivo(entrada_str, idx)
        else:
            nodo.izquierdo = None

        # si hay coma cargar derecho
        if idx < len(entrada_str) and entrada_str[idx] == ',':
            idx += 1
            nodo.derecho, idx = self._cargar_recursivo(entrada_str, idx)
        else:
            nodo.derecho = None

        # consumir ']' si existe
        if idx < len(entrada_str) and entrada_str[idx] == ']':
            idx += 1

        return nodo, idx

    # Métodos públicos
    def insertar(self, valor):
        self._limpiar_seleccionados(self.raiz)
        print("\n" + "="*48)
        print(f"           INSERTANDO NUMERO: {valor}")
        print("="*48 + "\n")

        self.raiz = self._insertar_recursivo(self.raiz, valor, 0)

        print("\n" + "="*48)
        print("        INSERCION COMPLETADA EXITOSAMENTE")
        print("="*48 + "\n")

        print("\nArbol actual:")
        self.mostrar_arbol()
        time.sleep(0.25)

    def insertar_silencioso(self, valor):
        self.raiz = self._insertar_silencioso_recursivo(self.raiz, valor)

    def buscar(self, valor):
        self._limpiar_seleccionados(self.raiz)
        print("\n" + "="*48)
        print(f"           BUSCANDO NUMERO: {valor}")
        print("="*48 + "\n")

        camino = []
        resultado = self._buscar_recursivo(self.raiz, valor, camino)

        print("\n" + "="*48)
        if resultado is not None:
            print("           ¡NUMERO ENCONTRADO!")
            print("Camino recorrido: ", end="")
            for i in range(len(camino)):
                print(camino[i], end="")
                if i < len(camino) - 1:
                    print(" -> ", end="")
            print()
        else:
            print("       NUMERO NO ENCONTRADO EN EL ARBOL")
        print("="*48 + "\n")

        self._limpiar_seleccionados(self.raiz)
        return resultado is not None

    def eliminar(self, valor):
        if not self.buscar(valor):
            print("No se puede eliminar: el numero no existe")
            return

        self._limpiar_seleccionados(self.raiz)
        print("\n" + "="*48)
        print(f"          ELIMINANDO NUMERO: {valor}")
        print("="*48 + "\n")

        print("Arbol antes de eliminar:")
        self.mostrar_arbol()
        time.sleep(0.25)

        self.raiz = self._eliminar_recursivo(self.raiz, valor)

        print("\n" + "="*48)
        print("       ELIMINACION COMPLETADA EXITOSAMENTE")
        print("="*48 + "\n")

        print("\nArbol despues de eliminar:")
        self.mostrar_arbol()
        time.sleep(0.25)

    def mostrar_arbol(self):
        if self.raiz is None:
            print("\n" + "="*48)
            print("            EL ARBOL ESTA VACIO")
            print("="*48 + "\n")
            return

        print("\n" + "="*48)
        print("        REPRESENTACION DEL ARBOL BST")
        print("="*48 + "\n")

        self._mostrar_arbol_recursivo(self.raiz, 0)
        print()

        # Mostrar leyenda
        print("\nLeyenda: [R:raiz] [N:nodo intermedio] [H:hoja]")

    def recorrido_inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def recorrido_preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def recorrido_posorden(self):
        resultado = []
        self._posorden_recursivo(self.raiz, resultado)
        return resultado

    def obtener_altura(self):
        return self._altura_recursivo(self.raiz)

    def obtener_tamanio(self):
        return self._tamanio_recursivo(self.raiz)

    def esta_vacio(self):
        return self.raiz is None

    def exportar_inorden(self, nombre_archivo):
        resultado = self.recorrido_inorden()

        try:
            with open(nombre_archivo, 'w') as archivo:
                archivo.write("Recorrido Inorden: ")
                for i in range(len(resultado)):
                    archivo.write(str(resultado[i]))
                    if i < len(resultado) - 1:
                        archivo.write(" ")
                archivo.write(f"\nTotal nodos: {len(resultado)}")
                archivo.write(f"\nAltura: {self.obtener_altura()}")
            return True
        except Exception as e:
            print(f"Error al exportar: {e}")
            return False

    def guardar_arbol(self):
        nombre_archivo = "arbol_guardado.txt"

        try:
            with open(nombre_archivo, 'w') as archivo:
                # Guardar información de cabecera
                archivo.write("ARBOL_BST_ESTRUCTURA_COMPLETA\n")
                archivo.write("FORMATO: [valor,izquierdo,derecho] donde N=nulo\n")

                # Guardar estructura del árbol
                archivo.write("ESTRUCTURA:")
                self._guardar_recursivo(self.raiz, archivo)
                archivo.write("\n")

                # Guardar información adicional
                archivo.write(f"TOTAL_NODOS:{self.obtener_tamanio()}")
                archivo.write(f"\nALTURA:{self.obtener_altura()}")
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def cargar_arbol(self):
        nombre_archivo = "arbol_guardado.txt"

        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            print("\nNo se encontro el archivo 'arbol_guardado.txt'")
            return False

        estructura_str = ""
        for linea in lineas:
            if linea.startswith("ESTRUCTURA:"):
                estructura_str = linea[11:].strip()
                break

        if not estructura_str:
            print("\nError: No se encontro la estructura del arbol en el archivo.")
            return False

        # Limpiar el árbol actual
        self.limpiar()

        print("\nCargando arbol desde archivo...")
        print("Reconstruyendo estructura...")

        # Reconstruir el árbol desde la estructura guardada
        self.raiz, _ = self._cargar_recursivo(estructura_str, 0)

        if self.raiz is not None:
            print("\n¡Arbol cargado exitosamente preservando la estructura original!")
            print(f"Nodos: {self.obtener_tamanio()}")
            print(f"Altura: {self.obtener_altura()}")
            return True
        else:
            print("\nError: No se pudo reconstruir el arbol desde la estructura guardada.")
            return False

    def limpiar(self):
        self._limpiar_recursivo(self.raiz)
        self.raiz = None

    def _insertar_silencioso_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_silencioso_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_silencioso_recursivo(nodo.derecho, valor)

        return nodo

# ============================================================================ 
# INTERFAZ POR COMANDOS
# ============================================================================ 
class InterfazComandos:
    def _init_(self):
        self.arbol = BST()

    def _limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _mostrar_bienvenida(self):
        self._limpiar_pantalla()
        print("="*48)
        print("    GESTOR BST - INTERFAZ POR COMANDOS")
        print("="*48)
        print("Escribe 'help' para ver los comandos disponibles")
        print("="*48 + "\n")

    def _mostrar_estado(self):
        print("\n[Estado] ", end="")

        if self.arbol.esta_vacio():
            print("Arbol: Vacio")
        else:
            print(f"Nodos: {self.arbol.obtener_tamanio()}", end="")
            print(f" | Altura: {self.arbol.obtener_altura()}", end="")
            print(" | Inorden: [", end="")
            inorden = self.arbol.recorrido_inorden()
            for i in range(len(inorden)):
                print(inorden[i], end="")
                if i < len(inorden) - 1:
                    print(" ", end="")
            print("]")
        print()

    def _mostrar_ayuda(self):
        print("\n" + "="*55)
        print("                  COMANDOS DISPONIBLES")
        print("="*55)
        print("\n** Comandos principales (requeridos en el PDF):")
        print("  insert <numero>     - Insertar un numero en el arbol")
        print("  search <numero>     - Buscar un numero en el arbol")
        print("  delete <numero>     - Eliminar un numero del arbol")
        print("  inorder             - Mostrar recorrido inorden")
        print("  preorder            - Mostrar recorrido preorden")
        print("  postorder           - Mostrar recorrido postorden")
        print("  height              - Mostrar altura del arbol")
        print("  size                - Mostrar numero de nodos")
        print("  export <archivo>    - Exportar recorrido inorden a archivo")
        print("  help                - Mostrar esta ayuda")
        print("  exit                - Salir del programa")

        print("\n** Comandos adicionales (visualizacion):")
        print("  show                - Mostrar arbol visualmente")
        print("  load_example        - Cargar datos de ejemplo del PDF")
        print("  clear               - Limpiar todo el arbol")

        print("\n** Comandos de persistencia:")
        print("  save                - Guardar estructura del arbol")
        print("  load                - Cargar estructura del arbol")

        print("\n" + "="*55)
        print("Ejemplos:")
        print("  BST> insert 45")
        print("  BST> search 20")
        print("  BST> delete 15")
        print("  BST> inorder")
        print("  BST> export resultado.txt")
        print("="*55 + "\n")

    def _cargar_ejemplo(self):
        print("\nCargando datos de ejemplo del PDF...")
        print("Secuencia: 45 15 79 90 10 55 12 20 50")
        print("Inorden esperado: 10 12 15 20 45 50 55 79 90\n")

        ejemplos = [45, 15, 79, 90, 10, 55, 12, 20, 50]

        for ejemplo in ejemplos:
            print(f"Insertando {ejemplo}... ")
            self.arbol.insertar_silencioso(ejemplo)

        print("\n¡Datos de ejemplo cargados exitosamente!")

    def ejecutar(self):
        self._mostrar_bienvenida()

        while True:
            try:
                comando = input("BST> ").strip()

                # Si el comando está vacío, continuar
                if not comando:
                    continue

                # Dividir comando en partes
                partes = comando.split()
                if not partes:
                    continue

                cmd = partes[0].lower()

                if cmd == "insert" and len(partes) > 1:
                    try:
                        valor = int(partes[1])
                        self.arbol.insertar(valor)
                    except ValueError:
                        print("Error: Numero no valido")
                elif cmd == "search" and len(partes) > 1:
                    try:
                        valor = int(partes[1])
                        self.arbol.buscar(valor)
                    except ValueError:
                        print("Error: Numero no valido")
                elif cmd == "delete" and len(partes) > 1:
                    try:
                        valor = int(partes[1])
                        self.arbol.eliminar(valor)
                    except ValueError:
                        print("Error: Numero no valido")
                elif cmd == "inorder":
                    resultado = self.arbol.recorrido_inorden()
                    print("\nRecorrido Inorden: ", end="")
                    if not resultado:
                        print("Arbol vacio")
                    else:
                        for i in range(len(resultado)):
                            print(resultado[i], end="")
                            if i < len(resultado) - 1:
                                print(" ", end="")
                        print()
                elif cmd == "preorder":
                    resultado = self.arbol.recorrido_preorden()
                    print("\nRecorrido Preorden: ", end="")
                    if not resultado:
                        print("Arbol vacio")
                    else:
                        for i in range(len(resultado)):
                            print(resultado[i], end="")
                            if i < len(resultado) - 1:
                                print(" ", end="")
                        print()
                elif cmd == "postorder":
                    resultado = self.arbol.recorrido_posorden()
                    print("\nRecorrido Postorden: ", end="")
                    if not resultado:
                        print("Arbol vacio")
                    else:
                        for i in range(len(resultado)):
                            print(resultado[i], end="")
                            if i < len(resultado) - 1:
                                print(" ", end="")
                        print()
                elif cmd == "height":
                    print(f"\nAltura del arbol: {self.arbol.obtener_altura()}")
                elif cmd == "size":
                    print(f"\nNumero de nodos: {self.arbol.obtener_tamanio()}")
                elif cmd == "export" and len(partes) > 1:
                    if self.arbol.exportar_inorden(partes[1]):
                        print(f"\n¡Archivo exportado exitosamente a '{partes[1]}'!")
                    else:
                        print("\nError al exportar el archivo")
                elif cmd == "show":
                    self.arbol.mostrar_arbol()
                elif cmd == "load_example":
                    self._cargar_ejemplo()
                elif cmd == "clear":
                    respuesta = input("\n¿Esta seguro de que desea limpiar todo el arbol? (s/n): ").lower()
                    if respuesta == 's':
                        self.arbol.limpiar()
                        print("\nArbol limpiado exitosamente!")
                    else:
                        print("\nOperacion cancelada.")
                elif cmd == "save":
                    if self.arbol.guardar_arbol():
                        print("\n¡Arbol guardado exitosamente en 'arbol_guardado.txt'!")
                    else:
                        print("\nError al guardar el arbol.")
                elif cmd == "load":
                    if self.arbol.cargar_arbol():
                        print("\n¡Arbol cargado exitosamente!")
                    else:
                        print("\nError al cargar el arbol.")
                elif cmd == "help":
                    self._mostrar_ayuda()
                elif cmd == "exit":
                    respuesta = input("\n¿Desea guardar el arbol antes de salir? (s/n): ").lower()
                    if respuesta == 's':
                        if self.arbol.guardar_arbol():
                            print("\nArbol guardado en 'arbol_guardado.txt'")

                    print("\n¡Gracias por usar el Gestor de Arboles BST!")
                    time.sleep(0.5)
                    self._limpiar_pantalla()
                    break
                else:
                    print(f"\nComando no reconocido: '{cmd}'")
                    print("Escribe 'help' para ver los comandos disponibles.")

                # Mostrar estado después de cada comando
                self._mostrar_estado()

            except KeyboardInterrupt:
                print("\n\nInterrupcion detectada. Saliendo...")
                time.sleep(0.5)
                break
            except Exception as e:
                print(f"\nError inesperado: {e}")
                print("Continuando...")

# ============================================================================ 
# FUNCIÓN PRINCIPAL
# ============================================================================ 
def main():
    try:
        interfaz = InterfazComandos()
        interfaz.ejecutar()
    except Exception as e:
        print(f"Error fatal: {e}")
        input("Presione Enter para salir...")

if __name__ == "_main_":
    main()