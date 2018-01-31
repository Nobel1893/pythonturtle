import turtle


def drawSquare(myturtle):    
    myturtle.speed(2)
    myturtle.color("red")

    myturtle.shape('circle')
    i=0
    while i < 4:
        myturtle.forward(100)
        myturtle.left(90)
        i+=1
    
def drawcircle(myturtle):
    myturtle.shape('turtle')
    myturtle.color("yellow")
    myturtle.circle(50)


def drawtriangle(myturtle):
    myturtle.color("orange")
    i=0
    while i < 4:
        if i % 2==0:
            myturtle.forward(100)
        else :
            myturtle.forward(100*2)

        myturtle.left(90)
        i+=1

def init ():
    myturtle = turtle.Turtle()
    screen = turtle.Screen()
    myturtle.pensize(5)
    screen.bgcolor("black")
    drawcircle(myturtle)
    myturtle.left(10)
    drawSquare(myturtle)
    myturtle.left(20)
    drawtriangle(myturtle)
    screen.exitonclick()

init()
