# Imports
from turtle import Turtle, Screen

# Create turtle and screen
cursor = Turtle()
screen = Screen()

# Make screen listen
screen.listen()

# Forwards function
def move_forward():
    cursor.forward(5)

# Backwards function
def move_backward():
    cursor.backward(5)

# Clockwise-turn function
def turn_clockwise():
    cursor.setheading(cursor.heading() + 5)

# Counter-clockwise function
def turn_counterclockwise():
    cursor.setheading(cursor.heading() - 5)

# Keypress functions
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_clockwise, "d")
screen.onkeypress(turn_counterclockwise, "a")

# Make screen exit on click 
screen.exitonclick()