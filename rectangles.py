import pgzrun
import random
WIDTH=600
HEIGHT= 800
def draw():
    r=255
    g=20
    b=random.randint(100,255)
    screen.fill("black")
    w=600
    h=50
    for i in range(50):
        r1=Rect((0,0),(w,h))
        r1.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(r1,(r,g,b))
        w=w-15
        h=h+15
        r-=2
        g+=2
def update():
        pass



pgzrun.go()
