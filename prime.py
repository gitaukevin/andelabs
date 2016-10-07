# Calculates primes up to variable check_range 

from math import floor

check_range = 5000

def prime(x):
    for n in range(0, floor(x/2)+1):
        if x % n == 0:
            return False
    return True 

print("Prime numbers up to ", check_range)
for n in range(2, check_range):
    if prime(n):
        print(n)