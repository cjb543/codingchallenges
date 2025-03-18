import re
def main():
    # Open file
    with open("input.txt") as f:
        # Read file into contents
        contents = f.read()
        
        # Create regex pattern to only search for "mul(#,#)"
        mul_string = r'mul\((-?\d+(\.\d+)?),(-?\d+(\.\d+)?)\)'

        # Create list of all "mul(#,#)" instances
        matches = re.findall(mul_string,contents)

        # Add to final sum and print
        final_sum = 0
        for match in matches:
            final_sum += int(match[0]) * int(match[2])
        print(final_sum)

if __name__ == "__main__":
    main()