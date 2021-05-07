import CreateTurtle
from turtle import Screen
y=-200
tim=CreateTurtle.MakeTurtle("tim","red","turtle",y)
y+=120
tim.take_name()
rim=CreateTurtle.MakeTurtle("rim","black","turtle",y)
y+=120
vim=CreateTurtle.MakeTurtle("vim","violet","turtle",y)
y+=120
sim=CreateTurtle.MakeTurtle("sim","green","turtle",y)
loop=True

while loop:
    if rim.xcord()>=250 or sim.xcord()>=250 or tim.xcord()>=250 or vim.xcord()>=250:
        loop=False 
    else:
        rim.moving()
        tim.moving()
        sim.moving()
        vim.moving()
if rim.xcord()>sim.xcord() and rim.xcord()>tim.xcord() and rim.xcord()>vim.xcord():
    # print(rim.ret_name()
     rim.ret_name()
elif sim.xcord()>rim.xcord() and sim.xcord()>tim.xcord() and sim.xcord()>vim.xcord():
    # print(sim.ret_name())
     sim.ret_name()
elif tim.xcord()>rim.xcord() and tim.xcord()>tim.xcord() and tim.xcord()>vim.xcord():
    # print(tim.ret_name())
     tim.ret_name()
else:
    # print(vim.ret_name())
     vim.ret_name()


# tim=turtle.Turtle()
# rim=turtle.Turtle()
# sim=turtle.Turtle()
# vim=turtle.Turtle()

# tim.penup()
# vim.penup()
# rim.penup()
# sim.penup()

# tim.shape("turtle")
# tim.color("red")
# sim.shape("turtle")
# sim.color("pink")
# rim.shape("turtle")
# rim.color("green")
# vim.shape("turtle")
# tim.setposition(x,y)
# y+=120
# rim.setposition(x,y)
# y+=120
# sim.setposition(x,y)
# y+=120
# vim.setposition(x,y)

# COLORS={
#     "tim":"red",
#     "sim":"black",
#     "rim":"orange",
#     "vim":"green"
# }
# for colors in COLORS:   
#     t_color=COLORS[colors]
#     colors=turtle.Turtle()
#     colors.penup()
#     colors.shape("turtle")
#     colors.setposition(x,y)
#     colors.color(t_color)
#     y+=120


# loop=True
# while loop:
#     if rim.xcor()>=250 or sim.xcor()>=250 or tim.xcor()>=250 or vim.xcor()>=250:
#         loop=False 
#     else:
#         moving(rim)
#         moving(sim)
#         moving(vim)
#         moving(tim)

# if rim.xcor()>
Screen().exitonclick()