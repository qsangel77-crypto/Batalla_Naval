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