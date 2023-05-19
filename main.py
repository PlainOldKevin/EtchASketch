# Imports
from turtle import Turtle, Screen

# Create turtle and screen
cursor = Turtle()
screen = Screen()

# Make screen listen
screen.listen()

# Forwards function
def move_forward():
    cursor.forward(10)

# Backwards function
def move_backward():
    cursor.backward(10)

# Left turn function
def turn_left():
    cursor.left(10)

# Right turn function
def turn_right():
    cursor.right(10)

# Clear screen function
def clear():
    cursor.clear()
    cursor.reset()

# Keypress functions
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "d")
screen.onkey(turn_right, "a")
screen.onkey(clear, "c" )

# Make screen exit on click 
screen.exitonclick()