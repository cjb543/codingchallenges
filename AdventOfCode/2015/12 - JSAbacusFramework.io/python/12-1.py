import re
def main():
    with open("input.txt") as file:
        contents = file.read()
        print(sum(map(int, re.findall(r'-?\d+', contents))))

if __name__ == "__main__":
    main()