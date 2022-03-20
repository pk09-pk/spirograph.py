import random
import turtle as t

tim = t.Turtle()
colours = ["light steel blue","dark green","lime","peru","red","magenta","grey"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)