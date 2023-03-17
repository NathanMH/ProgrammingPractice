#!/bin/python3
from functools import reduce

with open("/home/natha/Documents/python/AdventOfCode/assets/Day13.txt", "r") as f:
    timeStr = f.readline().strip("\n")
    routesStr = f.readline().strip("\n").replace("x,", "").split(",")

busRoutes = list(map(int, routesStr))
busRoutes.sort()
leaveTime = int(timeStr)

# print(leaveTime)
# print(busRoutes)

closestBuses = []

for bus in busRoutes:
    nextBus = 0
    while nextBus < leaveTime:
        nextBus += bus

    closestBuses.append(nextBus)

# print(closestBuses)


with open("/home/natha/Documents/python/AdventOfCode/assets/Day13.txt", "r") as f:
    data = f.readlines()
available = list(map(lambda x: x if x == "x" else int(x), data[1].strip().split(",")))
print(available)
idmap = {key: val for val, key in filter(lambda x: x[1] != "x", enumerate(available))}
print(idmap)
idlist = [id for id in idmap]
print(idlist)

step = idlist[0]
start = 0
for id in idlist[1:]:
    delta = idmap[id]
    for i in range(start, step * id, step):
        if not (i + delta) % id:
            step = step * id
            start = i
print(start)
