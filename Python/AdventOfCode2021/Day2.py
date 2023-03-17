def part1():
    validPasses = 0
    with open('/home/natha/Documents/python/AdventOfCode/assets/Day2.txt', 'r') as f:
        for line in f:

            substrings = line.split(" ")
            minCount, maxCount = substrings[0].split("-")
            reqLetter = substrings[1].strip(":")
            password = substrings[2]

            passCount = dict()
            for letter in list(password):
                if letter in passCount:
                    passCount[letter] += 1
                else:
                    passCount[letter] = 1


            if int(minCount) <= passCount.get(reqLetter, 0) <= int(maxCount):
                validPasses += 1
            else:
                notValids += 1

    print("Valid: " + str(validPasses))


def part2():
    valid = 0
    invalid = 0
    with open('/home/natha/Documents/python/AdventOfCode/assets/Day2.txt', 'r') as f:
        for line in f:

            substrings = line.split(" ")
            firstPos, secondPos = substrings[0].split("-")
            letter = substrings[1].strip(":")
            password = list(substrings[2])

            if (password[int(firstPos)-1] == letter) ^ (password[int(secondPos)-1] == letter):
                valid += 1
            else:
                invalid += 1


    print("Valid: " + str(valid))
    print("invalid: " + str(invalid))

part2()
