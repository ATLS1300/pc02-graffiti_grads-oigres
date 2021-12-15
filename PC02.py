#!/usr/bin/env python
# coding: utf-8

# '''
# Turtle starter code
# ATLS 1300
# Author: Dr. Z
# Author: YOUR NAME
# May 29, 2020
# '''

# Create a panel to draw on. 
import turtle #import the library of commands that you'd like to use
panel = turtle.Screen()
w = 650 # width of panel
h = 650 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Create a colorful background and add Bezos image to it

image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)


#=======Add your code here======


#Tortuga Bebe
turtle.hideturtle()
turtle.penup() 


tortuga_bebe = turtle.setpos(-19,90)
tortuga_bebe = turtle.begin_fill()
tortuga_bebe = turtle.circle(25)
tortuga_bebe = turtle.color("blue")
tortuga_bebe = turtle.end_fill()

tortuga_bebe2 = turtle.setpos(50,99)
tortuga_bebe2 = turtle.begin_fill()
tortuga_bebe2 = turtle.circle(25)
tortuga_bebe2 = turtle.color("green")
tortuga_bebe2 = turtle.end_fill()

tortuga_bebe3 = turtle.st()
tortuga_bebe3 = turtle.color("purple")
tortuga_bebe3 = turtle.shapesize(4,10,20)
tortuga_bebe = turtle.setpos(89,60)
tortuga_bebe3 = turtle.settiltangle(-20)
tortuga_bebe3 = turtle.dot(45, "red")



turtle.pendown() 
    

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
