# import the pygame module, so you can use it
import pygame


# class to implement the cursor
class Cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self, 0, 0, 1, 1)

	def update(self):
		self.left, self.top = pygame.mouse.get_pos()


# class to implement a hover-like animation on buttons
class Button(pygame.sprite.Sprite):
	# image1 image to be set on standby
	# image2 image to be set on hovering
	# x x offset to be placed at
	# y y offset to be placed at
	def __init__(self, image1, image2, x=200, y=200):
		self.normal_image = image1
		self.selected_image = image2
		self.current_image = self.normal_image
		self.rect = self.current_image.get_rect()
		self.rect.left, self.rect.top = (x, y)


# define a main function
def main():
	# initialize the pygame module
	pygame.init()
	# load and set the logo
	logo = pygame.image.load("resources/logo32x32.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("Chess Finals")

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

	# create a surface on screen that has the size of 800 x 600
	screen = pygame.display.set_mode((800, 600))

	# create a cursor
	cursor = Cursor()

	# i'll be needing a clock
	clock = pygame.time.Clock()

	# i need to define the bounds for the main board
	board_width = 555
	board_height = 555

	# and the amount of distance between the board cells
	margin = 0

	# i need to keep info on this board
	"""
	board = []
	for row in range(0, 8):
		board.append([])
		for column in range(0, 8):
			board[row].append(0)
	"""
	board = [
			[-1, -2, -3, -4, -5, -3, -2, -1],
			[-6, -6, -6, -6, -6, -6, -6, -6],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[6, 6, 6, 6, 6, 6, 6, 6],
			[1, 2, 3, 4, 5, 3, 2, 1]]

	# define a variable to control the main loop
	running = True

	# main loop
	while running:
		# event handling, gets all event from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False

		# reset the screen's background
		screen.fill((0, 0, 0))

		# i wish to surround the board with a white line
		pygame.draw.rect(screen, (255, 255, 255), [0, 0, board_height + 8 * margin + 3, board_height + 8 * margin + 3])

		# cells drawing needs to be intermittent to make it black and white
		white = True

		# i need to draw the board
		for row in range(0, 8):
			for column in range(0, 8):
				if white:
					color = (255, 255, 255)
				else:
					color = (0, 0, 0)
				pygame.draw.rect(screen, color, [(board_width // 8 + margin) * column + margin,
												(board_height // 8 + margin) * row + margin, board_width // 8,
												board_height // 8])

				# 1 for rook
				if board[row][column] == 1:
					screen.blit(white_rook_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				elif board[row][column] == -1:
					screen.blit(black_rook_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				# 2 for knight
				elif board[row][column] == 2:
					screen.blit(white_knight_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				elif board[row][column] == -2:
					screen.blit(black_knight_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				# 3 for bishop
				elif board[row][column] == 3:
					screen.blit(white_bishop_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				elif board[row][column] == -3:
					screen.blit(black_bishop_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				# 4 for queen
				elif board[row][column] == 4:
					screen.blit(white_queen_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				elif board[row][column] == -4:
					screen.blit(black_queen_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				# 5 for king
				elif board[row][column] == 5:
					screen.blit(white_king_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				elif board[row][column] == -5:
					screen.blit(black_king_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				# 6 for pawn
				elif board[row][column] == 6:
					screen.blit(white_pawn_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				elif board[row][column] == -6:
					screen.blit(black_pawn_image,
								((board_width // 8 + margin) * column + margin, (board_height // 8 + margin) * row + margin))
				white = not white
			white = not white

		# make this 60 times per second
		clock.tick(60)

		# and now commit the draw
		pygame.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
	# call the main function
	main()
