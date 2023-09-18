# vamos utilisar matriz como sudoku (list of lists)
# donde 0 --> bloque libre

sudoku_1 = [[8, 0, 4, 7, 0, 0, 0, 6, 0],
            [0, 9, 0, 0, 4, 0, 3, 1, 0],
            [0, 3, 6, 0, 0, 2, 0, 0, 0],
            [0, 2, 5, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 7, 2, 0, 0],
            [0, 0, 1, 0, 0, 6, 9, 0, 0],
            [0, 6, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 1],
            [0, 0, 0, 4, 0, 0, 0, 8, 0]]

sudoku_2 = [[0, 2, 1, 4, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 1, 2, 0, 5, 0, 7],
            [2, 0, 0, 0, 0, 0, 0, 8, 1],
            [0, 1, 0, 0, 0, 0, 0, 4, 9],
            [0, 0, 0, 0, 0, 8, 0, 0, 0],
            [0, 8, 2, 0, 6, 0, 0, 9, 0],
            [0, 9, 4, 7, 0, 3, 0, 0, 0]]


# buscamos primer 0
def buscar_zero(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None, None


def podemos_poner_num(sudoku, row, col, num):

    # miramos si hay numeros eguales en rows - m y en columnas - n
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # buscamos en qual de 9 bloques grande (3x3) esta nuestro bloque pequeño
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3

    # miramos si hay en este bloque numero egual a nuestro
    for i in range(3):
        for j in range(3):
            if sudoku[block_row + i][block_col + j] == num:
                return False
    return True


def sudoku_final(sudoku):

    row, col = buscar_zero(sudoku)
    if row is None:
        return True

    for num in range(1, 10):
        # Miramos si podemos poner numero a este bloque
        if podemos_poner_num(sudoku, row, col, num):
            # Si podemos --> lo ponemos
            sudoku[row][col] = num

            # En recurcia seguimos resolver sudoku
            if sudoku_final(sudoku):
                for m in sudoku:
                    print(m)

            # si recurcia no ayuda, regresamos
            # y hacemos con numero nuevo en siguente iteracion
            sudoku[row][col] = 0
    return False


sudoku_final(sudoku_1)
print('----------------------------------')
sudoku_final(sudoku_2)
