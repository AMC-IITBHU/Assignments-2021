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
def demo(num):
    return num * num


number = float(input("please enter any numeric value:"))

sqre = demo(number)

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
def ispalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
       if not string[left_pos] == string[right_pos]:
           return False
       left_pos += 1
       right_pos -= 1
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
 def sqrt(n):
    if n < 0:
        return
    else:
        return n ** 0.5

print(sqrt(61))

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
     n = len(arr)
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [10, 324, 45]




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
def print2largest(arr, arr_size):
    if (arr_size < 2):
        print("Invalid Input")
        return

    arr.sort

    for i in range(arr_size-2, -1, -1):
        print("The second largest element is", arr[i])
        return


arr = [12, 35, 1, 10, 34, 1]

n = len(arr)
print2largest(arr, n)



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
A = np.array([[3, -9], [2, 4]])
b = np.array([-42, 2])
z = np.linalg.solve(A, b)
print(z)

M = np.array([[1, -2, -1], [2, 2, -1], [-1, -1, 2]])
c = np.array([6, 1, 1])
y = np.linalg.solve(M, c)
print(y)
