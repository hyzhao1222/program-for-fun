from turtle import *
speed(100)
r=3
pu()
goto(0,-300)
pd()
for i in range(40):
    r+=1
    for a in range(r):
        forward(30)
        left(360/r)
    goto(0,-300)
done()