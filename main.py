# Imports
from turtle import Turtle, Screen

# Create turtle and screen
cursor = Turtle()
screen = Screen()

# Screen title
screen.title("Etch-A-Sketch")

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
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c" )

# Make screen exit on click 
screen.exitonclick()