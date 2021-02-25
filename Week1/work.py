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
#y=6
#print (demo(9))
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
    for i in range(0,len(string)):
        if string[i] != string[len(string)-i-1]:
            return 0



    return 1
'''
s1='n mam n'
print(is_palindrome(s1))
'''
def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''
    s=math.sqrt(num)
    ## Code Here
    return s
#print (sqrt_of_numbers(101))
def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''
   # numpy.zeros(shape, dtype=float, order='C', *, like=None)¶

    y=arr[0]
    z=y
    for i in arr:
        if i>y:
            z=y
            y=i



    ## Code Here
    return y,z
#arr=[1,4,5,6,777,9999]
#print(Maximum(arr))
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
    a1=[]
    a2=[]
    for i in arr:
        if(i%2==0):
            a1.append(i)

        else:
            a2.append(i)

    a1.sort()
    a2.sort()
   ## np.concatenate((a1,a2),axis=0)

    ## Code Here
    return (a1+a2)
#    a=a.append([i])

#arr=[0,1,2,4,6,3,234324,34]
#print( even_sort(arr))

def eqn_solver(a, b, c):
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
    x=(c[0]*b[1]-b[0]*c[1])/(a[0]*b[1]-a[1]*b[0])
    y=(a[0]*c[1]-a[1]*c[0])/(a[0]*b[1]-a[1]*b[0])
    ## Code Here
    return x,y
'''
a=[12,2]
b=[3,-3]
c=[15,13]
print(eqn_solver(a, b, c))
'''
