from pieces import piece
from game import game

state = game()
square = piece("square", "blue")
state.place(square, 0)
state.place(square, 0)
