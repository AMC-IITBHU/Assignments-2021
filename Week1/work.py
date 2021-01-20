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

    ## Code Here
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

    ## Code Here
    if string.lower() == string[::-1].lower():
        return True

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    ## Code Here
    if num >= 0:
        sqroot = float(num**0.5)
        return sqroot
    else:
        return None

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

    ## Code Here
    if arr.__len__() >= 2:
        arr.sort(reverse=True)
        return arr[0], arr[1]
    else:
        return None

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

    ## Code Here
    even_array = list(i for i in arr if i % 2 == 0)
    odd_array = list(i for i in arr if not i % 2 == 0)
    even_array.sort()
    odd_array.sort()
    sort_arr = even_array + odd_array
    return sort_arr


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

    ## Code Here
    coeff = np.vstack((A, B)).transpose()
    det = np.linalg.det(coeff)
    if not det == 0:
        inv = np.linalg.inv(coeff)
        eqn = np.array(C, dtype=float).transpose()
        var = np.matmul(inv, eqn)
        return var[0], var[1]
    else:
        return None
