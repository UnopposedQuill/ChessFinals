# get the current cell
def get_cell_piece(x, y):
    x = x - 120
    y = y - 60
    return [y // 68, x // 68]

# white pawn moves
def get_white_pawn_moves(cell_piece, current_piece_cell, next_piece_cell):
    if current_piece_cell[0] == next_piece_cell[0] + 1 and current_piece_cell[1] == next_piece_cell[1] and \
            cell_piece.get_name() == "None":
        print("Movimiento: peón blanco.")
        return True
    elif current_piece_cell[0] == next_piece_cell[0] + 1 and current_piece_cell[1] + 1 == next_piece_cell[1] or \
            current_piece_cell[1] - 1 == next_piece_cell[1] and cell_piece.get_color() == "black":
        print("Elimina: peón blanco a peón negro.")
        return True
    else:
        print("Movimiento de peón inválido.")
        return False

# black pawn moves
def get_black_pawn_moves(cell_piece, current_piece_cell, next_piece_cell):
    if current_piece_cell[0] == next_piece_cell[0] - 1 and current_piece_cell[1] == next_piece_cell[1] and \
            cell_piece.get_name() == "None":
        print("Movimiento: peón negro.")
        return True
    elif current_piece_cell[0] == next_piece_cell[0] - 1 and current_piece_cell[1] + 1 == next_piece_cell[1] or \
            current_piece_cell[1] - 1 == next_piece_cell[1] and cell_piece.get_color() == "white":
        print("Elimina: peón negro a peón blanco.")
        return True
    else:
        print("Movimiento de peón inválido.")
        return False

# tower moves
def get_rook_moves(board, cell_piece, current_piece_cell, next_piece_cell, current_color):
    current_piece_i = current_piece_cell[0]
    current_piece_j = current_piece_cell[1]

    # vertical move
    if current_piece_cell[1] == next_piece_cell[1] and cell_piece.get_name() == "None" and cell_piece.get_color() != current_color:

        # move to up loop
        if (current_piece_cell[0] > next_piece_cell[0]):
            while next_piece_cell[0] < current_piece_cell[0]:
                piece = board[current_piece_cell[0]][next_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[0] = current_piece_i
                    return False
                current_piece_cell[0] -= 1

        # move to down loop
        else:
            while next_piece_cell[0] > current_piece_cell[0]:
                piece = board[current_piece_cell[0]][next_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[0] = current_piece_i
                    return False
                current_piece_cell[0] += 1
        print("Movimiento: torre " + current_color + " vertical.")
        return True

    # horizontal move
    elif current_piece_cell[0] == next_piece_cell[0] and cell_piece.get_name() == "None" and cell_piece.get_color() != current_color:

        # move to right loop
        if (current_piece_cell[1] > next_piece_cell[1]):
            while next_piece_cell[1] < current_piece_cell[1]:
                piece = board[next_piece_cell[0]][current_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[1] = current_piece_j
                    return False
                current_piece_cell[1] -= 1

        # move to left loop
        else:
            while next_piece_cell[1] > current_piece_cell[1]:
                piece = board[next_piece_cell[0]][current_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[1] = current_piece_j
                    return False
                current_piece_cell[1] += 1
        print("Movimiento: torre " + current_color + " horizontal.")
        return True
    else:
        print("Movimiento de torre inválido.")
        return False
