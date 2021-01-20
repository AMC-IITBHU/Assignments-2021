import work

funcs = [work.demo, work.is_palindrome, work.sqrt_of_numbers, work.Maximum, work.even_sort, work.eqn_solver]
debug = False
test_cases = {}     ## Will be filled after submission date

score = 0

for func in funcs:
    flag = 1
    for i,test_case in enumerate(test_cases[func.__name__]):
        x, y = test_case
        try:
            assert y==func(*x)
        except Exception as e:
            flag = 1
            print("function "+func.__name__+" fails on testcase "+str(i+1),end="")
            if debug:
                print("because ")
                print(e)
            else:
                print("")
    score += flag

print("Your score is "+str(score)+"!!, You will receive extra points for smart implementation directly in the pull request")
