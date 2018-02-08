# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:13:38 2018

@author: sandeela
"""

import turtle

def draw_upper(some_turtle):
    for i in range (1,4):
        some_turtle.backward(100)         
        some_turtle.left(90)
        
def draw_lower(some_turtle):
    for i in range (1,3):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def letter_S(some_turtle):
    draw_upper(some_turtle)
    draw_lower(some_turtle)
    
def letter_W(some_turtle):
    for i in range (1,3):
        some_turtle.right(-90)
        some_turtle.backward(100)
        some_turtle.right(45)
        some_turtle.forward(100)
  
def draw_art():    
    window = turtle.Screen()
    window.bgcolor("red")
    ben = turtle.Turtle()
    ben.color("yellow")
    ben.shape("turtle")
    letter_S(ben)
    
    ben1 = turtle.Turtle()
    ben1.color("yellow")
    ben1.shape("turtle")
    letter_W(ben1) 
    
    window.exitonclick()
    
draw_art()
    