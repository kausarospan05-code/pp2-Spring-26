# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):#prime factors 2,3,5
        if n % i == 0:
            return False
    return True

# Input
nums = list(map(int, input().split()))

#Usefilter + lambda
primes = list(filter(lambda x: is_prime(x), nums))
# әр елементке ламбда функциясын колданад filter
#бір жолда шағын функция құруға мүмкіндік береді
#lambda is a way to create a short, anonymous function — a function without a name.
if primes:
    print(" ".join(map(str, primes)))#бос орынмен болып шыгарады
else:
    print("No primes")