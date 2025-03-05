'''
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640. 

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''
# Sum of the squares of 100
def sum_of_squares(n):
    total_sum = 0
    for x in range(1,n+1):
        total_sum = total_sum + (x*x) 
    return total_sum

# Square of the sum of 0-100
def square_of_sums(n):
    total_sum = sum(range(0,n+1))
    return total_sum*total_sum

# Difference between sum of squares and square of sums
def main():
    print(square_of_sums(100) - sum_of_squares(100))

if __name__ == "__main__":
    main()

