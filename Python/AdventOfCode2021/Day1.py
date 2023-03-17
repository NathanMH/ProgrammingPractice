import csv

numList = []
with open("/home/natha/Documents/python/AdventOfCode/assets/Day1.csv", newline="") as f:
    for row in csv.reader(f):
        numList.append(int(row[0]))

numList.sort()
# print(numList)

target = 2020

# Basic part 1
def find_2():
    for num in numList:
        if num > 1010:
            break
        else:
            if (2020 - num) in numList:
                print(num * (2020 - num))


# Part 2

expenseNums = set()


def find_3():
    for firstNum in numList:
        tempNum = target - firstNum
        for secondNum in numList:
            if (tempNum - secondNum) in numList:
                lastNum = tempNum - secondNum
                expenseNums.add(firstNum)
                expenseNums.add(secondNum)
                expenseNums.add(lastNum)


find_3()
finalNums = list(expenseNums)
print(finalNums[0] * finalNums[1] * finalNums[2])
