import pprint

class game(object):
  """A place to store methods for game play."""

  def __init__(self):
    """board object."""
    self.board = [[0 for x in range(20)] for y in range(20)]
    self.in_play = {"blue": [], "red": [], "green": [], "yellow": []}

  def place(self, piece, location):
    """hurry up and play!"""
    if self.valid_play(piece, location):
      # TODO actually add the piece.
      self.in_play[piece.color].append(piece.shape)
      self.print_board()

  def valid_play(self, piece, location):
    """Checks in a move is valid."""
    # TODO add first piece checks
    # TODO add overlap checks
    # TODO add side check
    # TODO add corner check
    if not self.in_use(piece):
      return True
    else:
      return False

  def in_use(self, piece):
    """Check if piece already in play."""
    # TODO check for valid comparisons
    use = piece.shape in self.in_play[piece.color]
    if use:
      print("Not a valid move: %s %s already in play" %(piece.color, piece.shape))
    return use

  def print_board(self):
    pprint.pprint(self.board)
