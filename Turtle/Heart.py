import turtle
userName = "We Love\nYou"
#userName = input("Please enter your name\n--> ")

def createHeart(turt, x = 0, y = 0, speed = 1, length = 150):
    turtle.Screen().bgcolor("Black")

    turt.speed(0)
    turt.penup()
    turt.setx(x)
    turt.sety(y)
    turt.pendown()
    turt.speed(speed)

    turt.color("#d60841")
    turt.pencolor("#d60841")

    def half():
        turt.left(45)
        turt.forward(length)
        turt.circle(length / 2, 180)

    def otherHalf():
        turt.right(90)
        turt.circle(length / 2, 180)
        turt.forward(length)

    turt.begin_fill()
    half()
    otherHalf()
    turt.end_fill()

def createName(turt, name, x = 0, y = 0):
    turt.up()
    turt.setx(x)
    turt.sety(y)
    turt.down()

    turt.color("#2c2c2c")
    name = name
    style = ("Arial", 30, "italic")
    turt.write(name, font = style, align = "center")

love = turtle.Turtle()
name = turtle.Turtle()

love.speed(1)
love.shape("turtle")
love.resizemode("auto")

createHeart(love)
createName(name, userName, 0, 90)


turtle.exitonclick()
