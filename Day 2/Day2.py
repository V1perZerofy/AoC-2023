import re
import aoc_lube

def readInput():
    with open("input/input2.txt") as f:
        lines = f.readlines()
        #remove \n
        lines = [x.strip() for x in lines]
        f.close()
    return lines

#part 1 and 2 cause 2 is just one line of code
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
    return endres, sum(power)

def part1_without_regex():
    endres = 0
    power = []
    for i in range(len(lines)):
        #split by :
        relevant = lines[i].split(":")[1]
        parts = relevant.split(";")
        red = []
        blue = []
        green = []
        for part in parts:
            #split by comma
            items = part.split(",")
            for item in items:
                split_item = item.strip().split(' ')
                if len(split_item) == 2:
                    value, color = split_item
                    value = int(value)
                    if color == "red":
                        red.append(value)
                    elif color == "blue":
                        blue.append(value)
                    elif color == "green":
                        green.append(value)
        red.sort(reverse=True)
        blue.sort(reverse=True)
        green.sort(reverse=True)
        if red[0] <= 12 and green[0] <= 13 and blue[0] <= 14:
            endres += i + 1
        power.append(red[0] * green[0] * blue[0])
    return endres, sum(power)

if __name__ == "__main__":
    lines = readInput()
    print(part1())
    print(part1_without_regex())
    #aoc_lube.submit(year=2023, day=2, part=2, solution=part1)