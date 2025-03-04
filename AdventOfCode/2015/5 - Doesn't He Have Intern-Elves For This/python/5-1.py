
def main():
    niceCount = 0
    with open("input.txt") as f:
        line = f.readlines()
        for line in line:
            # Handle Vowel Check
            vowel_count = sum(1 for c in line if is_vowel(c))
            has_three_vowels = vowel_count >= 3

            # Handle Double Check 
            has_double = any(line[i] == line[i+1] for i in range(len(line)-1))

            # Handle Bad String Check
            has_bad = any(bad in line for bad in["ab","cd","pq","xy"])

            # Increment nice counter if all true
            if (has_three_vowels and has_double and not has_bad):
                niceCount += 1

    # Print answer
    print(niceCount)

def is_vowel(c):
    return c in "aeiou"


if __name__ == "__main__":
    main()

            