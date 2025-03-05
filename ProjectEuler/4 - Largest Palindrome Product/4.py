'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Is the number a palindrome?
def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def main():
    largest_palindrome = 0 
    for i in range(100,1000):
        for j in range(100,1000):
            product = i*j 
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    print(largest_palindrome)

if __name__ == "__main__":
    main()
