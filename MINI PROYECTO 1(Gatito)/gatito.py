tablero = [" " for _ in range(9)]

def mostrar_tablero():
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---|---|---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---|---|---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("\n")

def verificar_ganador(jugador):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for combo in combinaciones:
        if all(tablero[i] == jugador for i in combo):
            return True
    return False

def juego():
    jugador_actual = "❌"
    while " " in tablero:
        mostrar_tablero()
        try:
            movimiento = int(input(f"Turno de {jugador_actual} (0-8): "))
            if tablero[movimiento] == " ":
                tablero[movimiento] = jugador_actual
                if verificar_ganador(jugador_actual):
                    mostrar_tablero()
                    print(f"🎉 ¡{jugador_actual} ha ganado! 🎉")
                    return
                jugador_actual = "⭕" if jugador_actual == "❌" else "❌"
            else:
                print(" Esa casilla ya está ocupada. Intenta otra.")
        except (ValueError, IndexError):
            print("Entrada inválida. Escribe un número del 0 al 8.")
    mostrar_tablero()
    print("¡Empate! Nadie ganó esta vez.")

juego()