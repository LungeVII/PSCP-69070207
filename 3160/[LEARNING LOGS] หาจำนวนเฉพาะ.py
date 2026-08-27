"""kkk"""
import math

def is_prime(n):
    """kkk"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n % 2 :
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if not n % i :
            return False
    return True

start, end = map(int, input().split())

primes = [num for num in range(start, end + 1) if is_prime(num)]

m = len(primes)

if not m:
    print(f"Total primes: {len(primes)}")
else:
    print(*primes)
    print(f"Total primes: {len(primes)}")
