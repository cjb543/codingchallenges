def main():
    totalSurfaceArea = 0
    with open("input.txt") as file:
        line = file.readline()
        while line:
            line = line.strip()
            parts = line.split('x')
            if len(parts) == 3:
                try:
                    l = int(parts[0])
                    w = int(parts[1])
                    h = int(parts[2])
                    side1 = l*w*2
                    side2 = w*h*2
                    side3 = h*l*2
                    area1 = l*w
                    area2 = l*h
                    area3 = w*h
                    smallestSide = min(area1,area2,area3)
                    totalSurfaceArea += (side1+side2+side3+smallestSide)
                except ValueError:
                    print(f"Failed to assign line to variables")
            line = file.readline()
    print(totalSurfaceArea)

if __name__ == "__main__":
    main()