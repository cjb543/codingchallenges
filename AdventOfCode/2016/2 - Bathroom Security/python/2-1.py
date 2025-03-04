def main():
    x,y=0,0
    with open("input.txt") as f:
        line = f.readline()
        while line:
            line = line.strip()
            # Solution
            for direction in line:
                if direction == "U" and y<1:
                    y+=1
                elif direction == "D" and y>-1: 
                    y-=1
                elif direction == "L" and x>-1: 
                    x-=1
                elif direction == "R" and x<1:
                    x+=1
            line = f.readline()
            print(f"{x,y}")

# Mystical code of workingness (i dont know anymore)
if __name__ == "__main__":
    main()