'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million.
'''
import math
def main():
    finalSum = 0
    for x in range(2000000):
        if is_prime(x):
            finalSum += x
    print(finalSum)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()