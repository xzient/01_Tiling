# Title: 01: Tiling
#  Date: 2024-07-18

from turtle import *
import random

setup(1000, 1000)

def framing(s=500, w=1):
    width(w)
    penup()
    goto(-s, -s)
    pendown()
    goto( s, -s)
    goto( s,  s)
    goto(-s,  s)
    goto(-s, -s)



def tiling(x, y, s, l, mode="straight"):
    """
    Simple tiling drawing.
    """
    
    if random.random() < .5:
        width(3)
    else:
        width(2)

    if random.random() < .5:
        mode="straight"
    else:
        mode="diagonal"
        

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
framing(400, 1)
framing(401, 1)
framing(403, 1)
framing(405, 1)
tiling(0,0,400, 6, mode="diagonal")
tracer(True)
exitonclick()