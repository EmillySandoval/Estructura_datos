#!/usr/bin/env python3
"""
Script para ejecutar todas las pruebas del proyecto
"""

import sys
import os
import subprocess
import argparse

def ejecutar_pruebas_unitarias():
    """Ejecuta pruebas unitarias basicas"""
    print("\n" + "=" * 70)
    print("EJECUTANDO PRUEBAS UNITARIAS")
    print("=" * 70)
    
    comando = [sys.executable, "-m", "unittest", "tests.py", "-v"]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print(resultado.stdout)
        
        if resultado.stderr:
            print("Errores:", resultado.stderr)
        
        return resultado.returncode == 0
    except Exception as e:
        print(f"Error ejecutando pruebas unitarias: {e}")
        return False

def ejecutar_pruebas_integracion():
    """Ejecuta pruebas de integracion"""
    print("\n" + "=" * 70)
    print("EJECUTANDO PRUEBAS DE INTEGRACION")
    print("=" * 70)
    
    comando = [sys.executable, "test_integracion.py"]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print(resultado.stdout)
        
        if resultado.stderr:
            print("Errores:", resultado.stderr)
        
        return resultado.returncode == 0
    except Exception as e:
        print(f"Error ejecutando pruebas de integracion: {e}")
        return False

def ejecutar_benchmark():
    """Ejecuta pruebas de rendimiento"""
    print("\n" + "=" * 70)
    print("EJECUTANDO PRUEBAS DE RENDIMIENTO (BENCHMARK)")
    print("=" * 70)
    
    # Verificar si benchmark.py existe
    if not os.path.exists("benchmark.py"):
        print("ERROR: benchmark.py no encontrado")
        return False
    
    comando = [sys.executable, "benchmark.py"]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print(resultado.stdout)
        
        if resultado.stderr:
            print("Errores:", resultado.stderr)
        
        return resultado.returncode == 0
    except Exception as e:
        print(f"Error ejecutando benchmark: {e}")
        return False

def ejecutar_pruebas_personalizadas(tamanos=None):
    """Ejecuta pruebas personalizadas con diferentes tamanos"""
    if tamanos is None:
        tamanos = [100, 500, 1000]
    
    print("\n" + "=" * 70)
    print("EJECUTANDO PRUEBAS PERSONALIZADAS")
    print("=" * 70)
    
    from benchmark import Benchmark
    
    benchmark = Benchmark()
    
    for tamaño in tamanos:
        print(f"\n[TAMAÑO: {tamaño} nodos]")
        
        # Prueba insercion
        resultado = benchmark.prueba_insercion_masiva(tamaño)
        
        if resultado["tamano_verificado"] != tamaño + 1:
            print(f"  [ERROR] Tamano incorrecto!")
            return False
    
    return True

def verificar_dependencias():
    """Verifica que todas las dependencias esten instaladas"""
    print("\n" + "=" * 70)
    print("VERIFICANDO DEPENDENCIAS")
    print("=" * 70)
    
    dependencias = [
        ("sistema_archivos.py", True),
        ("persistencia.py", True),
        ("busqueda_trie.py", True),
        ("papelera_manager.py", True),
        ("cmd_simulator.py", True),
        ("tests.py", True),
        ("benchmark.py", False),
        ("test_integracion.py", False),
    ]
    
    todas_ok = True
    
    for archivo, requerido in dependencias:
        if os.path.exists(archivo):
            print(f"  ✓ {archivo}")
        else:
            if requerido:
                print(f"  ✗ {archivo} (REQUERIDO - NO ENCONTRADO)")
                todas_ok = False
            else:
                print(f"  ⚠ {archivo} (opcional - no encontrado)")
    
    return todas_ok

def main():
    """Funcion principal"""
    parser = argparse.ArgumentParser(description="Ejecutar pruebas del proyecto")
    parser.add_argument("--unitarias", action="store_true", help="Ejecutar solo pruebas unitarias")
    parser.add_argument("--integracion", action="store_true", help="Ejecutar solo pruebas de integracion")
    parser.add_argument("--benchmark", action="store_true", help="Ejecutar solo benchmark")
    parser.add_argument("--personalizadas", nargs="+", type=int, help="Ejecutar pruebas personalizadas con tamanos especificos")
    parser.add_argument("--todo", action="store_true", help="Ejecutar todas las pruebas")
    parser.add_argument("--verificar", action="store_true", help="Solo verificar dependencias")
    
    args = parser.parse_args()
    
    # Si no se especifico nada, ejecutar todo
    if not any([args.unitarias, args.integracion, args.benchmark, args.personalizadas, args.todo, args.verificar]):
        args.todo = True
    
    print("=" * 70)
    print("SISTEMA DE PRUEBAS - PROYECTO ARBOLES")
    print("=" * 70)
    
    # Verificar dependencias primero
    if not verificar_dependencias():
        print("\n[ERROR] Faltan archivos requeridos")
        sys.exit(1)
    
    if args.verificar:
        return
    
    resultados = []
    
    # Ejecutar pruebas segun argumentos
    try:
        if args.unitarias or args.todo:
            resultados.append(("Pruebas Unitarias", ejecutar_pruebas_unitarias()))
        
        if args.integracion or args.todo:
            resultados.append(("Pruebas Integracion", ejecutar_pruebas_integracion()))
        
        if args.benchmark or args.todo:
            resultados.append(("Benchmark", ejecutar_benchmark()))
        
        if args.personalizadas:
            resultados.append(("Pruebas Personalizadas", ejecutar_pruebas_personalizadas(args.personalizadas)))
        
        # Mostrar resumen
        print("\n" + "=" * 70)
        print("RESUMEN FINAL")
        print("=" * 70)
        
        exitos = 0
        total = len(resultados)
        
        for nombre, exitoso in resultados:
            estado = "EXITOSO" if exitoso else "FALLIDO"
            print(f"{nombre:30} : {estado}")
            
            if exitoso:
                exitos += 1
        
        print("-" * 70)
        print(f"Total: {exitos}/{total} exitosos ({exitos/total*100:.1f}%)")
        
        if exitos == total:
            print("\n🎉 TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        else:
            print("\n⚠ ALGUNAS PRUEBAS FALLARON")
        
        # Terminar con codigo apropiado
        sys.exit(0 if exitos == total else 1)
    
    except KeyboardInterrupt:
        print("\n\n[INTERRUMPIDO] Pruebas canceladas por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()