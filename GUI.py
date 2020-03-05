# import the pygame module, so you can use it
import pygame

from Piece import Piece

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



# now i'll declare variables for all the resources
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





# i need to keep info on this board
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




def get_cell_gui(x, y):
	if (120 + 60 > x  > 120 and 430 + 60 > y > 430):
		return [6, 0]



# define a main function
def main():
	# initialize the pygame module
	pygame.init()

	# load and set the logo
	logo = pygame.image.load("resources/logo32x32.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Chess Finals")

	# create a surface on screen that has the size of 800 x 600
	screen = pygame.display.set_mode((800, 600))

	# create a cursor
	# cursor = Cursor()

	# i'll be needing a clock
	clock = pygame.time.Clock()

	# i need to define the bounds for the main board
	board_width = 555
	board_height = 555

	column_margin = 120
	row_margin = 20

	selected_piece = False

	# main loop
	while True:
		if pygame.event.poll().type == pygame.QUIT:
			return

		screen.blit(pygame.image.load("resources/background.jpg"), [0, 0])

		# i wish to surround the board with a white line
		pygame.draw.rect(screen, (51, 25, 0), [column_margin - 2, row_margin - 2, board_height + 2, board_height + 2])

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


				mouse = pygame.mouse.get_pos()
				if (pygame.mouse.get_pressed()[0]):
					#print("x: " + str(mouse[0]) + ", y: " + str(mouse[1]))
					#print(str(get_cell_gui(mouse[0], mouse[1])))

					coordinates = get_cell_gui(mouse[0], mouse[1])

					selected_piece = board[coordinates[0]][coordinates[1]]

					if not selected_piece.get_type() == "None":
						board[coordinates[0]][coordinates[1]] = none_piece


				piece = board[row][column]

				if piece.type == "pawn":
					if piece.color == "black":
						screen.blit(black_pawn_image, (board_width_value, board_height_value))
					else:
						screen.blit(white_pawn_image, (board_width_value, board_height_value))

				elif piece.type == "rook":
					if piece.color == "black":
						screen.blit(black_rook_image, (board_width_value, board_height_value))
					else:
						screen.blit(white_rook_image, (board_width_value, board_height_value))

				elif piece.type == "knight":
					if piece.color == "black":
						screen.blit(black_knight_image, (board_width_value, board_height_value))
					else:
						screen.blit(white_knight_image, (board_width_value, board_height_value))

				elif piece.type == "bishop":
					if piece.color == "black":
						screen.blit(black_bishop_image, (board_width_value, board_height_value))
					else:
						screen.blit(white_bishop_image, (board_width_value, board_height_value))

				elif piece.type == "queen":
					if piece.color == "black":
						screen.blit(black_queen_image, (board_width_value, board_height_value))
					else:
						screen.blit(white_queen_image, (board_width_value, board_height_value))

				elif piece.type == "king":
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
