from random import randint,choice
import pgzrun
WIDTH=800
HEIGHT=500

box1=Rect((100,100),(50,50)("red"))
box2=Rect((WIDTH-150,100),(50,50)("blue"))
box3=Rect(randint(100,700),randint(100,500),(10,200))

b1x=2
b2x=3
b3y=2

def draw():
    screen.clear()
    screen.filled_Rect(box1,"blue")
    screen.filled_Rect(box2,"red")
    screen.filled_Rect(box3,"green")
    screen.Rect_text(f'box1{b1x.x}| box2{b2x.x}|box3{b3y.y}'(10,10)"white")

def check_boundary(box,speed):
    if box.right>WIDTH or box.left<0:
        sounds.metal.play()
        return -speed
    re
