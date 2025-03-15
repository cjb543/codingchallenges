def main():

    # Open file
    with open("input.txt") as f:
        # Read entire file to contents variable
        contents = f.read()

        list1,list2,list3 = [],[],[]

        # Process into 2 separate lists
        for num in contents.split():
            list1.append(num)
        for x in list1[::2]:
            list2.append(x)
        for x in list1[1::2]:
            list3.append(x) 
 
        # List 2 = Left Column
        # List 3 = Right Column
        final_sum = 0
        list2.sort()
        list3.sort()
        list2 = [int(x) for x in list2]
        list3 = [int(x) for x in list3]

        i = 0
        for num in list2:
            final_sum += abs(num - list3[i])
            i+=1

        print(final_sum)


if __name__ == "__main__":
    main()