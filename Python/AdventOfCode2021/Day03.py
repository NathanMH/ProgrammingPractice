import pandas as pd
from bitarray import bitarray

path = "C:\\Users\\natha\\Desktop\\Documents\\Python_Projects\\AdventOfCode2021\\assets\\Day03.txt"

with open(path, "r") as f:
    data = [list(map(int, row)) for row in f.read().split()]

def get_count(data_list, col, which):
    count = {0: 0, 1: 0}
    for row in data_list:
        if int(row[col]) > 0:
            count[1] += 1
        else:
            count[0] += 1
    if which == 'most':
        return 1 if count[1] >= count[0] else 0
    else:
        return 0 if count[1] >= count[0] else 1

def part_one():
    dataframe = make_frame(data)

    binary = ''
    for name, values in dataframe.iteritems():
        counts = dataframe[name].value_counts(sort=False)
        if counts[0] > counts[1]:
            binary += '1'
        else:
            binary += '0'

    bits = bitarray(binary)
    i = 0
    for bit in ~bits:
        i = (i << 1) | bit

    print(i * (int(binary, 2)))

def part_two():

    with open(path, "r") as f:
        data = f.read().split()

    for col in range(0, 12):
        num = get_count(data, col, 'most')
        print(str(col) + ": " + str(num))
        for index, row in enumerate(data):
            if int(row[col]) != num:
                data.pop(index)
                # print(row[col])
            # print(get_count(data, 1))
    print(data)



if __name__ == "__main__":
    # part_one()
    part_two()