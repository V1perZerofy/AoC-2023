import re
from word2number import w2n
import aoc_lube
import sys
import time

def readInput():
    with open("input/input1.txt") as f:
        lines = f.readlines()
        #remove \n
        lines = [x.strip() for x in lines]
        f.close()
    return lines


# Part 1
def part1():
    endres = 0
    for i in lines:
        x = re.findall(r"([1-9])", i)
        endres += int(x[0] + x[-1])
    return endres

def part2():
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

#part 2 with animation
def part2_with_anim(lines):
    endres = []
    for line in lines:
        # Strip newline characters and any trailing whitespace
        line = line.rstrip()
        res = []
        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        numerals = ["o\u001b[32;1m1\u001b[30me", "t\u001b[32;1m2\u001b[30mo", "t\u001b[32;1m3\u001b[30me",
                    "f\u001b[32;1m4\u001b[30mr", "f\u001b[32;1m5\u001b[30me", "s\u001b[32;1m6\u001b[30mx",
                    "s\u001b[32;1m7\u001b[30mn", "e\u001b[32;1m8\u001b[30mt", "n\u001b[32;1m9\u001b[30me"]
        #line = re.sub(r'(\d)', "\u001b[32;1m" + r'\1' + "\u001b[30m", line)
        for j in range(9):
            line = re.sub(nums[j], numerals[j], line)
            sys.stdout.write("\r" + line)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the sleep time as needed for the animation effect
        # Extract numbers from the final line
        for j in line:
            if j.isdigit():
                res.append(j)
        endres.append(res[0] + res[-1] if res else '00')
        # Print the final result always on the same space
        #formatted_sentence = f"{line.ljust(8)}{endres[-1]}"
        #print("\r" + formatted_sentence, end="")
        print()  # Move to the next line after processing the current line
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
    print(lines)
    #print(part1())
    #print(part2())
    #print(sum(map(int, findNumsRegex())))
    #part2_with_anim(lines)

    #aoc_lube.submit(year=2015, day=1, part=1, solution=part1)
    #aoc_lube.submit(year=2015, day=1, part=2, solution=part2)