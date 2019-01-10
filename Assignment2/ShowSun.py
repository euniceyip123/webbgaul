# ShowSun.py
# Eunice Yip, Raian Ohtaka, Jun Kim
# November 13, 2018

""" A module that creates two windows with one sun and one nested sun.
"""

from simpleGraphics import*

def DrawSun(x,y,r,c1,c2,c3):
    """Draws a sun in the current window with center at (x,y), and radius r.
    It also specifies fill color.
    
    The fill color can be one of the 13 built-in Python colors including YELLOW, MAGENTA,
    CYAN, GREEN, RED, BLUE, WHITE, PURPLE, BLACK, LIGHTGRAY, PINK, DARKGRAY, ORANGE, or another
    combination of rgb arrays.

Preconditions: x, y, and r are floats or int with r being positive and the colors are rgb arrays.

Sample calls:
            DrawSun(0,0,5)
            DrawSun(0,0,5,CYAN,MAGENTA,ORANGE)
    """
    # The function body goes here:  
    DrawStar(x,y,r,c1,rotate=0.0)
    DrawStar(x,y,r,c2,rotate=48)
    DrawStar(x,y,r,c3,rotate=24)
    r=r*0.62
    DrawDisk(x,y,r,color=YELLOW,stroke=0)
    
    
#Application Script 
if __name__ == '__main__':
    """Creates one window with a sun with center at (0,0) and radius 5. Creates
    another window with a nested sun - a sun with center at (0,0) and radius 5,
    a smaller sun nested, fitting inside the bigger sun. In total, the nested sun
    has 6 suns, all at the center (0,0) and have the same ray color (cyan, magenta,
    and orange) but shifted clockwise one 'notch'.
    """
    r = 5.
    x = 0.
    y = 0.
    alpha = 0.62
    # My chosen ray colors
    c1 = CYAN
    c2 = MAGENTA
    c3 = ORANGE
    # Figure 1: A single sun
    n=6
    MakeWindow(n,labels=True,bgcolor=BLACK)  
    DrawSun(x,y,r,c1,c2,c3)
    # Figure 2: A nested sun
    #Sun 1
    MakeWindow(n,labels=True,bgcolor=BLACK)
    DrawSun(x,y,r,c1,c2,c3)
    #Sun 2
    r=r*alpha
    DrawSun(x,y,r,c3,c1,c2)
    #Sun 3
    r=r*alpha
    DrawSun(x,y,r,c2,c3,c1)
    #Sun 4
    r=r*alpha
    DrawSun(x,y,r,c1,c2,c3)
    #Sun 5
    r=r*alpha
    DrawSun(x,y,r,c3,c1,c2)
    #Sun 6
    r=r*alpha
    DrawSun(x,y,r,c2,c3,c1)
    
    ShowWindow()
