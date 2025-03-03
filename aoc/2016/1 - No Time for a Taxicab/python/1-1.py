def main():
    # Open file with error checking
    try:
        with open("input.txt") as f:
             # Read file, strip whitespace, split with delimiter
            directions = f.read().strip().split(", ")
             # If the file is read and "directions" are present
            if directions:
                # Assign each direction to a "tokens" list. Each element accessible via token[index][1-2]
                tokens = [(d[0], int(d[1:])) for d in directions]

                # Initialize starting point and direction (facing north)
                x, y = 0, 0
                direction = 0  # 0: North, 1: East, 2: South, 3: West

                # Define movement vectors for each direction
                movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                # Process each token
                for turn, steps in tokens:
                    # Update direction based on turn
                    if turn == 'R':
                        direction = (direction + 1) % 4
                    elif turn == 'L':
                        direction = (direction - 1) % 4

                    # Move in the current direction
                    dx, dy = movements[direction]
                    x += dx * steps
                    y += dy * steps

                # Calculate and print the Manhattan distance
                distance = abs(x) + abs(y)
                print(f"Manhattan distance: {distance}")
                
            else:
                print("The file is empty or not in the expected format.") # Error check 1 - File is empty/wrong
    except FileNotFoundError:
        print("The file 'input.txt' was not found.") # Error check 2 - File is absent
    except Exception as e:
        print(f"An error occurred: {e}") # Error check 3 - Something else is broken. Generic error provided {e}

# Prevent execution when imported
if __name__ == "__main__":
    main()