import pgzrun

WIDTH=400
HEIGHT=500

width=100
height=200

def draw():
    screen.clear()
    screen.fill("white")

    rect=Rect((150,100),(width,height))

    screen.draw.circle((150,100),100,"red")
    screen.draw.rect(rect,"blue")
    screen.draw.line((125,400),(350,400),"green")   

pgzrun.go()    
