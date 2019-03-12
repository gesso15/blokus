import pieces as ps
from game import game

state = game()
blue_square = ps.square("blue")
state.place(blue_square, 0)
state.place(blue_square, 0)
