#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:08:26 2021

@author: luoyaxin
"""
import numpy as np
def dataload(filename):
    '''load the data from file contains Bacteria Data we need.
       input filename: A string containing the filename of a data file.
       output data is a N*3 Matrix.
    '''
    lines_array = read_txt_1dimArray(filename)
    matrix = convert_filelines_matrix(lines_array) # convert the array from line 16 into a N*M matrix
    data = handle_data_errors(matrix) #use handle_data_errors funtion to detele line does not satisfy condtions
    return data

def read_txt_1dimArray(filename):
    ''' read all the lines of any an arbitrary txt file into an array'''
    filein = open(filename, "r") # Opens the file for reading
    lines_array = filein.readlines()   # Reads all lines into an array
    return lines_array
def convert_filelines_matrix(lines):
    ''' convert whole lines array of a text file into N*N array.
        input lines should be a 1 dimensional array read from all lines of the file.
        output should be a N*M array of the data read from file.
    '''
    list = []
    for line in lines: # operations line by line
        stripped_line = line.strip() # strip all the blankspaces between each line
        line_list = stripped_line.split() # split each stripped_line into a list item
        list.append(line_list) # add each line item into empty list
    matrix = np.asarray(list) # convert list to array format
    return matrix
def handle_data_errors(matrixname):
    ''' Accessing each row of a matrix given by users and check the data of matrix
    whether satisfiies the requirements. If not, delete that row.
    input matrixname variable is an array.
    output data is an new array which has already deleted the rows do not need.
    '''
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
            print("The number {} represents the type of Bacteria which is not \
in one our types, hence we delte line {}".format(Bacteria,index_line))
        else:
            data.append(array) # the line pass all conditions check, add it to the data matrix we want to return
        index_line += 1 # next line
    data = np.asarray(data)
    data = data.astype(float) #convert elements in data from string to float
    return data
