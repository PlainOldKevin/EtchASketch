# Imports
from turtle import Turtle, Screen

# Create turtle and screen
cursor = Turtle()
screen = Screen()

# Make screen listen
screen.listen()

# Forwards function
def move_forward():
    cursor.foward(10)

# Backwards function
def move_backwards():
    cursor.backward(10)