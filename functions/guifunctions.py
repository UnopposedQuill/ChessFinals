def get_cell_piece(x, y):
    x = x - 120
    y = y - 60
    return [y // 68, x // 68]

# valid moves for a white pieces
def get_white_pawn_valid_moves(cell_piece, curr_piece_cell, next_piece_cell):
    if curr_piece_cell[0] == next_piece_cell[0] + 1 and curr_piece_cell[1] == next_piece_cell[1] and \
            cell_piece.get_name() == "None":
        print("MOVIMIENTO DE PEÓN BLANCO NORMAL.")
        return True
    elif curr_piece_cell[0] == next_piece_cell[0] + 1 and curr_piece_cell[1] + 1 == next_piece_cell[1] or \
            curr_piece_cell[1] - 1 == next_piece_cell[1] and cell_piece.get_color() == "black":
        print("PEÓN BLANCO COME PEÓN NEGRO.")
        return True
    else:
        print("NO ES MOVIMIENTO VÁLIDO.")
        return False

# valid moves for a black pieces
def get_black_pawn_valid_moves(cell_piece, curr_piece_cell, next_piece_cell):
    if curr_piece_cell[0] == next_piece_cell[0] - 1 and curr_piece_cell[1] == next_piece_cell[1] and \
            cell_piece.get_name() == "None":
        print("MOVIMIENTO DE PEÓN NEGRO NORMAL.")
        return True
    elif curr_piece_cell[0] == next_piece_cell[0] - 1 and curr_piece_cell[1] + 1 == next_piece_cell[1] or \
            curr_piece_cell[1] - 1 == next_piece_cell[1] and cell_piece.get_color() == "white":
        print("PEÓN NEGRO COME PEÓN BLANCO.")
        return True
    else:
        print("NO ES PEÓN.")
        return False