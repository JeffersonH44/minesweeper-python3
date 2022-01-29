import random

def ponerMinas(minas, tablero):
    tablero_minas = tablero["minas"]
    filas = tablero["filas"]
    columnas = tablero["columnas"]

    counter = 0
    while counter < minas:
        rand_fila = random.randint(0, filas - 1)
        rand_col = random.randint(0, columnas - 1)
        if tablero_minas[rand_fila][rand_col] == -1: # -1 is used when is a mine
            continue
        tablero_minas[rand_fila][rand_col] = -1
        counter += 1

def obtenerVecindad(index_i, index_j, filas, columnas):
    indices = []
    for i in range(index_i - 1, index_i + 2):
        if i < 0 or i >= filas:
            continue
        for j in range(index_j - 1, index_j + 2):
            if j < 0 or j >= columnas:
                continue
            if i == index_i and j == index_j:
                continue
            indices.append((i, j))
    return indices


def contarMinasVecinas(tablero):
    tablero_minas = tablero["minas"]
    filas = tablero["filas"]
    columnas = tablero["columnas"]

    for i in range(filas):
        for j in range(columnas):
            if tablero_minas[i][j] == -1:
                continue
            vecinos_idx = obtenerVecindad(i, j, filas, columnas)
            contador = 0
            for fila, col in vecinos_idx:
                if tablero_minas[fila][col] == -1:
                    contador += 1
            tablero_minas[i][j] = contador

def crearMatriz(filas, columnas, valor=0):
    return [[valor] * columnas for _ in range(filas)]

def crearTablero(filas, columnas):
    tablero_minas = crearMatriz(filas, columnas)
    tablero_mostrar = crearMatriz(filas, columnas, valor="-")

    tablero = {
        "minas": tablero_minas,
        "mostrar": tablero_mostrar,
        "filas": filas,
        "columnas": columnas
    }

    return tablero

def imprimirTablero(tablero, test=False):
    for elem in tablero["mostrar"]:
        print(elem)
    if test:
        for elem in tablero["minas"]:
            print(elem)

def crearJuego(filas, columnas, total_minas=10):
    tablero = crearTablero(filas, columnas)
    ponerMinas(total_minas, tablero)
    contarMinasVecinas(tablero)
    return tablero

def obtenerEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except:
            print(f"Debes introducir un entero, intentalo de nuevo")

def mostrarMinas(tablero):
    tablero_minas = tablero["minas"]
    tablero_mostrar = tablero["mostrar"]
    filas = tablero["filas"]
    columnas = tablero["columnas"]

    for i in range(filas):
        for j in range(columnas):
            if tablero_minas[i][j] == -1:
                tablero_mostrar[i][j] = "x"


def realizarAccion(fila, columna, tablero):
    tablero_minas = tablero["minas"]
    if tablero_minas[fila][columna] == -1:
        mostrarMinas(tablero)
        return False
    return True

def obtenerDatos():
    fila = obtenerEntero("Introduce la fila:")
    columna = obtenerEntero("Introduce la columna:")
    return (fila, columna)

def run():
    tablero = crearJuego(9, 9)
    is_playing = True
    while is_playing:
        imprimirTablero(tablero, test=True)
        fila, columna = obtenerDatos()
        is_playing = realizarAccion(fila, columna, tablero)
    imprimirTablero(tablero)
    print("Perdiste!")



if __name__ == "__main__":
    run()
