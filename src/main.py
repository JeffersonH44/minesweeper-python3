import random

def ponerMinas(minas, tablero):
    minas = tablero["minas"]
    filas = tablero["filas"]
    columnas = tablero["columnas"]

    counter = 0 
    while counter < minas:
        rand_fila = random.randint(0, filas)
        rand_col = random.randint(0, columnas)
        if minas[rand_fila][rand_col] == 1:
            continue

        minas[rand_fila][rand_col] = 1
        counter += 1


def crearTablero(filas, columnas):
    tablero_minas = [[0] * columnas for _ in range(filas)]
    tablero_mostrar = [[0] * columnas for _ in range(filas)]

    tablero = {
        "minas": tablero_minas,
        "mostrar": tablero_mostrar,
        "filas": filas,
        "columnas": columnas
    }

    return tablero

def imprimirTablero(tablero):
    for elem in tablero["minas"]:
        print(elem)
    
def run():
    tablero = crearTablero(9, 9)
    imprimirTablero(tablero)


if __name__ == "__main__":
    run()
