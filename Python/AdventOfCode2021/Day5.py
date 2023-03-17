import sys

print(sys.maxsize)

with open('/home/natha/Documents/python/AdventOfCode/assets/Day5.txt', 'r') as myFile:
    passes = []
    maxID = 0
    minID = sys.maxsize
    for l in myFile:
        # convert to binary
        ID = int(l.replace('F','0').replace('L','0').replace('B','1').replace('R','1'), 2)
        # print(l.replace('F','0').replace('L','0').replace('B','1').replace('R','1'))
        passes.append(ID)
        maxID = max(maxID, ID)
        minID = min(minID, ID)

    passes.sort()
    print("1st STAR SOLUTION ->", maxID)
    print("2nd STAR SOLUTION ->", set(list(range(minID,maxID))) - set(passes))
