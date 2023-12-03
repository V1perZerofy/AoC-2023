import re

def openFile():
    with open("input/input3.txt") as f:
            lines = f.readlines()
            #lines = [x.strip() for x in lines]
            f.close()
    return lines

def is_valid_pos(i, j, arr):
    return 0 <= i < len(arr) and 0 <= j < len(arr[0])

def check_is_part(arr, i, j, length):
    directions = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
    neighbors = ''
    for temp in range(length):
        for di, dj in directions:
            newi, newj = i + di, j + dj
            if is_valid_pos(newi, newj, arr):
                neighbors += arr[newi][newj]
        j += 1
    x = re.findall(r"[^a-zA-Z.0-9\n]+", neighbors)
    return True if x else False
    
def part1(arr):
    num = ''
    endres = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].isnumeric():
                num += arr[i][j]
            else:
                if 1 <= len(num) <= 3:
                    if check_is_part(arr, i, j - len(num), len(num)):
                        #print(num)
                        endres.append(int(num))
                num = ''
            if j + 1 > len(arr[i]) - 1:
                if 1 <= len(num) <= 3:
                    if check_is_part(arr, i, j - len(num), len(num)):
                        #print(num)
                        endres.append(int(num))
                num = ''
    return sum(endres)

def get_neighbouring_nums(arr, i, j):
    directions = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)] #clockwise
    neighbours = [] #list of neighbouring numbers
    last_num = '' #last number added to neighbours
    for di, dj in directions: #check all directions
        ni, nj = i + di, j + dj #new i and j
        if is_valid_pos(ni, nj, arr): #if valid position
            if arr[ni][nj].isnumeric(): #if numeric
                if arr[ni][nj - 1].isnumeric(): #if left is numeric
                    if arr[ni][nj - 2].isnumeric(): #if left left is numeric
                        if arr[ni][nj- 2:nj+1] != last_num: #if not same as last added
                            last_num = arr[ni][nj- 2:nj+1] #set last_num to new last added
                            neighbours.append(arr[ni][nj- 2:nj+1]) #add to neighbours
                    elif arr[ni][nj + 1].isnumeric(): #if right is numeric
                        if arr[ni][nj- 1:nj + 2] != last_num: #if not same as last added
                            last_num = arr[ni][nj- 1:nj + 2] #set last_num to new last added
                            neighbours.append(arr[ni][nj- 1:nj + 2]) #add to neighbours
                    else:
                        if arr[ni][nj- 1:nj+1] != last_num:
                            last_num = arr[ni][nj- 1:nj+1]
                            neighbours.append(arr[ni][nj- 1:nj+1])
                elif arr[ni][nj + 1].isnumeric():
                    if arr[ni][nj + 2].isnumeric():
                        if arr[ni][nj:nj + 3] != last_num:
                            last_num = arr[ni][nj:nj + 3]
                            neighbours.append(arr[ni][nj:nj + 3])
                    else:
                        if arr[ni][nj:nj + 2] != last_num:
                            last_num = arr[ni][nj:nj + 2]
                            neighbours.append(arr[ni][nj:nj + 2])
                else:
                    neighbours.append(arr[ni][nj])
            else:
                last_num = ''
    return neighbours

def part2(arr):
    endres = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '*':
                neighbours = get_neighbouring_nums(arr, i, j)
                if neighbours:
                    if len(neighbours) == 2:
                        ratio = int(neighbours[0]) * int(neighbours[1])
                        endres += ratio
    return endres

if __name__ == "__main__":
    lines = openFile()
    res1 = part1(lines)
    print(res1)
    res2 = part2(lines)
    print(res2)