# Come back to this in 3 months and see how much you progressed. - Chris

def main():
    vowelCount,niceCount = 0,0
    vowelCheck, doubleCheck, badCheck = False, False, False

    with open("input.txt") as f:
        line = f.readlines()
        for c in line:

            # Handle Vowel Check
            if (isVowel(c)):
                vowelCount += 1
                if (vowelCount >= 3):
                    vowelCheck = True

            # Handle Double Check 
            if (c == c.next()):
                doubleCheck = True

            # Handle Bad String Check
            if (c + c.next() == "ab" or c + c.next() == "cd" or c + c.next() == "pq" or c + c.next() == "xy"):
                badCheck = True

            # Increment nice counter if all true
            if (vowelCheck and doubleCheck and not badCheck):
                niceCount += 1

    # Print answer
    print(niceCount)

def isVowel(c):
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


            