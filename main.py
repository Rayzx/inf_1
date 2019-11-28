import tkinter as tk
import math as m
import copy
import random

random.seed()

class Gun:
    def __init__(self,pos,mc,mw):
        self.pos = pos
        self.position = pos
        self.mc = mc
        self.mw = mw
        self.mw.guns.append(self)
        self.phi = 0
        self.cords = [self.position[0],self.position[1]-10,self.position[0]+50,self.position[1]-10,
                                      self.position[0]+50,self.position[1]+10,self.position[0],self.position[1]+10,
                                      self.position[0],self.position[1]-10]
        self.obj = mc.create_polygon(self.cords,fill = "green")

    def updateRot(self,posTo):
        self.phi = m.atan2((posTo[1]-self.pos[1]) , (posTo[0]-self.pos[0])) # y / x
        self.mc.delete(self.obj)
        phi = self.phi
        self.obj = mc.create_polygon([(self.cords[0]-self.pos[0])*m.cos(phi) - (self.cords[1]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[0]-self.pos[0])*m.sin(phi) + (self.cords[1]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[2]-self.pos[0])*m.cos(phi) - (self.cords[3]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[2]-self.pos[0])*m.sin(phi) + (self.cords[3]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[4]-self.pos[0])*m.cos(phi) - (self.cords[5]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[4]-self.pos[0])*m.sin(phi) + (self.cords[5]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[6]-self.pos[0])*m.cos(phi) - (self.cords[7]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[6]-self.pos[0])*m.sin(phi) + (self.cords[7]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[0]-self.pos[0])*m.cos(phi) - (self.cords[1]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[0]-self.pos[0])*m.sin(phi) + (self.cords[1]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      ], fill = "green")
        pass

    def updatePos(self):
        self.cords = [self.position[0],self.position[1]-10,self.position[0]+50,self.position[1]-10,
                      self.position[0]+50,self.position[1]+10,self.position[0],self.position[1]+10,
                      self.position[0],self.position[1]-10]
        self.mc.delete(self.obj)
        phi = self.phi
        self.obj = mc.create_polygon([(self.cords[0]-self.pos[0])*m.cos(phi) - (self.cords[1]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[0]-self.pos[0])*m.sin(phi) + (self.cords[1]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[2]-self.pos[0])*m.cos(phi) - (self.cords[3]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[2]-self.pos[0])*m.sin(phi) + (self.cords[3]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[4]-self.pos[0])*m.cos(phi) - (self.cords[5]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[4]-self.pos[0])*m.sin(phi) + (self.cords[5]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[6]-self.pos[0])*m.cos(phi) - (self.cords[7]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[6]-self.pos[0])*m.sin(phi) + (self.cords[7]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      (self.cords[0]-self.pos[0])*m.cos(phi) - (self.cords[1]-self.pos[1])*m.sin(phi) + self.pos[0],
                                      (self.cords[0]-self.pos[0])*m.sin(phi) + (self.cords[1]-self.pos[1])*m.cos(phi) + self.pos[1],
                                      ], fill = "green")

    def shoot(self):
        self.mw.bul.append( Bullet([70*m.cos(self.phi), 70*m.sin(self.phi)], [self.pos[0] + self.mw.camOffsetX , self.pos[1]]  , 3,self.mw,1 ) )



class Bullet:
    def __init__(self,vel,pos,accel,mw,cl):
        self.flag = 0
        self.cl = cl
        self.mw = mw
        self.kil = 0
        self.rp = copy.deepcopy(pos)
        self.velocity = copy.deepcopy(vel)
        self.position = copy.deepcopy(pos)
        self.accel = copy.deepcopy(accel)
        self.cords = [self.position[0]-10,self.position[1]-10,self.position[0]+10,self.position[1]-10,
                                      self.position[0]+10,self.position[1]+10,self.position[0]-10,self.position[1]+10,
                                      self.position[0]-10,self.position[1]-10]
        self.obj = mc.create_polygon(self.cords,fill = "red")

        print(self.rp, self.cl, self.position)

        pass

    def update(self):
        #print ("hello")
        if (self.kil == 0):
            self.position[0] += self.velocity[0] * 0.1
            self.rp[0] += self.velocity[0] * 0.1
            self.velocity[1] += self.accel*0.1
            self.position[1] += self.velocity[1] * 0.1
            self.rp[1] += self.velocity[1] * 0.1

            self.position = [ self.rp[0]-self.mw.camOffsetX , self.rp[1]+self.mw.camOffsetY  ]

            self.cords = [self.position[0]-10,self.position[1]-10,self.position[0]+10,self.position[1]-10,
                                          self.position[0]+10,self.position[1]+10,self.position[0]-10,self.position[1]+10,
                                          self.position[0]-10,self.position[1]-10]
            mc.delete(self.obj)
            self.obj = mc.create_polygon(self.cords,fill = "red")
            if (self.cl == 1):
                #print('test ', self.position)
                pw = 0
                pw = self.mw.wcc(self.rp)
                #mc.create_polygon([pw[0]-10,pw[1]-10,pw[0]+10,pw[1]-10,
                #                              pw[0]+10,pw[1]+10,pw[0]-10,pw[1]+10,
                #                              pw[0]-10,pw[1]-10] , fill = "green"


                #)

                if (self.mw.p == 1):
                    if (self.rp[0]<1900) and (self.rp[0]>1700) and (self.rp[1]<700) and (self.rp[1]>500):
                        print("YOU WIN PLAYER1")
                        self.flag = 1
                        self.mw.camlock = 1

                if (self.mw.p == 2):
                    print("YOU WIN PLAYER2")
                    if (self.rp[0]<400) and (self.rp[0]>200) and (self.rp[1]<700) and (self.rp[1]>500):
                        self.flag = 1
                        self.mw.camlock = 1


                self.mw.moveEnv(0, self.velocity[1] * -0.1)
                self.mw.moveEnv(self.velocity[0] * -0.1, 0)
                if pw == 1:
                    flag = 0
                    #self.mw.bul = list()
                    if (self.mw.p == 1):
                        if (self.position[0]<1830) and (self.position[0]>1770) and (self.position[1]<630) and (self.position[0]>570):
                            print("YOU WIN PLAYER1")
                            flag = 1
                            #  300 600 1800 600
                        for i in range(100):
                            self.mw.moveEnv(0,-10)
                            self.mw.moveEnv(-10,0)
                            self.mw.p = 2
                            self.mw.camlock = 0
                            self.kil = 1
                        if self.flag == 1:
                            self.mw.camlock = 1

                    else:
                        if (self.mw.p == 2):
                            if (self.position[0]<330) and (self.position[0]>270) and (self.position[1]<630) and (self.position[0]>570):
                                print("YOU WIN PLAYER2")
                                flag = 1
                            for i in range(100):
                                self.mw.moveEnv(0,-10)
                                self.mw.moveEnv(10,0)
                                self.mw.p = 1
                                self.mw.camlock = 0
                                self.kil = 1
                            if self.flag == 1:
                                self.mw.camlock = 1



        else:
            self.position = [ self.rp[0]-self.mw.camOffsetX , self.rp[1]+self.mw.camOffsetY  ]
            self.cords = [self.position[0]-10,self.position[1]-10,self.position[0]+10,self.position[1]-10,
                          self.position[0]+10,self.position[1]+10,self.position[0]-10,self.position[1]+10,
                          self.position[0]-10,self.position[1]-10]
            mc.delete(self.obj)
            self.obj = mc.create_polygon(self.cords,fill = "red")



class GameManager:
    def __init__(self, mc, root, mw):
        self.mc = mc
        self.root = root
        self.test = Bullet([0,0],[200,200],10,mw,0)
        self.mw = mw
        pass

    def runGame(self):
        self.root.mainloop()

    def eventTick(self):
        #print('tick')
        for i in self.mw.bul:
            i.update()
        self.test.update()
        self.root.after(10,self.eventTick)


class World:
    def __init__(self, mc):
        self.mc = mc
        self.wEnvironment = Environment(2000,700)
        self.oEnvironment = 0
        self.genEnv()#self.wEnvironment.canvasPoints())
        self.camOffsetX = 0
        self.camOffsetY = 0
        self.camlock = 0
        self.bul = list()
        self.guns = list()
        self.p = 1
        self.activeG = 0

    def genEnv(self):
        if ( self.oEnvironment != 0):
            self.mc.delete(self.oEnvironment)
        #print('creating')
        self.oEnvironment = self.mc.create_polygon(self.wEnvironment.canvasPoints(),fill = "black")

    def moveEnv(self,length,height):
        if (self.camOffsetX-length > 0 )and(self.camOffsetX-length<900)and(self.camOffsetY+height >= 0 ):
            self.camOffsetX = self.camOffsetX - length
            self.camOffsetY = self.camOffsetY + height
            self.wEnvironment.move(length,height)
            self.genEnv()
            for i in self.bul:
                i.position = [i.position[0] + length, i.position[1] + height]
            for i in self.guns:
                i.position = [i.position[0] + length, i.position[1] + height]
                i.pos = i.position
                i.updatePos()
    def wcc(self,pos1):
        #print ("new", pos1)
        return self.wEnvironment.checkCol(pos1)

class Environment:
    def __init__(self,length,countPoints):
        self.aPoints  = list()
        self.length = length
        self.countPoints = countPoints
        self.generate()
        self.raPoints = copy.deepcopy(self.aPoints)
        pass

    def generate(self):
        self.aPoints.append([0,1000])
        for i in range(self.countPoints):
            self.aPoints.append([ i*self.length/self.countPoints,
                                (m.sin(random.random()*3.14)*100
                                + m.sin(random.random()*3.14)*100)
                                *-3*m.exp(-(4*i/self.countPoints-2)**2) + 700 ]) #[x,y]
        self.aPoints.append([self.length,1000])
        self.aPoints.append(self.aPoints[0])
        self.countPoints += 3

    def move(self,length,height):
        for i in range(self.countPoints):
            self.aPoints[i][0] += length
            self.aPoints[i][1] += height

    def canvasPoints(self):
        lArr = list()
        for i in range(self.countPoints):
            for j in range(2):
                lArr.append(self.aPoints[i][j])
        return lArr

    def checkCol(self,pos):
        print(pos)

        if False: #((pos[0]<10)or(pos[0]>1900)):
            print('boooM!')
            return 1
        else:
            if pos[0]<1000:
                n1 = m.floor(pos[0]*(self.countPoints-3)/self.length+1)
                n2 = m.ceil(pos[0]*(self.countPoints-3)/self.length+1)
                p = self.raPoints
                if ( pos[1] > (pos[0])*(p[n2][1]-p[n1][1])/(p[n2][0]-p[n1][0])
                               + (p[n2][0]*p[n1][1]-p[n1][0]*p[n2][1])/(p[n2][0]-p[n1][0]) ):
                    print('boooM!')
                    return 1
            if pos[0]>=1000:
                n1 = m.floor(pos[0]*(self.countPoints-3)/self.length+1)
                n2 = m.ceil(pos[0]*(self.countPoints-3)/self.length+1)
                p = self.raPoints
                if ( pos[1] > (pos[0])*(p[n2][1]-p[n1][1])/(p[n2][0]-p[n1][0])
                               + (p[n2][0]*p[n1][1]-p[n1][0]*p[n2][1])/(p[n2][0]-p[n1][0]) ):
                    print('boooM!')
                    return 1
            # 300 600 1800 600


root = tk.Tk()
mc = tk.Canvas(root, width = 1000, height = 1000, bg = 'white')
mc.pack()


myWorld = World(mc)

p1Gun = Gun([300,600],mc, myWorld)
p2Gun = Gun([1800,600],mc, myWorld)
myWorld.camlock = 0


def eventLeft(event):
    global myWorld
    if (myWorld.camlock == 0):
        myWorld.moveEnv(20,0)
def eventUp(event):
    global myWorld
    if (myWorld.camlock == 0):
        myWorld.moveEnv(0,20)
def eventRight(event):
    global myWorld
    if (myWorld.camlock == 0):
        myWorld.moveEnv(-20,0)
def eventDown(event):
    global myWorld
    if (myWorld.camlock == 0):
        myWorld.moveEnv(0,-20)
def shoot(event):
    global myWorld
    if (myWorld.camlock == 0):
        global p1Gun
        print(myWorld.camlock)
        myWorld.camlock = 1
        print(myWorld.guns[1].pos)
        myWorld.guns[myWorld.p-1].shoot()
        print("hello12")



def motion(event):
    global myWorld
    global p1Gun
    x = event.x
    y = event.y
    myWorld.guns[myWorld.p-1].updateRot([x,y])
    #print('{}  {}'.format(x,y))


root.bind('<Button-1>',shoot)
root.bind('<d>',eventRight)
root.bind('<a>',eventLeft)
root.bind('<w>',eventUp)
root.bind('<s>',eventDown)
root.bind('<Motion>', motion)

for i in range(len(myWorld.wEnvironment.aPoints)):
    for j in range(2):
        print(myWorld.wEnvironment.aPoints[i][j])


myGame = GameManager(mc,root, myWorld)
myGame.eventTick()
myGame.runGame()
