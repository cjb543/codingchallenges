import math

'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

def main():
    print(smallest_multiple(20))

if __name__ == "__main__":
    main()