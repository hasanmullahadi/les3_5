# see :
#  https://processing.org/reference/ellipseMode_.html
# will make a calass for the object and has it atributes in it, then have multipe 
# bouncing around



from ball import *

balls = []
noo = 5
def setup():
    size(800,600)
    for i in range(noo):
        balls.append(Ball(random(width),random(height),random(10),random(10),random(100)))
    
    
def draw():
     background(254)
     for a_ball in balls:
         a_ball.display()
    
    
