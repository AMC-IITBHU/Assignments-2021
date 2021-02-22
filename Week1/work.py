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
    x=[]
    for i in range(len(string)):
		x.append(string[len(string)-i-1])
    if x.all()==string.all():
    	return True
    else:
    	return False

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    ## Code Here
    return sqroot(num)

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
    arr.sort(reverse=True)
    max1=arr[0]
    max2=arr[1]
    	
    return max1,max2;

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
    
    for i in range(len(arr)): 
    	 arr.append(int(input()))
	arr.sort()
	arrev=[]
	arrod=[]
	for i in range(x): 
    	 if arr[i]%2==0:
    	 	arrev.append(arr[i])
    	 else:
    	 	arrod.append(arr[i])
    arr1=np.concatenate(arrev,arrod)
    	 	
    return arr1


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
    
    x=float((B[1]*C[0] - B[0]*C[1])/(A[0]*B[1] - A[1]*B[0]))
    y=float((A[1]*C[0] - A[0]*C[1])/(A[1]*B[0] - A[0]*B[1])))
    return x,y;
