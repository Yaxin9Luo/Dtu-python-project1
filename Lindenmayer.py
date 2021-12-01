#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 08:15:53 2021

@author: luoyaxin
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt

def LindIter(System, N):
    if System=='Koch':
        new='S'
        for i in range(N):
            new=new.replace('S','SLSRSLS')
    elif System=='Sierpinski':
        new='A'
        for i in range(N):
           working = list(new)
           for j in range (len(working)):
               if working[j]=='A':
                   working[j]='BRARB'
               elif working[j]=='B':
                   working[j]='ALBLA'
           new=''.join(working) 
           
    else:
        print('Wrong type of system')
    LindenmayerString=new
    return LindenmayerString


def turtleGraph(LindenmayerString):
    if 'A' and 'B' not in LindenmayerString:
        num_S = LindenmayerString.count('S')
        s = num_S
        p = 1
        while s / 4 != 1:
            p += 1
            s = s/4
        length = (1/3)**p
        linden = LindenmayerString[:-1]
        turtleCommands = []
        for character in linden:
            if character == 'S':
                turtleCommands.append(length)
            elif character == 'L':
                turtleCommands.append(m.pi/3)
            elif character == 'R':
                turtleCommands.append(-2*m.pi/3)
        #print(linden,turtleCommands)
    elif 'A' or 'B' in LindenmayerString:
       # print(LindenmayerString)
        num_S = LindenmayerString.count('A')+LindenmayerString.count('B')
        s = num_S
        p = 1
        while s / 3 != 1:
            p += 1
            s = s/3
        length = (1/2)**p
        linden = LindenmayerString[:-1]
        #print(linden)
        turtleCommands = []
        for character in linden:
            if character == 'A':
                turtleCommands.append(length)
            elif character == 'B':
                turtleCommands.append(length)
            elif character == 'L':
                turtleCommands.append(m.pi/3)
            elif character == 'R':
                turtleCommands.append(-m.pi/3)
    return turtleCommands

def turtlePlot(turtleCommands):
    #print(len(turtleCommands))
    x = np.ones(shape=(int(len(turtleCommands)/2) + 2,2))
    d = np.ones(shape=(int(len(turtleCommands)/2) + 2,2))
    #print(d)
    loop = len(d)
    #print(loop)
    d[0] = [1,0]
    d[1] = [1,0]
    #print(d)
    x[0] = [0,0]
    x[1] = [turtleCommands[0],0]
    #print(x)
    #print(x[0][0])
    #print(turtleCommands)
    for i in range(1,loop-1):
        index = abs(2*i-1)
        angle = turtleCommands[index]
        #print(angle)
        d[i+1] = np.array([[m.cos(angle),-m.sin(angle)],[m.sin(angle),m.cos(angle)]])@d[i]
        #print(d[i+1])
        x[i+1] = x[i] + turtleCommands[0]*d[i+1]
        #print(i)
    #d2 = d1[0]*np.array([cos(v2),sin(v2)])+d1[0]*np.array([-sin(v2),cos(v2)])
    #x2 = x1 + l2*d2
    points = x
    x_axis = points[:,0]
    y_axis = points[:,1]
    plt.plot(x_axis,y_axis)
    plt.show()
###############################################################################
def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number
    #
    # Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
    # number. Repeats until user inputs a valid number.
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num
def displayMenu(options):
    # DISPLAYMENU Displays a menu of options, ask the user to choose an item
    # and returns the number of the menu item chosen.
    #
    # Usage: choice = displayMenu(options)
    #
    # Input    options   Menu options (array of strings)
    # Output   choice    Chosen option (integer)
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice
menu_item = np.array(["Choose the type of Lindenmayer system and the number of iterations.", "Generate plots", "Quit"])
Lindenmayer_options = np.array(["Koch curve","Sierpinski triangle"])
while True:
    choice = displayMenu(menu_item)
    if choice == 1:
        options = displayMenu(Lindenmayer_options)
        if options == 1:
            system_name = 'Koch'
        elif options == 2:
            system_name = 'Sierpinski'
        iteration = int(input("Please enter an iteration number you want:"))
        while iteration > 10:
            iteration = int(input("Please choose a number smaller than 10:"))
    elif choice == 2:
        plt.title(system_name)
        turtlePlot(turtleGraph(LindIter(system_name,iteration)))
    elif choice == 3:
        break





#print(turtlePlot(turtleGraph(LindIter('Sierpinski',10))))
