# Solution: 88811886
import re
def main():
    enabled = True
    total = 0

    # Open file
    with open("input.txt") as f:
        # Read file into contents
        contents = f.read()

        # Create regex pattern to only search for "mul(#,#)" with do or dont prefixes
        # New concept: Regex grouping, grouping regex with findall returns tuples ? XD
        mul_string2 = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

        # Create list of all "mul(#,#)" instances
        matches = re.findall(mul_string2,contents)

        # Add to final sum and print
        final_sum = 0
        for a,b,do,dont in matches:
            if do or dont:
                enabled = bool(do)
            else:
                x = int(a) * int(b)
                total += x * enabled
        print(total)
if __name__ == "__main__":
    main()