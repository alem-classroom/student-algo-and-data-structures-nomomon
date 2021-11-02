def fib(num):
    # return n-th Fibonacci number

    # base case: n = 0
    if(num == 0):
        return 1
    # base case: n = 1
    if(num == 1):
        return 1
    
    # recursion
    return fib(num - 1) + fib(num - 2)