# import pgzrun 
# class Robot(Actor):
#     frame =0
#     speed = 5
#     def __init__(self, imglist, **Kwargs):
#         super().__init__(imglist[0])
#         self.imglist=imglist
#     def walk(self):
#         self.image=self.imglist[self.frame]
#         print((self.frame + 1)%len(self.imglist))
#         self.frame=(self.frame +1) % len(self.imglist)
#         if self.left < 0 or self.right > WIDTH:
#            self.speed = -self.speed
#         self.x +=self.speed
  
# HEIGHT=400
# WIDTH=600
# r=Robot(['w0','w1','w2','w3','w4','w5','w6'],center=(100,100))
# def draw():
#     screen.clear()
#     r.draw()
# def update():
#      r.walk()
# pgzrun.go()   

import pgzrun
class Robot(Actor):
    frame=0
    speed=5
    def __init__(self, imglist,**kwargs):
        super().__init__ (imglist[0])
        self.imglist=imglist

    def walk(self):
        self.image=self.imglist[self.frame]
        print(self.frame+1) % len(self.imglist) 
        self.frame=(self.frame+1)%len(self.imglist)
        if self.left < 0 or self.right > WIDTH:
            self.speed=-self.speed
        self.x +=self.speed 

HIGHT=500
WIDTH=600
r=Robot(['w0','w1','w2','w3','w4','w5','w6'],center=(100,100))

def draw():
    screen.clear()
    r.draw()
def update():
    r.walk()
pgzrun.go()
    