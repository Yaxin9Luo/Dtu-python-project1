#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:08:26 2021

@author: luoyaxin
"""
import numpy as np
def dataload(filename):
    '''load the data from file contains Bacteria Data we need
       input filename: A string containing the filename of a data file.
       output data is a N*3 Matrix
    '''
    
    filein = open(filename, "r") 
    lines = filein.readlines() 
    list = []
    for line in lines: # operations line by line
        stripped_line = line.strip() # strip all the blankspaces between each line
        line_list = stripped_line.split() # split each stripped_line into a list item
        list.append(line_list) # add each line item into empty list 
        data = np.asarray(list) # convert list to array format
    return data
    
print(dataload('test.txt'))
