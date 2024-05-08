# Fibonacci numbers module

a, b = 0, 1

def fib(n):    # write Fibonacci series up to n
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
