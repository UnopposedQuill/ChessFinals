# import the pygame module, so you can use it
import pygame

from program.objects.Piece import *
from program.functions.GUIFunctions import *

# PIEZAS DE JUEGO.
none_piece = Piece("None", "None")
black_pawn = Piece("black", "pawn")
black_rook = Piece("black", "rook")
black_knight = Piece("black", "knight")
black_bishop = Piece("black", "bishop")
black_queen = Piece("black", "queen")
black_king = Piece("black", "king")
white_pawn = Piece("white", "pawn")
white_rook = Piece("white", "rook")
white_knight = Piece("white", "knight")
white_bishop = Piece("white", "bishop")
white_queen = Piece("white", "queen")
white_king = Piece("white", "king")

# RECURSOS DE IMÁGENES DE FONDO.
white_rook_image = pygame.image.load("program/resources/pieces/white-rook.png")
black_rook_image = pygame.image.load("program/resources/pieces/black-rook.png")
white_knight_image = pygame.image.load("program/resources/pieces/white-knight.png")
black_knight_image = pygame.image.load("program/resources/pieces/black-knight.png")
white_bishop_image = pygame.image.load("program/resources/pieces/white-bishop.png")
black_bishop_image = pygame.image.load("program/resources/pieces/black-bishop.png")
white_king_image = pygame.image.load("program/resources/pieces/white-king.png")
black_king_image = pygame.image.load("program/resources/pieces/black-king.png")
white_queen_image = pygame.image.load("program/resources/pieces/white-queen.png")
black_queen_image = pygame.image.load("program/resources/pieces/black-queen.png")
white_pawn_image = pygame.image.load("program/resources/pieces/white-pawn.png")
black_pawn_image = pygame.image.load("program/resources/pieces/black-pawn.png")
logo = pygame.image.load("program/resources/logo32x32.png")
background = pygame.image.load("program/resources/background.jpg")

# TABLERO.
board = [
    [black_rook, black_knight, black_bishop, black_king, black_queen, black_bishop, black_knight, black_rook],
    [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
    [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
    [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
    [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
    [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
    [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn],
    [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook]
]

# DIMENCIONES.
board_width = 555
board_height = 555
column_margin = 120
row_margin = 60


# FUNCIÓN PRINCIPAL.
def main():
    # INICIALIZACIÓN DE GUI.
    pygame.init()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chess Finals")
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    # MAIN LOOP.
    while True:
        if pygame.event.poll().type == pygame.QUIT:
            return

        screen.blit(background, (0, 0))

        # i wish to surround the board with a white line
        pygame.draw.rect(screen, (0, 0, 0), [column_margin - 2, row_margin - 2, board_height + 2, board_height + 2])

        # cells drawing needs to be intermittent to make it black and white
        white = True

        # i need to draw the board
        for row in range(0, 8):
            for column in range(0, 8):
                if white:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)

                board_width_value = (board_width // 8) * column + column_margin
                board_height_value = (board_height // 8) * row + row_margin

                pygame.draw.rect(screen, color,
                                 [board_width_value, board_height_value, board_width // 8, board_height // 8])

                # CLICK Y SELECCIÓN SE CELDA/PIEZA.
                mouse = pygame.mouse.get_pos()
                x = mouse[0]
                y = mouse[1]
                if pygame.mouse.get_pressed()[0] and 671 >= x >= 120 and 564 >= y >= 60:
                    cell = get_cell_piece(x, y)
                    if not cell == "Not selected":
                        selected_piece = board[cell[0]][cell[1]]
                        print(
                            selected_piece.get_name() + " - " + selected_piece.get_color() +
                            ", in pos: " + str(cell))

                # DIBUJA LA PIEZA EN EL TABLERO.
                piece = board[row][column]
                if piece.get_name() == "pawn":
                    if piece.color == "black":
                        screen.blit(black_pawn_image, (board_width_value, board_height_value))
                    else:
                        screen.blit(white_pawn_image, (board_width_value, board_height_value))

                elif piece.get_name() == "rook":
                    if piece.color == "black":
                        screen.blit(black_rook_image, (board_width_value, board_height_value))
                    else:
                        screen.blit(white_rook_image, (board_width_value, board_height_value))

                elif piece.get_name() == "knight":
                    if piece.color == "black":
                        screen.blit(black_knight_image, (board_width_value, board_height_value))
                    else:
                        screen.blit(white_knight_image, (board_width_value, board_height_value))

                elif piece.get_name() == "bishop":
                    if piece.color == "black":
                        screen.blit(black_bishop_image, (board_width_value, board_height_value))
                    else:
                        screen.blit(white_bishop_image, (board_width_value, board_height_value))

                elif piece.get_name() == "queen":
                    if piece.color == "black":
                        screen.blit(black_queen_image, (board_width_value, board_height_value))
                    else:
                        screen.blit(white_queen_image, (board_width_value, board_height_value))

                elif piece.get_name() == "king":
                    if piece.color == "black":
                        screen.blit(black_king_image, (board_width_value, board_height_value))
                    else:
                        screen.blit(white_king_image, (board_width_value, board_height_value))

                white = not white
            white = not white

        # make this 60 times per second
        clock.tick(60)

        # and now commit the draw
        pygame.display.flip()
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
