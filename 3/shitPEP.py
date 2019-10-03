from graph import brushColor, polygon, randColor, \
                  windowSize, canvasSize, onTimer, run, penSize, penColor, line, circle, moveTo, \
                  lineTo, deleteObject, moveObjectBy

import math

# GLOBAL VARIABLES
# it's scale koef

k = 4

# standartIter

i = 0
j = 0

# It's eye's

obj1 = None
obj2 = None


# ##

# background gradient function (R: 0-225, G: 0-225, B: 0-225)

def gradient(R=225, G=0, B=0):
    i = 0
    global k
    penSize(1)
    R = R / (300 * k)
    G = G / (300 * k)
    B = B / (300 * k)
    print(R, G, B)
    while i < 300 * k:
        penColor(int(R * i) + 20, int(G * i) + 20, int(B * i) + 20)
        line(0, i, 200 * k, i)
        i += 1


# ##

# Spyral (koef:+/- change twist dir, X: X-cord, Y: Y-cord)

def spyral(koef=1, X=100, Y=150):
    penSize(10)
    moveTo(X * k, Y * k)
    j = 0
    while j < 360 * 4 * abs(koef):
        rho = j / 10 * koef / abs(koef)
        lineTo(100 * k + rho * math.sin(j / 360 * 3.14) + X * k - 100 * k,
150 * k + rho * math.cos(j / 360 * 3.14) + Y * k - 150 * k)
        j += 1
        if j % 30 == 0:
            penColor(randColor())


# ##

# Print some TUX UGLY LEGACY CODE ARHHHHHHHH

def printTUX():
    penColor('black')
    brushColor('black')
    global obj1
    global obj2
    circle(100 * k, 50 * k, 30 * k)
    circle(100 * k, 145 * k, 65 * k)
    polygon([(80 * k, 70 * k), (200 * k - 80 * k, 70 * k),
(200 * k- 55 * k, 100 * k), (55 * k, 100 * k)])
    brushColor('white')
    circle(100 * k, 145 * k, 57 * k)
    brushColor('yellow')
    penColor('yellow')
    circle(65 * k, 200 * k, 22 * k)
    circle(54 * k, 173 * k, 12 * k)
    circle(35 * k, 185 * k, 15 * k)
    circle(37 * k, 205 * k, 12 * k)

    circle(200 * k - 65 * k, 200 * k, 22 * k)
    circle(200 * k - 54 * k, 173 * k, 12 * k)
    circle(200 * k - 35 * k, 185 * k, 15 * k)
    circle(200 * k - 37 * k, 205 * k, 12 * k)

    brushColor('white')
    penColor('black')

    circle(88 * k, 50 * k, 10 * k)
    circle(200 * k - 88 * k, 50 * k, 10 * k)
    brushColor('red')
    circle(88 * k, 52 * k, 6 * k)
    circle(200 * k - 88 * k, 53.5 * k, 6 * k)
    brushColor('black')
    obj1 = circle(85 * k, 53 * k, 2 * k)
    obj2 = circle(200 * k - 85 * k, 52 * k, 2 * k)
    brushColor(252, 252, 12)
    polygon([(100 * k, 60 * k), (200 * k - 80 * k, 70 * k),
(100 * k, 80 * k), (80 * k, 70 * k)])
    brushColor(252, 156, 12)
    polygon([(100 * k, 72 * k), (200 * k - 80 * k, 70 * k),
(100 * k, 77 * k), (80 * k, 70 * k)])


# ##

# ## start main ###

# #init
print(123)
windowSize(200 * k, 300 * k)
canvasSize(200 * k, 300 * k)
print(321)
# print

gradient()
printTUX()
spyral()

# test code

obj = polygon([(50 * k, 50 * k), (150 * k, 50 * k),
(150 * k, 150 * k), (50 * k, 150 * k)])

# changeCoord(obj,[(x,y),(x,y)])
# Animation

i = 0


def update():
    global i
    global j
    global x1
    global y1
    global x2
    global y2
    i += 1
    if i >= 360:
        i = 0
    moveObjectBy(obj1, 13 * math.sin(i), 10 * math.cos(i))
    moveObjectBy(obj2, 7 * math.cos(i), 10 * math.sin(i))


# ##

deleteObject(obj)

onTimer(update, 100)

run()
