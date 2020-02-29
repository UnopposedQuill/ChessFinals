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
	tower_image = pygame.image.load("resources/pieces/tower.png")

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
	margin = 5

	# i need to keep info on this board
	board = []
	for row in range(0, 8):
		board.append([])
		for column in range(0, 8):
			board[row].append(0)

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

		# cells drawing needs to be intermittent to make it black and white
		white = True

		# i need to draw the board
		for row in range(0, 8):
			for column in range(0, 8):
				if white:
					color = (255, 255, 255)
					pygame.draw.rect(screen, color, [(board_width//8 + 5) * column + 5, (board_height//8 + 5) * row + 5, board_width//8, board_height//8])

				# 1 for tower
				if board[row][column] == 0:
					screen.blit(tower_image, ((board_width//8 + 5) * column + 5, (board_height//8 + 5) * row + 5))
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
