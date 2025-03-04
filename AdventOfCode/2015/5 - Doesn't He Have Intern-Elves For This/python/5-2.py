
def main():
    niceCount = 0
    with open("input.txt") as f:
        line = f.readlines()
        for line in line:
            # Increment nice counter if all true
            if (twice_no_overlap(line) and sandwich_letters(line)):
                niceCount += 1

    # Print answer
    print(niceCount)

# Check if character pairs appear twice without overlap
def twice_no_overlap(string):
    has_repeating_pair = False 
    for i in range(len(string) - 1):
        pair = string[i:i+2] 
        # Check for overlap
        if string.find(pair,i+2) != -1:
            has_repeating_pair = True 
    return has_repeating_pair

# Check if there's a letter "sandwich" (personally coined term lol)
def sandwich_letters(string):
    has_repeat_with_gap = False
    for i in range(len(string) - 2):
        if (string[i] == string[i+2]):
            has_repeat_with_gap = True 
    return has_repeat_with_gap

if __name__ == "__main__":
    main()

            