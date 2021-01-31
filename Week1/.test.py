import work
import numpy as np
funcs = [work.demo, work.is_palindrome, work.sqrt_of_numbers, work.Maximum, work.even_sort, work.eqn_solver]
debug = False
test_cases = {
        'demo' : [
                    [[1],1],
                    [[-1],1],
                    [[2],4],
                    [[5],25],
                    [[2.5],6.25],
                    [[0.3],0.09]
                    ],
        'is_palindrome' : [
                            [ ['malayalam'], True ],
                            [['Racecar'],True],
                            [['bobby'],False],
                            [['AbaBa'],True],
                            [['poppins'],False],
                            [['MadamiamadaM'],False]
                            ],
        'sqrt_of_numbers' : [
                                [ [1], 1.0],
                                [ [56], 7.483314773547883],
                                [ [0.3], 0.5477225575051661 ],
                                [ [25], 5.0],
                                [ [-1], complex(0,1)]
                                ],
        'Maximum' : [
                        [ [[0,1,2]], (2,1) ],
                        [ [[-5,2,7,1,0]], (7,2)],
                        [ [[-1,-1,-1,-1,-1]], (-1,-1)],
                        [ [[1,2,9,8,9]], (9,9)],
                        [ [[2,-2,-2,-2,0]], (2,0)],
                        ],
        'even_sort' : [
                        [ [[1,2,3,4]], [2,4,1,3] ],
                        [ [[0,5,-1,2,8,3,7,8,55,4]], [0,2,4,8,8,-1,3,5,7,55]],
                        [ [[-5,-5,-3,-7,8]], [8,-7,-5,-5,-3]],
                        [ [[0,0,0,0,0,0,0,0]], [0,0,0,0,0,0,0,0]],
                        [ [[1,6,9,2.5,2,8,4,-1.5]], [2,4,6,8,-1.5,1,2.5,9]],
                        ],
        'eqn_solver' : [
                        [ [[1,2],[3,4],[0,0]], (0,0) ],
                        [ [[2,6],[10,20],[29,61]], (1.5,2.6)],
                        [ [[1,2],[-5,1],[10,-13]], (-5,-3)],
                        [ [[4,8],[7,6],[58.5,69.8]], (4.3,5.9)],
                        [ [[4,2],[8,5],[12,7]], (1,1)]
                        ],
    }     ## Will be filled after submission date

score = 0

for func in funcs:
    flag = 1
    for i,test_case in enumerate(test_cases[func.__name__]):
        x, y = test_case
        try:
            if func.__name__ == 'eqn_solver':
                np.testing.assert_allclose( y, func(*x) )
            else:
                assert y==func(*x)
        except Exception as e:
            flag = 0
            print("function "+func.__name__+" fails on testcase "+str(i+1),end="")
            if debug:
                print("because ")
                print(e)
            else:
                print("")
    if flag==1:
        print("function "+func.__name__+" passes all the test cases!")
    score += flag

print("Your score is "+str(score)+"!!,\nYou will receive extra points for smart implementation directly on the pull request")
if score!=len(funcs):
    raise Exception("Did not pass all tests")
