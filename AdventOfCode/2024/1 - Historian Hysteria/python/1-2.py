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
        list2.sort()
        list3.sort()
        list2 = [int(x) for x in list2]
        list3 = [int(x) for x in list3]

        similarity_score = 0
        for num in list2:
            similarity_mulitplier = list3.count(num)
            similarity_score += num*similarity_mulitplier
        print(similarity_score)


if __name__ == "__main__":
    main()
