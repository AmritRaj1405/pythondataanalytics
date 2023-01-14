import pgzrun
HEIGHT=500
WIDTH=800
p=Actor('ironman',center=(400,250))
b_vx=4

def draw():
    screen.clear()
    p.draw()

def update():
    global b_vx
    p.x +=0
    if p.x > WIDTH:
        p.x= 2
    elif p.x > WIDTH:
        p.x= -1
    elif p.right > WIDTH or p.left<0:
        b_vx= -b_vx
    elif p.left > WIDTH:
        b_vx= -b_vx
    if WIDTH > 800:
         p.x= 0
    if keyboard.left:
        p.x -=5
        p.angle = 10
    elif keyboard.right:
        p.x +=5
        p.angle = -10
    elif keyboard.up:
        p.y -=5
    elif keyboard.down:
        p.y +=5
    else:
        p.angle=0
pgzrun.go()