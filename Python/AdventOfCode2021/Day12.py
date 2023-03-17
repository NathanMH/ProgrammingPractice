#!/usr/bin/python3
path = "/home/natha/Documents/python/AdventOfCode/assets/Day12.txt"

cardinals = {0: "N", 90: "E", 180: "S", 270: "W"}


def readInput():
    instructions = []
    with open(path) as f:
        for line in f.readlines():
            instructions.append([line[0], int(line[1 : len(line.strip("\n"))])])
            # print(instructions)
    return instructions


class Ship:
    def __init__(self):
        self.direction = 90
        self.position = {"N": 0, "E": 0, "S": 0, "W": 0}

    def move(self, instr):
        for command in instr:
            if command[0] == "F":
                self.position[cardinals[self.direction]] += command[1]
            elif command[0] == "N":
                self.position["N"] += command[1]
            elif command[0] == "E":
                self.position["E"] += command[1]
            elif command[0] == "S":
                self.position["S"] += command[1]
            elif command[0] == "W":
                self.position["W"] += command[1]
            else:
                self.turn(command)

    def turn(self, instr):
        print(
            "Turning: "
            + str(instr[0])
            + ":"
            + str(instr[1])
            + " from "
            + cardinals[self.direction]
            + " to :"
        )
        if instr[0] == "R":
            self.direction = (self.direction + instr[1]) % 360
        elif instr[0] == "L":
            self.direction = (self.direction - instr[1]) % 360
        print(cardinals[self.direction])


def main():
    finput = readInput()
    ferry = Ship()
    ferry.move(finput)
    print(ferry.position)
    ns = ferry.position["S"] - ferry.position["N"]
    ew = ferry.position["E"] - ferry.position["W"]
    print(ns)
    print(ew)
    print(ns + ew)


if __name__ == "__main__":
    main()
