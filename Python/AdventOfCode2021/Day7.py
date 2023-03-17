import re
import pdb

pdb.set_trace()


def count_children(bags, parent, level=0):
    total = 1
    for child, number in bags[parent].items():
        total += int(number) * count_children(bags, child, level + 1)
    return total


def count_holding_bags(bags, target, parents=set()):
    for key, value in bags.items():
        if target in value and key not in parents:
            parents.add(key)
            count_holding_bags(bags, key, parents)

    return len(parents)


def main():
    bags = dict()
    shiny_gold_bag = "shiny gold bag"
    bags[shiny_gold_bag] = dict()

    with open("/home/natha/Documents/python/AdventOfCode/assets/Day7.txt", "r") as f:
        for line in f.read().splitlines():
            parent, children = re.match(r"(.+?)s? contain (.+)", line).groups()
            children = re.findall(r"(\d) ([ a-z]+bag)?", children)

            if parent not in bags:
                bags[parent] = dict()

            for (number, child) in children:
                bags[parent][child] = number

    print(f"Part1: {count_holding_bags(bags, shiny_gold_bag)}")
    print(f"Part2: {count_children(bags, shiny_gold_bag) - 1}")


if __name__ == "__main__":
    main()
