import re
def main():
    with open("input.txt") as f:
        contents = f.read()
        mul_string = r'mul\((-?\d+(\.\d+)?),(-?\d+(\.\d+)?)\)'
        matches = re.findall(mul_string,contents)
        final_sum = 0
        for match in matches:
            final_sum += int(match[0]) * int(match[2])
        
        print(final_sum)

if __name__ == "__main__":
    main()