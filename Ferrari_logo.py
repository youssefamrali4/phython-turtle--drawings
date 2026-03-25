import turtle

def draw_rectangle(color,x,y,width,height):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    # turtle.color(color)
    
    # Drawing the rectangle
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()


def setup_env():
    screen = turtle.Screen()
    screen.bgcolor("red")
    screen.title("Ferrari Logo - Youssef")
    turtle.speed(5)


def write_logo_name():
    #draw ferrari text placeholder
    turtle.penup()
    turtle.goto(30,-100)
    turtle.pendown()
    turtle.color("black")
    style=("cursiv",50,"bold")
    turtle.write("Ferrari",font=style,align="center")

    turtle.penup()
    turtle.pensize(8)
    turtle.goto(-50, -39.5)
    turtle.pendown()
    turtle.forward(160)






    



setup_env()


draw_rectangle('yellow',-100, -100, 250, 300)

draw_rectangle('red', -100, 200, 250, 15)
draw_rectangle('white',-100, 215, 250, 15)
draw_rectangle('green',-100, 230, 250, 15)

write_logo_name() 



turtle.done()



    