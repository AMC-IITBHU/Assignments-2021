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
    return x ** 2


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
    string_reversed=string[::-1].lower()              #Reversing the string and converting it into lower case
    if string_reversed==string.lower():               #converting the string to lower case to check it against the string_reversed
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
    if num>0:
        square_root=math.sqrt(num)
        return square_root
    else:
        return "Cannot find square root of a negative number"



def Maximum(arr):
    '''
    This function returns first maximum and the second minimum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

    ## Code Here
    arr.sort(reverse=True)
    print(arr)
    if len(arr)>=2:
        for n in range(1,len(arr)):           #checking if the array contains maximum number more than once so that Max2 is different than Max1
            if arr[0]!=arr[n]:
                Max1=arr[0]
                Max2=arr[n]
                break
    else:
        return "Array contains less than 2 numbers"

    return Max1,Max2






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
    arr.sort()
    even_numbers_list = []
    for number in arr:
        if number % 2 == 0:
            even_numbers_list.append(number)
    odd_numbers_list = []
    for number in arr:
        if not number % 2 == 0:
            odd_numbers_list.append(number)

    final_list = even_numbers_list + odd_numbers_list

    return final_list




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
    try:                                                       #Checking for the exception when the equations have no solution
        a = np.array([A, B])
        b = np.array(C)
        solution = np.linalg.solve(a, b)
        x=solution[0]
        y=solution[1]
        return x,y
    except:
        return "The equations have no solution"



