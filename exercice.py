#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from ch6 import histogramme
import turtle

# TODO: Importez vos modules ici
def ellipse(a = 8, b = 9, c = 22):
    mass_volum = 1
    volume = 4/3 * (math.pi) * a * b * c
    mass = volume/mass_volum
    
    return volume, mass
    

# TODO: Définissez vos fonction ici 
'''
def frequence_trie(histogramme: dict, sentence: str) -> tuple:
    dict_sequence = {}
    list_letter = sorted(histogramme(sequence).item(), reverse= True, key= lambda x:x[1])

    for i in range(len(list_letter)):
        dict_sequence[list_letter[i][0] = list_letter[i][1]]

    return list_letter[0][0], dict_sequence[list_letter[0][0]]
'''
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
        
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
        

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    volume, mass = ellipse(a = 10, b = 22, c = 33)
    print (volume, mass)
    main()

