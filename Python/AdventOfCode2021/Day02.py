path = "C:\\Users\\natha\\Desktop\\Documents\\Python_Projects\\AdventOfCode2021\\assets\\Day02.txt"

def part_one(path):
    moves = {"down": 0, "up": 0, "forward": 0}
    with open(path, "r") as f:
        for line in f:
            direction, amount = line.split(" ")
            moves[direction] += int(amount)
    print(moves)
    print(depth * moves["forward"])

def part_two(path):

    depth = 0
    horizontal = 0
    aim = 0

    with open(path, "r") as f:
        for line in f:
            direction, amount = line.split(" ")
            if direction == "down":
                aim += int(amount)
            elif direction == "up":
                aim -= int(amount)
            elif direction == "forward":
                horizontal += int(amount)
                depth += (int(amount) * aim)

    print(depth)
    print(horizontal)
    print(aim)
    print(horizontal * depth)


if __name__ == "__main__":
    # part_one(path)
    part_two(path)