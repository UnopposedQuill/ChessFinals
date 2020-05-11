
class Ai:

    iteration_count = 0

    def __init__(self, board, colour):
        self.board = board
        self.colour = colour

    # this function will take care of calling all the advanced methods within the ai
    # is planned to use the current board and then return said board, with its move done
    # notice that it receives the colour, needs to be either black or white
    def get_move(self):

        # first, I need to fetch all the possible moves
        moves = self.get_possible_moves()

        # now I need to choose the best possible move

    # this will proceed the search for moves forward
    def iterate(self):
        self.iteration_count += 1

    # this will make sure to get all the possible moves from the board argument
    def get_possible_moves(self):
        return self.board

    # this will return the best board from the boards list
    def choose_best(self):
        return self.board[0]
