import turtle
import subprocess, sys

def draw_square(some_turtle):
	for i in xrange(0,4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_shapes():
	opener ="open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, "I like to move it.mp3"])
	window = turtle.Screen()
	window.bgcolor("white")
	leonardo = turtle.Turtle()
	leonardo.shape("turtle")
	opener ="open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, "I like to move it.mp3"])
	for i in xrange(0,36):
		draw_square(leonardo)
		leonardo.right(10)
	window.exitonclick()


draw_shapes()