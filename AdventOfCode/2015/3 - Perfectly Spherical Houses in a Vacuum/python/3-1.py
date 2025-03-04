def main():

# New way to parse these files :D
    with open("input.txt") as f:
        directions = f.read().strip()

    x,y = 0,0
    visited_houses = [(x,y)]

    for move in directions:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1        
        visited_houses.append((x,y))

    unique_houses = set(visited_houses)
    print (len(unique_houses))

if __name__ == "__main__":
    main()
