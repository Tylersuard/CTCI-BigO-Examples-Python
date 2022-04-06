import math
def isPrime(n):
    top = int(math.sqrt(n))
    for i in range(2,top):
        if n % i == 0:
            return False
    return True
