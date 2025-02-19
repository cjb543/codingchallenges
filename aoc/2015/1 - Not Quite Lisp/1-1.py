def main():
    with open("1-input.txt") as f:
        data = f.read()
        count = 0
        for c in data:
            if c == '(':
                count+=1
            if c == ')':
                count-=1
    print(count)


if __name__ == "__main__":
    main()