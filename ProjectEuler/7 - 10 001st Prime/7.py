'''
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that
the 6th prime is 13.

What is the 10,001st prime number?
'''
import math

def main():
    found, x, prime_counter = False,1,0
    while not found:
        x+=1
        if is_prime(x):
            prime_counter += 1
            if prime_counter == 10001:
                found = True
                print(x)
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()