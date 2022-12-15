import turtle

george = turtle.Turtle('turtle') 

george.width(5)
george.color('blue')

for num in range(8):
    george.forward(70)
    george.left(90)
    print(num)

turtle.exitonclick()