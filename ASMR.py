import turtle
import random
import time


turtle.getscreen()
time.sleep(1)
turtle.speed(1500)

tmp = 0
tmp2 = 0
rand = random.randint(10, 120)
rand2 = random.randint(1, 180)
rand3 = random.randint(10, 150)

while tmp2 < random.randint(1, 10):
    while tmp < rand3:
        turtle.forward(100)
        turtle.left(rand)
        turtle.forward(100)
        turtle.left(rand)
        turtle.forward(100)
        turtle.left(rand)
        turtle.forward(100)
        turtle.left(rand2)
        tmp += 1
    
    if tmp == rand3:
        turtle.up()
        turtle.forward(100)
        turtle.left(90)
        turtle.down()
        tmp = 0
        tmp2 += 1
time.sleep(10)