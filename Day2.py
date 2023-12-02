import re
import aoc_lube

def readInput():
    with open("input/input2.txt") as f:
        lines = f.readlines()
        #remove \n
        lines = [x.strip() for x in lines]
        f.close()
    return lines

def part1():
    redpattern = r"(\d+)\s+red"
    bluepattern = r"(\d+)\s+blue"
    greenpattern = r"(\d+)\s+green"
    endres = 0
    power = []
    for i in range(len(lines)):
        red = [int(num) for num in re.findall(redpattern, lines[i], re.MULTILINE)]
        red.sort(reverse=True)
        blue = [int(num) for num in re.findall(bluepattern, lines[i], re.MULTILINE)]
        blue.sort(reverse=True)
        green = [int(num) for num in re.findall(greenpattern, lines[i], re.MULTILINE)]
        green.sort(reverse=True)
        
        if red[0] <= 12 and green[0] <= 13 and blue[0] <= 14:
            endres += i + 1
        power.append(red[0] * green[0] * blue[0])
    return sum(power)

if __name__ == "__main__":
    lines = readInput()
    print(part1())
    aoc_lube.submit(year=2023, day=2, part=2, solution=part1)