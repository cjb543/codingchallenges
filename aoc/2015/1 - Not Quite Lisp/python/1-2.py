# Listless approach
def main():
    with open("input.txt") as f:
        # Read input file and assign to a string
        data = f.read()

        # Track Santa's current floor
        floor = 0

        # Track the number of floors Santa has visited
        count = 0

        # Loop through file's data
        for c in data:
            if c == '(':
                floor+=1
                count+=1
            if c == ')':
                floor-=1
                count+=1
            if floor == -1:
                # Print every instance of when floor -1 is visited
                print("Santa reached the basement in position:", count)
    print("Floor landed on:", floor)
if __name__ == "__main__":
    main()