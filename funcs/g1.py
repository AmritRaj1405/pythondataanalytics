import pgzrun

HEIGHT =500
WIDTH= 500
#rect with 100 * 100 size and 0,0 coordinates
rect=Rect((0,0),(100,100))

rect2=Rect((250,250),(100,100))

def draw():
    screen.fill('yellow')
    screen.draw.filled_rect(rect,'red')
    screen.draw.filled_rect(rect2,'blue')
#code will here 
pgzrun.go()
