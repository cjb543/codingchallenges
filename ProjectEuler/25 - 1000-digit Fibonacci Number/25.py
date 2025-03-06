def main():
    # Tracking number itself
    index = 2

    # Fib minions
    a,b = 1,2

    # Do Fib sequence until number is 1k digits
    while len(str(a)) < 1000:
        
        # Actual fibonacci operation
        a,b = b,a+b

        # Increment index
        index += 1
    
    # Print result
    print(index)

# Boilerplate
if __name__ == "__main__":
    main()