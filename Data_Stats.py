import numpy as np
def dataStatistics(data, statistic):
'''

input data: An N by 3 matrix with columns Temperature,Growth rate and Bacteria
input statistic: A string specofying the statistic that should be calculated

output result: A scalar containg the calculated statistic


'''
    lower_statistic = lower(statistic) #navoid users' typing errors
    temperatures = data[:,0]
    growth_rates = data[:,1]
    less,high = mean_grow_depends_tem(data)
    if lower_statistic == 'mean temperature':
        result = np.mean(temperature)
    elif lower_statistic == 'mean growth rate':
        reslut = np.mean(growth_rate)
    elif lower_statistic == 'std temperature':
        reslut = np.std(temperature)
    elif lower_statistic = 'std growth rate':
        reslut = np.std(growth_rate)
    elif lower_statistic = 'rows':
        return rows_total(data)
    elif lower_statistic = 'mean cold growth rate':
        reslut = less
    elif lower_statistic = 'mean hot growth rate':
        reslut = high
    else:
        print("Error message, please check your tpying of statistic")
    return reslut

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
            less_result += rows[1]
        elif rows[0] > 50:
            more50_result += rows[1]
        else:
            pass
    return np.mean(less20_result),np.mean(more50_result)
