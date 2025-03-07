def main():
    possible_counter = 0
    # Open file
    with open("input.txt") as file:
        for line in file:
            sides = [int(x) for x in line.split()]
            if (sides[0] + sides[1] > sides[2] and 
                sides[0] + sides[2] > sides[1] and 
                sides[1] + sides[2] > sides[0]):
                possible_counter+=1
    
    print(possible_counter)

        

if __name__ == "__main__":
    main()