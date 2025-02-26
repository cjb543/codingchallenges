def main():
    totalSurfaceArea = 0
    totalRibbonNeeded = 0

    # Open file
    with open("input.txt") as file:
        line = file.readline()
        while line:
            # Strip whitespace from lines (not needed but good practice)
            line = line.strip()

            # Divide values into list according to 'x'
            parts = line.split('x')

            if len(parts) == 3:
                try:
                    # Find side dimensions
                    l = int(parts[0])
                    w = int(parts[1])
                    h = int(parts[2])
                    sideList = [l,w,h]
                    # Calculate surface areas
                    side1 = l*w*2
                    side2 = w*h*2
                    side3 = h*l*2

                    # Find smallest value and second smallest value to find
                    # smallest perimeter
                    firstMinSide = min(l,w,h)
                    secondMinSide = sorted(sideList)[1]
                    smallestPerimeter = 2*firstMinSide + 2*secondMinSide
                    bowRibbon = l*w*h 
                    totalRibbonNeeded += bowRibbon+smallestPerimeter 

                    # Find areas and smallest side for extra paper needed
                    area1 = l*w
                    area2 = l*h
                    area3 = w*h
                    smallestSide = min(area1,area2,area3)

                    # Calculate 2-1 solution
                    totalSurfaceArea += (side1+side2+side3+smallestSide)

                # Error-checking
                except ValueError:
                    print(f"Failed to assign line to variables")

            line = file.readline()

    # 2-1 Solution
    print(totalSurfaceArea)

    # 2-2 Solution
    print(totalRibbonNeeded)
if __name__ == "__main__":
    main()