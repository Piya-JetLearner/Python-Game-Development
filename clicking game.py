import pgzrun
import random
score=0
WIDTH=600
HEIGHT= 500
hp=Actor("harry potter clipart")
hp.x=300
hp.y=250
hg=Actor("hermione granger clipart")
def draw():
    screen.fill("pink")
    hp.draw()
    hg.draw()
    screen.draw.text("click me",(100,100))
    screen.draw.text(f"score={score}",(450,30))
    
def on_mouse_down(pos):
    global score
    print(pos)
    if hp.collidepoint(pos):
        hp.x= random.randint(50,500)
        hp.y= random.randint(50,250)
        score=score+1
def spawn_hg():
    hg.x=random.randint(50,500)
    hg.y=random.randint(50,250)
clock.schedule_interval(spawn_hg,1.5)   

    





pgzrun.go()