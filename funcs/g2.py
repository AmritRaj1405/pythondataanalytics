import pgzrun

width=800
height=500

square=Rect((400, 250),(50, 50))
b=Rect((200, 250),(50,50))#for new square
b_vx=4 #this is global variable ,this is the speed of the box you can change this 


def draw():
    screen.clear()
    screen.draw.filled_rect(square, 'red')
    screen.draw.filled_rect(b,'blue')#for new square color 

# def update():#update funcs update the screen every milllseconds
#     if square.right < width:#it will touch the right edge and stop
#         square.x +=1
#         square.inflate_ip(0,1)#inflate phulata h ,ip=inplace increase pixels(shape)
#         print(square.x)

# pgzrun.go()

#screen per chalta rhega  
# def update():   
#     square.x +=2
#     if square.x>width:
#         square.x=0
#     pgzrun.go()

def update():
    global b_vx #this allows us to change the value of b_vx
    #loop around the screen
    square.x +=2
    if square.x>width:
        square.x=0
    # bounce the box
    b.x +=b_vx   #this  is used to touch the border of screen and back
    if b.right > width or  b.left<0:
        b_vx= -b_vx #invert the direction of the box
pgzrun.go()