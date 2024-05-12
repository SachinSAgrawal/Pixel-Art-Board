'''
Sachin Agrawal
June 30th, 2021
PixelArtBoard.py
In this program, a user can paint a simple picture on a 6x6 grid using turtle graphics.
'''

import turtle

def main():
    # Set up everything
    print("PIXEL ART BOARD")
    print("Made by Sachin")

    # Ask for background and foreground colors
    bgcolor = input("Please enter a color for the background: ")
    maincolor = input("Please enter a color for the foreground: ")

    # Set up the screen
    wn = turtle.Screen()
    wn.setup(300, 300)
    wn.bgcolor(bgcolor)

    # Create the turtle for drawing
    drawing_turtle = turtle.Turtle() 
    drawing_turtle.speed(0)  # Fastest drawing speed
    drawing_turtle.hideturtle()
    drawing_turtle.color(maincolor)
    drawing_turtle.up()
    drawing_turtle.goto(-150, 100)  # Position the turtle at the top left corner of the grid
    drawing_turtle.down()

    # Instructions
    print("The pixel art board is broken into 36 sections in a 6 by 6 grid. "
          "For each section, enter 0 to fill it or 1 to leave it empty. "
          "Please only enter 1s and 0s. See examples in the files section.")

    # Draw the grid based on user input
    for row in range(6):
        for col in range(6):
            sections(drawing_turtle)  # Draw each section
            drawing_turtle.forward(50)  # Move to the next section

        # Move to the start of the next row
        drawing_turtle.up()
        drawing_turtle.goto(-150, drawing_turtle.ycor() - 50)
        drawing_turtle.down()

    # Finalization
    print("You are done! Feel free to screenshot your image.")

# Function to draw each section based on user input
def sections(turtle):
    turtle.down()
    section = int(input("Next Section: "))  # Ask user whether to fill the section or not
    if section == 0:
        turtle.begin_fill()
        for _ in range(4):  # Draw a square
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()
    else:
        turtle.up()  # Move the turtle without drawing
        turtle.down()
    turtle.up()  # Lift the pen

if __name__ == "__main__":
    main()
