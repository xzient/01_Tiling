# Title: 01: Tiling
#  Date: 2024-07-18

from turtle import *
import random
from time import sleep
from datetime import date
import io
from PIL import Image

HalfWidth = 500
HalfHeight = 500
setup(HalfWidth * 2, HalfHeight * 2)

colormode(255)

main_color = 'black'
# bgcolor((227,218,201)) 

def BackgroundColour(Colour=(227,218,201)):

    clear() # Prevents accumulation of layers
    penup()
    goto(-HalfWidth,-HalfHeight)
    
    color(Colour)
    begin_fill()
    
    goto(HalfWidth,-HalfHeight)
    goto(HalfWidth,HalfHeight)
    goto(-HalfWidth,HalfHeight)
    goto(-HalfWidth,-HalfHeight)
    
    end_fill()

    penup()
    home()


def framing(s=500, w=1, c=main_color):
    """
    Simple frame addition.
    """
    width(w)
    color(c)
    penup()
    goto(-s, -s)
    pendown()
    goto( s, -s)
    goto( s,  s)
    goto(-s,  s)
    goto(-s, -s)
    color(main_color)



def tiling(x, y, s, l, mode="straight"):
    """
    Simple tiling drawing.
    """
    
    # Define width
    if random.random() < .5:
        width(1.5)
    else:
        width(1.9)

    # Define mode
    if random.random() < .5:
        mode="straight"
    else:
        mode="diagonal"
    
    # Define color
    c_rand = random.random() 
    if c_rand < .50:
        color(main_color)
    elif c_rand < .75:
        color(191, 36, 15)
    else:
        color(63, 99, 74)

    # recursion ends
    if l == 0:

        if mode == "straight":
            
            # vertical line
            if random.random() < .5:
                penup()
                goto(x, y-s)
                pendown()
                goto(x, y+s)
            
            # horizontal line
            else:
                penup()
                goto(x-s, y)
                pendown()
                goto(x+s, y)
        
        elif mode == "diagonal":
            # top left to bottom right
            if random.random() < .5:
                penup()
                goto(x-s, y+s)
                pendown()
                goto(x+s, y-s)
            
            # bottomo left to top right
            else:
                penup()
                goto(x-s, y-s)
                pendown()
                goto(x+s, y+s)

    else:
        s /= 2
        l -= 1
        tiling(x-s, y+s, s, l, mode)
        tiling(x+s, y+s, s, l, mode)
        tiling(x-s, y-s, s, l, mode)
        tiling(x+s, y-s, s, l, mode)


hideturtle()
tracer(False)

BackgroundColour()
tiling(0,0,400, 6, mode="straight")
framing(400, 1)
framing(401, 1)
framing(402, 1)
framing(403, 1)
framing(404, 1)
tracer(True)
 
# Save
ps = getcanvas().postscript(colormode="color")
im = Image.open(io.BytesIO(ps.encode("utf-8")))
im.save(("examples/" + str(date.today()) + '.png'), format="PNG")
# This section needs to be reinstated after testing 
exitonclick()