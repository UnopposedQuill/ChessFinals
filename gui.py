# import the pygame module, so you can use it
import pygame

from objects.piece import *
from objects.button import *
from functions.guifunctions import *
from functions.loader import load_file
from tkinter import Tk, filedialog


# main function
def main():
    # main assets loading
    # model game pieces
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

    # image resources
    white_rook_image = pygame.image.load("resources/pieces/white-rook.png")
    black_rook_image = pygame.image.load("resources/pieces/black-rook.png")
    white_knight_image = pygame.image.load("resources/pieces/white-knight.png")
    black_knight_image = pygame.image.load("resources/pieces/black-knight.png")
    white_bishop_image = pygame.image.load("resources/pieces/white-bishop.png")
    black_bishop_image = pygame.image.load("resources/pieces/black-bishop.png")
    white_king_image = pygame.image.load("resources/pieces/white-king.png")
    black_king_image = pygame.image.load("resources/pieces/black-king.png")
    white_queen_image = pygame.image.load("resources/pieces/white-queen.png")
    black_queen_image = pygame.image.load("resources/pieces/black-queen.png")
    white_pawn_image = pygame.image.load("resources/pieces/white-pawn.png")
    black_pawn_image = pygame.image.load("resources/pieces/black-pawn.png")
    logo = pygame.image.load("resources/logo32x32.png")
    background = pygame.image.load("resources/background.jpg")
    reset = pygame.image.load("resources/buttons/reset.png")
    reset_hover = pygame.image.load("resources/buttons/reset_hover.png")
    load = pygame.image.load("resources/buttons/load.png")
    load_hover = pygame.image.load("resources/buttons/load_hover.png")

    # board variables
    board = [
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
    ]

    default_board = [
        [black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook],
        [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
        [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn],
        [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook]
    ]

    # dimensions
    board_width = 555
    board_height = 555
    column_margin = 120
    row_margin = 60

    # gui initializing
    pygame.init()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Chess Finals")
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    # control variables
    selected_piece = none_piece
    current_player = "white"
    current_event = "select"
    final_path = ""
    loaded_final = None

    # buttons
    reset_button = Button(x_offset=board_width + column_margin + 30, y_offset=30, width=150, height=30)
    load_button = Button(x_offset=board_width + column_margin + 30, y_offset=80, width=150, height=30)

    # MAIN LOOP.
    while True:
        # background image loading
        screen.blit(background, (0, 0))

        # i wish to surround the board with a black line
        pygame.draw.rect(screen, (0, 0, 0), [column_margin - 2, row_margin - 2, board_height + 2, board_height + 2])

        # cells drawing needs to be intermittent to make it black and white
        white = True

        # variables for checking mouse position
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]

        # mouse and keys events handler
        for event in pygame.event.get():

            # exit event
            if event.type == pygame.QUIT:
                return

            # mouse handler
            # turns, selected pieces and movements; click and cell/piece selection
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check if it's inside the board
                if 671 >= x >= 120 and 632 >= y >= 60:
                    cell = get_cell_piece(x, y)

                    # piece selection for a movement, it swaps between black and white
                    if selected_piece.get_name() == "None":
                        selected_piece = board[cell[0]][cell[1]]
                        if selected_piece.get_color() == current_player:
                            board[cell[0]][cell[1]] = none_piece
                        else:
                            selected_piece = none_piece
                    else:
                        board[cell[0]][cell[1]] = selected_piece
                        selected_piece = none_piece
                        if current_player == "white":
                            current_player = "black"
                        else:
                            current_player = "white"
                # check if it was inside on of the buttons
                # reset board button
                elif reset_button.is_cursor_inside(mouse):
                    if loaded_final is None:
                        for i in range(len(board)):
                            for j in range(len(board[i])):
                                board[i][j] = default_board[i][j]
                    else:
                        for i in range(len(board)):
                            for j in range(len(board[i])):
                                board[i][j] = loaded_final[i][j]
                    current_player = "white"
                # load board button
                elif load_button.is_cursor_inside(mouse):
                    root = Tk()
                    root.iconify()
                    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                               filetypes=(("Plain Text files", "*.txt"), ("all files", "*.*")))
                    print(root.filename)
                    root.destroy()

                    # time to load the board
                    final_path, loaded_final = load_file(root.filename)
                    if loaded_final is not None:
                        for i in range(len(board)):
                            for j in range(len(board[i])):
                                board[i][j] = loaded_final[i][j]
                        current_player = "white"

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

                # draws said piece on the board
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

        # visual buttons handling
        if reset_button.is_cursor_inside(cursor=mouse):
            screen.blit(reset_hover, (reset_button.x_offset, reset_button.y_offset))
        else:
            screen.blit(reset, (reset_button.x_offset, reset_button.y_offset))

        if load_button.is_cursor_inside(cursor=mouse):
            screen.blit(load_hover, (load_button.x_offset, load_button.y_offset))
        else:
            screen.blit(load, (load_button.x_offset, load_button.y_offset))

        # make this 60 times per second
        clock.tick(60)

        # and now commit the draw
        pygame.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
