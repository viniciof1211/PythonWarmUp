import io 


def FizzBuzz(n):
    # One liner: Time O(n) / Space O(n)
    return ["FizzBuzz," if i % 15 == 0 else "Fizz," if i % 3 == 0 else "Buzz," if i % 5 == 0 else i for i in range(0, n)]
    # Time O(n) but Space O(1) / Constant
