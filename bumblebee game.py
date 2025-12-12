import pgzrun
import random
WIDTH=600
HEIGHT= 400
bee=Actor("bee")
flower=Actor("flower")
flower.x=random.randint(0,600)
flower.y=random.randint(0,400)
game=True

bee.x=300
bee.y=200
def draw():
    screen.blit("field",(0,0))
    flower.draw()
    bee.draw()
def update():
    if keyboard.w:
        bee.y-=5
    if keyboard.s:
        bee.y+=5
    if keyboard.a:
        bee.x-=5
    if keyboard.d:
        bee.x+=5
pgzrun.go()
