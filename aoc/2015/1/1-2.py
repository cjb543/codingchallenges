# Listless approach
def main():
    with open("1-input.txt") as f:
        data = f.read()
        count = 0
        position = 0
        for c in data:
            if c == '(':
                count+=1
                position+=1
            if c == ')':
                count-=1
                position+=1
            if count == -1:
                # Tracks every instance of when -1 is visited
                print(position)
    print("Floor landed on:", count)

if __name__ == "__main__":
    main()