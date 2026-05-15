# Función para dibujar mapa
def dibujar_mapa(mapa):
    print("\n  0 1 2 3 4")
    for i in range(len(mapa)):
        print(f"{i} ", end="")
        for j in range(len(mapa[i])):
            valor = mapa[i][j]

            if valor == 1:
                simbolo = "B"
            elif valor == 8:
                simbolo = "X"
            elif valor == 9:
                simbolo = "O"
            else:
                simbolo = "~"

            print(f"{simbolo} ", end="")
        print()

# Crear matriz 5x5 llena de agua
oceano = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Posicionar barcos
oceano[1][2] = 1
oceano[3][4] = 1
oceano[4][0] = 1

print("¡Océano generado y flota desplegada!")
dibujar_mapa(oceano)

# Sistema de ataque
fila = int(input("\nIngresa la fila para atacar (0-4): "))
columna = int(input("Ingresa la columna para atacar (0-4): "))

# Verificar ataque
if oceano[fila][columna] == 1:
    print("¡IMPACTO CRÍTICO! Hundiste un barco.")
    oceano[fila][columna] = 8
else:
    print("Fallaste. Solo le diste al agua.")
    oceano[fila][columna] = 9

# Mostrar mapa actualizado
dibujar_mapa(oceano)