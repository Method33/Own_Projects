def factorial(n):
    # The factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # The factorial of n is n times the factorial of (n-1)
        return n * factorial(n-1)
