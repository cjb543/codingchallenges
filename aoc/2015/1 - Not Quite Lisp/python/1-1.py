def main():
    with open("1-input.txt") as f:
        # Read input file and assign to a string
        data = f.read()

        # Track Santa's position
        position = 0
        for c in data:
            if c == '(':
                position+=1
            if c == ')':
                position-=1
    
    # Print Santa's position
    print(position)
if __name__ == "__main__":
    main()