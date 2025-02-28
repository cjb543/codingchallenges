def main():

# New way to parse these files :D
    with open("input.txt") as f:
        directions = f.read().strip()
    x_santa, y_santa = 0,0
    x_robo, y_robo = 0,0
    visited_houses = [(0,0)]

    for i, move in enumerate(directions):
        if i % 2 == 0:
            if move == '^':
                y_santa += 1
            elif move == 'v':
                y_santa -= 1
            elif move == '>':
                x_santa += 1
            elif move == '<':
                x_santa -= 1
            visited_houses.append((x_santa,y_santa))
        else:
            if move == '^':
                y_robo += 1
            elif move == 'v':
                y_robo -= 1
            elif move == '>':
                x_robo += 1
            elif move == '<':
                x_robo -= 1
            visited_houses.append((x_robo,y_robo))
        
    unique_houses = set(visited_houses)
    print (len(unique_houses))

if __name__ == "__main__":
    main()