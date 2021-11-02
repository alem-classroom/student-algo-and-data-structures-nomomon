def fib(num):
    # return n-th Fibonacci number

    # base case: num == 0, num == 1
    if(num <= 1):
        return 1
    
    # recursion
    return fib(num - 1) + fib(num - 2)
