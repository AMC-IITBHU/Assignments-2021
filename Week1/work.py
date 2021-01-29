import math
import numpy as np

def demo(x):
    '''
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        x*x (int)
    '''
    return x*x

def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''
    string = string.upper()
    new_string = string[::-1]
    if string == new_string :
        result = True
    else:
        result = False
    return result
import cmath
def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''
    if num >= 0 :
        result = num**0.5 
    else:
        result = cmath.sqrt(num)
    return result

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''
    arr.sort()
    return (arr[-1],arr[-2])
    
def even_sort(arr):
    '''
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    '''
    new1 = []
    new2 = []
    for i in arr:
        if i % 2 == 0:
            new1.append(i)
        else:
            new2.append(i)
    new1.sort()
    new2.sort()
    return new1 + new2

def eqn_solver(A, B, C):
    '''
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    '''
    x = [A[0] , B[0]]
    y = [A[1] , B[1]]
    a = np.array([x, y])
    b = np.array(C)
    result = np.linalg.solve(a,b)
    return (round(result[0],1), round(result[1],1)) 
