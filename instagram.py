from turtle import *

speed(1000)
pensize(20)


# # gradient color to be applied
#
#
def outer_border(x, y, f, c1, c2):
    color('white')
    setposition(x, y)
    color('purple')
    for i in range(4):
        forward(f)
        circle(c1, c2)

#
# outer_border(-110, -90, 260, 50, 90)
# pendown()
# color('transparent')
# setposition(0, 0)
# color('purple')
# circle(100)
#
# hideturtle()
# done()


# c = (0.60156, 0, 0.99218)
# t = (0.86320, 0.47656, 0.31250)
# screen = Screen()
# turtle = Turtle()
# turtle.color(c)
#
# deltas = [(hue-c[index]) / (window_height() * 2) for index, hue in enumerate(t)]
# width, height = screen.window_width(), screen.window_height()
# penup()
# goto(100, -1)
# pendown()
#
# direction = 1
# for d, y in enumerate(range(200, 0, -1)):
#     forward(1 * direction)
#     color(tuple([c[i] + delta*d for i, delta in enumerate(deltas)]))
#     sety(y)
#     direction *= -1
#
# right(90)
# for d, y in enumerate(range(200, 0, -1)):
#     right(90)
#     forward(1 * direction)
#     color(tuple([c[i] + delta*d for i, delta in enumerate(deltas)]))
#     sety(y)
#     direction *= -1
#
# right(90)
# for d, y in enumerate(range(200, 0, -1)):
#     forward(1 * direction)
#     color(tuple([c[i] + delta*d for i, delta in enumerate(deltas)]))
#     sety(y)
#     direction *= -1
#
# right(90)
# for d, y in enumerate(range(200, 0, -1)):
#     forward(1 * direction)
#     color(tuple([c[i] + delta*d for i, delta in enumerate(deltas)]))
#     sety(y)
#     direction *= -1

right(90)

done()
