# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint
import parser
from math import sin
from decimal import Decimal



formula = "sin(x)*x^2"
formula = formula.replace("^","**")

def slope():
    functie = input("type your function\n")
    functie = functie.replace("^","**")
    startingX = input("type your X\n")
    length = len(startingX)
    startingX = int(startingX)
    dx = 10**-(12 - length)
    lowX = startingX
    highX = startingX + dx
    x = lowX
    compiledF = parser.expr(functie).compile()
    lowY = eval(compiledF)
    x = highX
    highY = eval(compiledF)
    dy = highY - lowY
    dydx = dy / dx
    print(dydx)

slope()