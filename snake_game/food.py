from turtle import Turtle
import random
import turtle

turtle.colormode(255)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.7, 0.7)
        self.penup()
        self.color(self.random_color())
        self.speed("fastest")
        self.locate_food()

    def locate_food(self):
        x_coordinate = random.randint(-280,280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate,y_coordinate)

    def random_color(self):
        r = (random.randint(0, 255))
        g = (random.randint(0, 255))
        b = (random.randint(0, 255))
        color = (r, g, b)
        return color
