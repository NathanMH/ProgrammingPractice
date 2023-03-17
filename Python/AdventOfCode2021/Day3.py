
trees = 0
loc = 0
count = 0


with open('/home/natha/Documents/python/AdventOfCode/assets/Day3.txt') as f:
    
    for line in f:
        if (count % 2 == 0):
            currentRow = list(line.strip('\n'))

            if (currentRow[loc] == '#'):
                trees += 1
            print(str(count) + " : " + str(loc) + " : " + currentRow[loc])
            loc = (loc + 1) % 31
        count += 1
    
    print(trees)


    #use modulo instead of adding repetition to line

