# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input
nums = list(map(int, input().split()))

# Use filter + lambda
primes = list(filter(lambda x: is_prime(x), nums))

if primes:
    print(" ".join(map(str, primes)))
else:
    print("No primes")