# see :
#  https://processing.org/reference/ellipseMode_.html
# will make a calass for the object and has it atributes in it, then have multipe 
# bouncing around



class obj:
    def __init__(self,x = 0, y = 0,vx = 0, vy = 0,dia =0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.dia = dia
        self.rbg = [random(255),random(255),255]
        self.checkInitialCondition()
    
    def checkInitialCondition(self):
        if self.x+self.dia >width:
            self.x-=self.dia
        if self.x<0:
            self.x = 0
        if self.y+self.dia >height:
            self.y-=self.dia
        if self.y<0:
            self.y = 0
       
    def display(self):
        ellipseMode(CORNER)
        self.x +=self.vx
        self.y +=self.vy
        if self.x+self.dia>=width or self.x<=0:
            self.vx *= -1
        if self.y+self.dia >= height or self.y<=0:
            self.vy *= -1
    
        fill(self.rbg[0],self.rbg[1],self.rbg[2])
        ellipse(self.x,self.y,self.dia,self.dia)
        


c = []
noo = 5
def setup():
    size(800,600)
    for i in range(noo):
        c.append(obj(random(width),random(height),random(10),random(10),random(100)))
    
    
def draw():
     background(254)
     for i in c:
         i.display()
    
    
