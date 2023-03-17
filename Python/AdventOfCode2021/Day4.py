import re


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = int(byr)
        self.iyr = int(iyr)
        self.eyr = int(eyr)
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def isValidHeight(self):
        if 'cm' in self.hgt:
            return 150 <= int(self.hgt.replace('cm', '')) <= 193
        elif 'in' in self.hgt:
            return 59 <= int(self.hgt.replace('in', '')) <= 76
        else:
            return False

    def isValid(self):
        validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return True if (1920 <= self.byr <= 2002
                        and 2010 <= self.iyr <= 2020
                        and 2020 <= self.eyr <= 2030
                        and self.isValidHeight()
                        and re.match(r"^#[a-f0-9]{6}", self.hcl)
                        and self.ecl in validEyeColors
                        and re.match(r"^[0-9]{9}$", self.pid)) else False


def readData(fileName):
    with open(fileName, 'r') as f:
        return f.read().split('\n\n')


def hasRequiredFields(string):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return True if all([field in string for field in requiredFields]) else False


def stringToPassport(string):
    params = {}
    for fieldString in re.split(' |\n', string):
        try:
            [field, value] = fieldString.split(':')
        except:
            pass
        params[field] = value
    return Passport(**params)


data = readData('/home/natha/Documents/python/AdventOfCode/assets/Day4.txt')

validStrings = [
    string for string in data if hasRequiredFields(string)]

passports = [stringToPassport(string)
             for string in validStrings]
validPassports = [passport for passport in passports if passport.isValid()]

# Part 1
print(len(validStrings))
# Part 2
print(len(validPassports))
