print("test")

path = "C:\\Users\\natha\\Desktop\\Documents\\Python_Projects\\AdventOfCode2021\\assets\\Day01.txt"
depths = []

def read_input(path):
    """ Reads input file """

    with open(path, "r") as f:
        for line in f:
            depths.append(int(line))
    return depths

def part_one():
    count = 0
    for i in range(0, len(depths)-1):
        if depths[i+1] - depths[i] > 0:
            count += 1
    return count

def part_two():
    count = 0
    sum = depths[0] + depths[1] + depths[2]
    for i in range(1, len(depths)-2):
        sum2 = depths[i] + depths[i+1] + depths[i+2]
        if sum2 > sum:
            count += 1
        sum = sum2
    print(count)



if __name__ == "__main__":
    read_input(path)
    part_two()