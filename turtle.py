def square():
	turtle.forward(500)
	turtle.left(90)
	turtle.forward(500)
	turtle.left(90)
	turtle.forward(500)
	turtle.left(90)
	turtle.forward(500)
	turtle.left(90)
def a():
	square()
	turtle.left(20)
import turtle
turtle.color("red")
turtle.shape("turtle")
turtle.left(20)
for i in range(18):
	a()
turtle.exitonclick()