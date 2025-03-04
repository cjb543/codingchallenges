def main():
        # Define the keypad layout
    keypad = [
        [None, None, '1', None, None],
        [None, '2', '3', '4', None],
        ['5', '6', '7', '8', '9'],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]

    # Define the starting position
    x, y = 0, 2

    # Define the movements
    movements = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    # Read the input from a file
    with open('input.txt') as f:
        instructions = f.read().strip().split('\n')

    # Process each line of instructions
    code = []
    for line in instructions:
        for move in line:
            dx, dy = movements[move]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 5 and 0 <= new_y < 5 and keypad[new_x][new_y] is not None:
                x, y = new_x, new_y
        # Add current digit to list "code"
        code.append(keypad[x][y])

    # Print the final code
    print(''.join(code))

# Mystical code of workingness (i dont know anymore)
if __name__ == "__main__":
    main()  