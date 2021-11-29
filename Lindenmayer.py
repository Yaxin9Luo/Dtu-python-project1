#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 08:15:53 2021

@author: luoyaxin
"""
import math as m
from fractions import Fraction
def LindIter(System, N):
    '''a  '''    
    if System=='Koch':
        new='S'
        for i in range(N):
            new=new.replace('S','SLSRSLS')
    elif System=='Sierpinski':
        new='A'
        for i in range(N):
            if len(new) > 1:
                new= new.replace('A','BRARB') 
                new= new.replace('B','ALBLA')
            elif len(new) == 1:
                new = new.replace('A','BRARB')
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
        turtleCommands = [length,0]
        for character in linden:
            if character == 'S':
                turtleCommands.append(length)
            elif character == 'L':
                turtleCommands.append(-m.pi/3)
            elif character == 'R':
                turtleCommands.append(2*m.pi/3)
        print(linden,turtleCommands)
    elif 'A' or 'B' in LindenmayerString:
        print(LindenmayerString)
        

print(turtleGraph(LindIter('Sierpinski',2)))
print(len('A'))