import turtle as t 
import random
X_COR=-240
FONT=("Courier",24,"normal")
class MakeTurtle:
    def __init__(self,name,colour,shape,y_coord):
        self.tName=name
        self.name=t.Turtle()
        self.name.penup()
        self.name.color(colour)
        self.name.shape(shape)
        self.name.setposition(X_COR,y_coord)
        # print(name,colour,shape,y_coord)

    def moving(self):
        self.name.forward(random.randint(25,50))
    
    def xcord(self):
        return self.name.xcor()

    def ret_name(self):
        new_turtle=t.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.setposition(-80,0)        
        new_turtle.write("Game over!!!!\n   ",align="left",font=FONT)

    