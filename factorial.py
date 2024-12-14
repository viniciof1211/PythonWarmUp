# Both implementations (recursive and iterative) of factorial multiplication (it's dynamically typed)

def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result