import turtle

def main():
  #sets up everthing
  print("PIXEL ART BOARD")
  print("Made by Sachin")
  bgcolor = input("Please enter a color for the background: ")
  maincolor = input("Please enter a color for the foreground: ")
  wn = turtle.Screen()
  wn.setup(300, 300)
  wn.bgcolor(bgcolor)
  bob = turtle.Turtle()
  bob.speed(0)
  bob.hideturtle()
  bob.color(maincolor)
  bob.up()
  bob.goto(-150,100)
  bob.down()
  #instructions
  print("The pixel art board is broken into 36 sections in a 6 by 6 grid. For each of the sections, you will enter a 0 if you want it filled and a 1 if you do not want it filled. Please only enter 1s and 0s. The sections go across, then down to the next line. See examples in the files section.")
  #first section 
  sect1 = int(input("First Section: "))
  if sect1 == 0:
    bob.begin_fill()
    for count in range(4):
      bob.forward(50)
      bob.left(90)
    bob.end_fill()
  else:
    bob.up  
    bob.down
  bob.up()
  #finishes first line
  xvalue = -100
  for count in range(5):
    bob.goto(xvalue,100)
    sections(bob)
    xvalue += 50
  #the rest of lines
  yvalue = 50
  for count1 in range(5):
    xvalue = -150
    for count in range(6):
      bob.goto(xvalue,yvalue)
      sections(bob)
      xvalue += 50
    yvalue -= 50
  #finale
  print("You are done! Feel free to screenshot your image.")

#code for each box in the grid
def sections(b):
  b.down
  section = int(input("Next Section: "))
  if section == 0:
    b.begin_fill()
    for count in range(4):
      b.forward(50)
      b.left(90)
    b.end_fill()
  else:
    b.up  
    b.down
  b.up  

if __name__=="__main__":
  main()
