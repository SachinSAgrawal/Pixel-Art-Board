'''
Sachin Agrawal
June 30th, 2021
PixelArtBoard.py
In this program, a user can paint a simple picture on a 6x6 grid using turtle graphics.
'''

import turtle

def main():
    # Print program title and author
    print("\nPIXEL ART BOARD")
    print("Made by Sachin")

    # Get user input for colors
    bg_color = input("\nEnter a background color: ")
    fg_color = input("Enter a foreground color: ")

    # Display instructions
    print("\nThe pixel art board is broken into 36 sections in a 6 by 6 grid.\n"
          "For each section, enter a 1 if you want it to be the foreground\n"
          "color and a 0 if you want it to be the background color. The\n"
          "sections go across, then down to the next line. The turtle will\n"
          "be in the center of the section in question to help visualize your\n"
          "place. See some examples in the README.md file.\n")

    # Set up the turtle screen
    window = turtle.Screen()
    window.setup(500, 500)
    window.bgcolor(bg_color)

    # Create a turtle object
    drawing_turtle = turtle.Turtle() 

    # Set speed and color
    drawing_turtle.speed(0)
    drawing_turtle.color(fg_color)

    # Draw the border around the grid
    drawing_turtle.up()
    drawing_turtle.goto(-150, 150)
    drawing_turtle.down()
    drawing_turtle.pensize(2)  # Make the border thicker
    for _ in range(4):
        drawing_turtle.forward(300)
        drawing_turtle.right(90)
    drawing_turtle.pensize(1)  # Reset pen size
    drawing_turtle.shape("turtle")

    # Move turtle along grid
    for row in range(6):
        for col in range(6):
            drawing_turtle.up()
            drawing_turtle.goto(-150 + col * 50 + 25, 150 - row * 50 - 25)
            drawing_turtle.down()

            # Determine what to do for each section
            sections(drawing_turtle)  

    # Hide the turtle because finished
    drawing_turtle.hideturtle()
    print("You are done! Feel free to screenshot your image.\n")
    turtle.done()

# Function to handle logic for each section
def sections(turtle):
    
    # Get user input for the section
    while True:
        user_input = input("Next Section: ")
        # Check if the input is a numeric string
        if user_input.isdigit():  
            int_input = int(user_input)
            # Check if the input is either 0 or 1
            if int_input in [0, 1]:
                break
            else:
                print("Invalid input. Please enter either 0 or 1.")
        else:
            print("Invalid input. Please enter a numeric value.")

    # Fill in the section if specified
    if int_input == 1:
        # Move turtle to correct position
        turtle.up()
        turtle.left(180)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.down()

        # Draw and fill in the square
        turtle.begin_fill()
        for _ in range(4):  
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill() 

# Entry point of the program
if __name__ == "__main__":
    main()