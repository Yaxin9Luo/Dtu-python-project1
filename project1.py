import matplotlib.pyplot as plt
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
################################################################################
################################################################################
"""dataStatistics function
author: Yaxin Luo, Oleg Minchev, Haoyang Yao."""
def dataStatistics(data, statistic):
    '''input data: An N by 3 matrix with columns Temperature,Growth rate and Bacteria
input statistic: A string specofying the statistic that should be calculated
output result: A scalar containg the calculated statistic'''
    lower_statistic = statistic.lower() #navoid users' typing errors
    temperatures = data[:,0]
    growth_rates = data[:,1]
    less,high = mean_grow_depends_tem(data)
    if lower_statistic == 'mean temperature':
        result = np.mean(temperatures)
    elif lower_statistic == 'mean growth rate':
        result = np.mean(growth_rates)
    elif lower_statistic == 'std temperature':
        result = np.std(temperatures)
    elif lower_statistic == 'std growth rate':
        result = np.std(growth_rates)
    elif lower_statistic == 'rows':
        result = rows_total(data)
    elif lower_statistic == 'mean cold growth rate':
        result = less
    elif lower_statistic == 'mean hot growth rate':
        result = high
    else:
        print("Error message, please check your tpying of statistic")
    return result

def rows_total(data):
    ''' calculate number of rows in any matrix'''
    number = 0
    for rows in data:
        number += 1
    return number
def mean_grow_depends_tem(data):
    '''  '''
    less20_result = 0
    more50_result = 0
    for rows in data:
        if rows[0] < 20:
            less20_result += rows[1]
        elif rows[0] > 50:
            more50_result += rows[1]
        else:
            pass
    return np.mean(less20_result),np.mean(more50_result)
################################################################################
################################################################################
"""
dataPlot function
author: Yaxin Luo, Oleg Minchev,Haoyang Yao.
"""
def dataPlot(data):




    """Bacteria type grpah"""
    x_axis = np.array(['Salmonella enterica','Bacillus cereus', 'Listeria',\
    'Brochothrix thermosphacta'])
    bacteria = data[:,2]
    bacteria1 = np.count_nonzero(bacteria == 1)
    bacteria2 = np.count_nonzero(bacteria == 2)
    bacteria3 = np.count_nonzero(bacteria == 3)
    bacteria4 = np.count_nonzero(bacteria == 4)
    y_axis = np.array([bacteria1, bacteria2, bacteria3, bacteria4])
    plt.bar(x_axis, y_axis)
    plt.title('Number of bacteria')
    plt.xlabel('name of each bacteria')
    plt.ylabel('number of each bacteria')
    plt.show()
###############################################################################
    """Growth rate grpah"""
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.xlim([10, 60])
    plt.ylim([0,np.max(data[:,1])])
    #defining coordinates
    x1 = (data[:,0][data[:,2]==1])
    y1 = (data[:,1][data[:,2]==1])

    x2 = (data[:,0][data[:,2]==2])
    y2 = (data[:,1][data[:,2]==2])

    x3 = (data[:,0][data[:,2]==3])
    y3 = (data[:,1][data[:,2]==3])

    x4 = (data[:,0][data[:,2]==4])
    y4 = (data[:,1][data[:,2]==4])
    plt.scatter(x1, y1, c = 'blue') # Plot line graph of x and y
    plt.scatter(x2, y2, c = 'hotpink')
    plt.scatter(x3, y3, c = 'black')
    plt.scatter(x4, y4, c = 'red')
    plt.legend([" Salmonella enterica", "Bacillus cereus",'Listeria','Brochothrix thermosphacta'])
    plt.title('Growth rate by temperature')
    plt.show()
################################################################################
################################################################################
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
################################################################################
################################################################################
menu_item = np.array(["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])
while True:
    choice = displayMenu(menu_item)
    if choice == 1:
        while True:
            try:
                filename = str(input("Please enter the file name:"))
                break
            except ValueError:
                print("Not Valid file name. Please try again.")
        data = dataload(filename)
    elif choice == 2:
        data = dataload(filename)
        while True:
            try:
                Bacteria_type = str(input("Please specify Bacteria Type: Bacteria = "))
                break
            except ValueError:
                print("Not valid bacteria name. Please try again")
        while True:
            try:
                min_growthRate = float(input("lower bound of growth rate:"))
                break
            except ValueError:
                print("Not valid lower bound. Please try again")
        while True:
            try:
                max_growthRate = float(input("upper bound of growth rate:"))
                break
            except ValueError:
                print("Not valid upper bound. Please try again")
        print("Bacteria type is {:s}".format(Bacteria_type))
        print("range of Growth rate is {:f} <= Growth rate <= {:f}"\
        .format(min_growthRate,max_growthRate))
        Bacteria = np.array(['Salmonella enterica','Bacillus cereus', 'Listeria',\
        'Brochothrix thermosphacta'])
        type_number = np.where(Bacteria == Bacteria_type)
        type_number = int(type_number[0])+1
        data = (data[:,:][data[:,1] >= min_growthRate])
        data = (data[:,:][data[:,1] <= max_growthRate])
        data = (data[:,:][data[:,2] == type_number])
    elif choice == 3:
        while True:
            try:
                statistic = str(input("Which kind of statistic you want to display: "))
                break
            except ValueError:
                print("Not Valid statistic type. Please try again.")
        display_stat = dataStatistics(data, statistic)
        print("{:s} is {:f}".format(statistic,display_stat))
    elif choice == 4:
        dataPlot(data)
    elif choice == 5:
        break
