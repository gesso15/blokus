class piece(object):
  """A place to store methods for pieces."""

  def __init__(self, shape, color):
    """pieces objects."""
    self.shape = shape
    self.color = color

  def valid_play(self, board, shape, color, location):
    """Checks in a move is valid."""
    self.in_use(board, shape, color)
    return True

  def in_use(self, board, shape, color):
    """Check if piece already in play."""
    return False

