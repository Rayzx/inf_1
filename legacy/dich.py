from graph import *
import math
"""
penColor(255,0,255)
penSize(5)
brushColor("blue")
rectangle(100, 100, 300, 200)
brushColor("yellow")
polygon([(100,100), (200,50),
         (300,100), (100,100)])
penColor("white")
brushColor("green")
circle(200, 150, 50)

"""
i = 0 


k = 4

penSize(1)
while i < 300*k:
    c = 225/((300*k))
    penColor(int(c*i)+30,0,0)
    line(0,i,200*k,i)
    i+=1

penColor("black")
windowSize(200*k,300*k)
canvasSize(200*k,300*k)
brushColor("black")
circle(100*k,50*k,30*k)
circle(100*k,145*k,65*k)
polygon([(80*k,70*k),(200*k-80*k,70*k),(200*k-55*k,100*k),(55*k,100*k)])
brushColor("white")
circle(100*k,145*k,57*k)
brushColor("yellow")
penColor("yellow")
circle(65*k,200*k,22*k)
circle(54*k,173*k,12*k)
circle(35*k,185*k,15*k)
circle(37*k,205*k,12*k)

circle(200*k-65*k,200*k,22*k)
circle(200*k-54*k,173*k,12*k)
circle(200*k-35*k,185*k,15*k)
circle(200*k-37*k,205*k,12*k)

brushColor("white")
penColor("black")

circle(88*k,50*k,10*k)
circle(200*k-88*k,50*k,10*k)
brushColor("red")
circle(88*k,52*k,6*k)
circle(200*k-88*k,53.5*k,6*k)
brushColor("black")
obj1 = circle(85*k,53*k,2*k)
obj2 = circle(200*k-85*k,52*k,2*k)


brushColor(252,252,12)
polygon([(100*k,60*k),(200*k-80*k,70*k),(100*k,80*k),(80*k,70*k)])
brushColor(252,156,12)
polygon([(100*k,72*k),(200*k-80*k,70*k),(100*k,77*k),(80*k,70*k)])


#polygon([(150,315),(350,315),(350,350),(150,350)])
#polygon([(70,90),(220,180),(220,200),(70,110)])
#polygon([(400,90),(400,100),(300,170),(300,110)])

penColor("black")
penSize(10)
moveTo(100*k,150*k)
j=0

while j < 360*4:
    rho=j/10
    lineTo(100*k+rho*math.sin(j/360*3.14),150*k+rho*math.cos(j/360*3.14))
    j+=1
    if j % 30 == 0:
        penColor(randColor())
i=0
def update():
    global i
    global j
    i +=1
    if i>=360:
        i=0
    moveObjectBy(obj1,10*math.sin(i),10*math.cos(i))
    moveObjectBy(obj2,10*math.cos(i),10*math.sin(i))
    
   
    
onTimer(update,100)
run()
