class piece(object):
  """A place to store methods for pieces."""

  def __init__(self, color):
    """pieces objects. Upper left is start index (even if empty)"""
    self.shape = [[0]]
    self.color = color
    self.rotation = 0

  def corners(self):
    """returns list of indices of valid play corners"""
    corners = list()
    for x, val_x in enumerate(self.shape):
      for y, val_y in enumerate(val_x):
        if val_y is 3:
          corners.append([x, y])
    return corners

  def edges(self):
    """returns list of indices of edges for comarison"""
    edges = list()
    for x, val_x in enumerate(self.shape):
      for y, val_y in enumerate(val_x):
        if val_y is 2:
          edges.append([x, y])
    return edges

  def rotate(self):
    """Rotate the piece 90 degrees clockwise."""
    # TODO ccw rotation
    newshape = []
    for i in range(len(self.shape[0])):
      newshape.append([x[i] for x in self.shape])
    self.shape = newshape

  # TODO add a flip function

class dot(piece):
  """A 1x1 dot."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,3],
                  [2,1,2],
                  [3,2,3]]

class square(piece):
  """A 2x2 square."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,3],
                  [2,1,1,2],
                  [2,1,1,2],
                  [3,2,2,3]]

class two_bar(piece):
  """A 1x2 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,3],
                  [2,1,1,2],
                  [3,2,2,3]]

class three_bar(piece):
  """A 1x3 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,2,3],
                  [2,1,1,1,2],
                  [3,2,2,2,3]]

class four_bar(piece):
  """A 1x4 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,2,2,3],
                  [2,1,1,1,1,2],
                  [3,2,2,2,2,3]]

class five_bar(piece):
  """A 1x5 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,2,2,2,3],
                  [2,1,1,1,1,1,2],
                  [3,2,2,2,2,2,3]]

class two_x_two_leg(piece):
  """A right angle 2x2 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,3],
                  [2,1,1,2],
                  [3,2,1,2],
                  [0,3,2,3]]

class two_x_three_leg(piece):
  """A right angle 2x3 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,3],
                  [2,1,1,2],
                  [3,2,1,2],
                  [0,2,1,2],
                  [0,3,2,3]]

class two_x_four_leg(piece):
  """A right angle 2x4 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,3],
                  [2,1,1,2],
                  [3,2,1,2],
                  [0,2,1,2],
                  [0,2,1,2],
                  [0,3,2,3]]

class three_x_three_leg(piece):
  """A right angle 3x3 bar."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,2,3],
                  [2,1,1,1,2],
                  [3,2,2,1,2],
                  [0,0,2,1,2],
                  [0,0,3,2,3]]

class small_t(piece):
  """A small t."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,3,0],
                  [3,2,1,2,3],
                  [2,1,1,1,2],
                  [3,2,2,2,3]]

class big_t(piece):
  """A small t."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,3,0],
                  [0,2,1,2,0],
                  [3,2,1,2,3],
                  [2,1,1,1,2],
                  [3,2,2,2,3]]

class esse(piece):
  """A s."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,2,3],
                  [3,2,1,1,2],
                  [2,1,1,2,3],
                  [3,2,2,3,0]]

class long_esse(piece):
  """A long s."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,2,2,3],
                  [3,2,1,1,1,2],
                  [2,1,1,2,2,3],
                  [3,2,2,3,0,0]]

class big_esse(piece):
  """A big s."""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,0,3,2,3],
                  [3,2,2,1,2],
                  [2,1,1,1,2],
                  [2,1,2,2,3],
                  [3,2,3,0,0]]

class oaklahoma(piece):
  """A oaklahoma"""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,3],
                  [3,2,1,2],
                  [2,1,1,2],
                  [2,1,1,2],
                  [3,2,2,3]]

class double_u(piece):
  """A double_u"""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,2,3],
                  [3,2,1,1,2],
                  [2,1,1,2,3],
                  [2,1,2,3,0],
                  [3,2,3,0,0]]

class cup(piece):
  """A cup"""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[3,2,2,3],
                  [2,1,1,2],
                  [2,1,2,3],
                  [2,1,1,2],
                  [3,2,2,3]]

class texas(piece):
  """A texas"""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,2,3],
                  [3,2,1,1,2],
                  [2,1,1,2,3],
                  [3,2,1,2,0],
                  [0,3,2,3,0]]

class star(piece):
  """A star"""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,3,0],
                  [3,2,1,2,3],
                  [2,1,1,1,2],
                  [3,2,1,2,3],
                  [0,3,2,3,0]]

class dog_leg(piece):
  """A dog_leg"""
  def __init__(self, color):
    piece.__init__(self, color)
    self.shape = [[0,3,2,3,0,0],
                  [3,2,1,2,2,3],
                  [2,1,1,1,1,2],
                  [3,2,2,2,2,3]]

