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
    matrix = np.asarray(list) # convert list to array format
    data = handle_data_errors(matrixname = matrix) #use handle_data_errors funtion to detele line does not satisfy condtions
    return data

def handle_data_errors(matrixname):
    data = []
    index_line = 0 # count for which line we are in
    for array in matrixname: # acess in each row in our matrix
        Temperature = float(array[0]) # first element is Temperature
        Growth_rate = float(array[1])
        Bacteria = int(array[2])
        if Temperature <= 10.0 and Temperature >= 60.0: # Check the conditions for Temperature
            print("the value of Temperature: {} is out of range,\
we delte line {}".format(Temperature,index_line)) # If ture, print error messeage
        elif Growth_rate  <= 0:
            print("Growth rate: {} must be positive we delte line {}".\
format(Growth_rate,index_line))
        elif Bacteria not in range(1,5):
            print("The number :{} represents the type of Bacteria is not \
in one our types we delte line {}".format(Bacteria,index_line))
        else:
            data.append(array) # the line pass all conditions check, add it to the data matrix we want to return
        index_line += 1 # next line
    data = np.asarray(data)
    return data
