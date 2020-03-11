# get the current cell
def get_cell_piece(x, y):
    x = x - 120
    y = y - 60
    return [y // 68, x // 68]

# valid moves for a white pieces
# pawn moves
def get_white_pawn_moves(cell_piece, current_piece_cell, next_piece_cell):
    if current_piece_cell[0] == next_piece_cell[0] + 1 and current_piece_cell[1] == next_piece_cell[1] and \
            cell_piece.get_name() == "None":
        print("MOVIMIENTO DE PEÓN BLANCO NORMAL.")
        return True
    elif current_piece_cell[0] == next_piece_cell[0] + 1 and current_piece_cell[1] + 1 == next_piece_cell[1] or \
            current_piece_cell[1] - 1 == next_piece_cell[1] and cell_piece.get_color() == "black":
        print("PEÓN BLANCO COME PEÓN NEGRO.")
        return True
    else:
        print("NO ES MOVIMIENTO VÁLIDO.")
        return False

# tower moves
def get_white_rook_moves(board, cell_piece, current_piece_cell, next_piece_cell):
    current_piece_i = current_piece_cell[0]
    current_piece_j = current_piece_cell[1]
    if current_piece_cell[1] == next_piece_cell[1] and cell_piece.get_name() == "None" or cell_piece.get_color() == "black":
        if (current_piece_cell[0] > next_piece_cell[0]):
            while next_piece_cell[0] < current_piece_cell[0]:
                piece = board[current_piece_cell[0]][next_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[0] = current_piece_i
                    return False
                current_piece_cell[0] -= 1
        else:
            while next_piece_cell[0] > current_piece_cell[0]:
                piece = board[current_piece_cell[0]][next_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[0] = current_piece_i
                    return False
                current_piece_cell[0] += 1
        print("MOVIMIENTO VERTICAL DE TORRE.")
        return True
    elif current_piece_cell[0] == next_piece_cell[0] and cell_piece.get_name() == "None" or cell_piece.get_color() == "black":
        if (current_piece_cell[1] > next_piece_cell[1]):
            while next_piece_cell[1] < current_piece_cell[1]:
                piece = board[next_piece_cell[0]][current_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[1] = current_piece_j
                    return False
                current_piece_cell[1] -= 1
        else:
            while next_piece_cell[1] > current_piece_cell[1]:
                piece = board[next_piece_cell[0]][current_piece_cell[1]]
                if not piece.get_name() == "None":
                    current_piece_cell[1] = current_piece_j
                    return False
                current_piece_cell[1] += 1
        print("MOVIMIENTO HORIZONTAL DE TORRE.")
        return True
    else:
        print("NO ES MOVIMIENTO VÁLIDO.")
        return False


# valid moves for a black pieces
def get_black_pawn_moves(cell_piece, current_piece_cell, next_piece_cell):
    if current_piece_cell[0] == next_piece_cell[0] - 1 and current_piece_cell[1] == next_piece_cell[1] and \
            cell_piece.get_name() == "None":
        print("MOVIMIENTO DE PEÓN NEGRO NORMAL.")
        return True
    elif current_piece_cell[0] == next_piece_cell[0] - 1 and current_piece_cell[1] + 1 == next_piece_cell[1] or \
            current_piece_cell[1] - 1 == next_piece_cell[1] and cell_piece.get_color() == "white":
        print("PEÓN NEGRO COME PEÓN BLANCO.")
        return True
    else:
        print("NO ES PEÓN.")
        return False