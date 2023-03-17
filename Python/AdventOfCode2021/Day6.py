
with open('/home/natha/Documents/python/AdventOfCode/assets/Day6.txt', 'r') as f:

    # Doesn't do the last set of items
    sum = 0
    setOfAnswers = set()
    groupOfAnswers = []

    # part 1
    # for line in f.readlines():
    #     line = line.strip('\n')
    #     if line == '':
    #         print("---")
    #         print(setOfAnswers)
    #         print(len(setOfAnswers))
    #         sum += len(setOfAnswers)
    #         setOfAnswers = set()
    #     else:
    #         for letter in line:
    #             setOfAnswers.add(letter)
    #         # print(setOfAnswers)
        

    for line in f.readlines():

        line = line.strip('\n')

        if line == '':
            print("---")

            # print(setOfAnswers)
            print(groupOfAnswers)

            allYes = groupOfAnswers[0].intersection(*groupOfAnswers)
            if len(allYes) == 0:
                print("empty set")
            else:
                sum += len(allYes)
            print(allYes)
            groupOfAnswers = []

        else:
            for letter in line:
                setOfAnswers.add(letter)

            groupOfAnswers.append(setOfAnswers)
            setOfAnswers = set()
            # setOfAnswers.intersection(subset)
            # print(setOfAnswers)

print(sum)
