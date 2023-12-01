import re
from word2number import w2n

def readInput():
    with open("input/input1.txt") as f:
        lines = f.readlines()
        f.close()
    return lines


# Part 1
def part1():
    endres = 0
    for i in lines:
        x = re.findall(r"([1-9])", i)
        endres += int(x[0] + x[-1])
    return endres


#part 2
def findNums():
    endres = []
    for i in range(len(lines)):
        res = []
        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        numerals = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
        for j in range(9):
            lines[i] = re.sub(nums[j], numerals[j], lines[i])
        for j in lines[i]:
            if j.isnumeric():
                res.append(j)
        endres.append(res[0] + res[-1])
    return sum(map(int, endres))


#shorter part 2 using word2number but thats cheating :(
def findNumsRegex():
    endres = []
    for i in range(len(lines)):
        x = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))", lines[i])
        x[0], x[-1] = w2n.word_to_num(str(x[0])), w2n.word_to_num(str(x[-1]))
        endres.append(str(x[0]) + str(x[-1]))
    return endres


if __name__ == "__main__":
    lines = readInput()
    print(part1())
    print(findNums())
    print(sum(map(int, findNumsRegex())))