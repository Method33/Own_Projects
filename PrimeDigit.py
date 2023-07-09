def is_prime(n):
    # Numbers less than or equal to 1 are not considered prime numbers
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    elif n <= 3:
        return True
    # Any number divisible by 2 or 3 is not a prime number
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # Start the counter i from 5
    i = 5
    # If a number n is not a prime, it can be factored into two factors a and b
    # If a and b are both greater than the square root of n, a*b would be greater than n. 
    # So at least one of those factors must be less or equal to the square root of n, and to check if n is prime, we can check for factors less than or equal to the square root.
    while i * i <= n:
        # n is divisible by i or i + 2, it is not a prime number
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # increment the counter i by 6
        i += 6
    # If no factor found, it is a prime number
    return True
