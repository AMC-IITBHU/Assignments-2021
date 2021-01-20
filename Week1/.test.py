import work

funcs = [work.demo, work.is_palindrome, work.sqrt_of_numbers, work.Maximum, work.even_sort, work.eqn_solver]
debug = False
test_cases = {
        'demo' : [
                    [ [1], 1],
                    ],
        'is_palindrome' : [
                            [ ['malayalam'], True ],
                            ],
        'sqrt_of_numbers' : [
                                [ [1], 1 ],
                                ],
        'Maximum' : [
                        [ [[0,1,2]], (2,1) ],
                        ],
        'even_sort' : [
                        [ [[1,2,3,4]], [2,4,1,3] ],
                        ],
        'eqn_solver' : [
                        [ [[1,2],[3,4],[0,0]], (0,0) ],
                        ],
    }     ## Will be filled after submission date

score = 0

for func in funcs:
    flag = 1
    for i,test_case in enumerate(test_cases[func.__name__]):
        x, y = test_case
        try:
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
