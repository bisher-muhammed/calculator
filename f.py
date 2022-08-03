from turtle import*
clear()
pensize(3)
clr=("red","yellow","green","black","pink")
for i in clr:
   right(60)
   color("red",i)
   begin_fill()
   for j in range(5):
      forward(100)
      right(72)
   end_fill()
input()

