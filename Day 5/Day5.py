with open("Day 5/input/input.txt") as f:
    #split empty lines
    lines = f.readlines()

start_seeds = list(map(int, lines[0][7:].split(" ")))
all_seeds = []
i = 0
all_seeds = []
for i in range(0, len(start_seeds), 2):
    start = start_seeds[i]
    length = start_seeds[i + 1]
    for j in range(length):
        all_seeds.append(start + j)


maps = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [], "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []}

current_map = None
for line in lines[1:]:
    if "map:" in line:
        current_map = line.split()[0]
    elif len(line) > 1:
        start_dest, start_source, length = list(map(int, line.split()))
        maps[current_map].append((start_dest, start_source, length))

locations = []
soil, fertilizer, water, light, temperature, humidity, location = None, None, None, None, None, None, None
for seed in all_seeds:
    soil = seed
    for start_dest, start_source, length in maps["seed-to-soil"]:
        if start_source <= seed < start_source + length:
            offset = seed - start_source
            soil = start_dest + offset
            break
    fertilizer = soil
    for start_dest, start_source, length in maps["soil-to-fertilizer"]:
        if start_source <= soil < start_source + length:
            offset = soil - start_source
            fertilizer = start_dest + offset
            break
    water = fertilizer
    for start_dest, start_source, length in maps["fertilizer-to-water"]:
        if start_source <= fertilizer < start_source + length:
            offset = fertilizer - start_source
            water = start_dest + offset
            break
    light = water
    for start_dest, start_source, length in maps["water-to-light"]:
        if start_source <= water < start_source + length:
            offset = water - start_source
            light = start_dest + offset
            break
    temperature = light
    for start_dest, start_source, length in maps["light-to-temperature"]:
        if start_source <= light < start_source + length:
            offset = light - start_source
            temperature = start_dest + offset
            break  
    humidity = temperature
    for start_dest, start_source, length in maps["temperature-to-humidity"]:
        if start_source <= temperature < start_source + length:
            offset = temperature - start_source
            humidity = start_dest + offset
            break  
    location = humidity
    for start_dest, start_source, length in maps["humidity-to-location"]:
        if start_source <= humidity < start_source + length:
            offset = humidity - start_source
            location = start_dest + offset
            break
    locations.append(location)

locations.sort()
print(locations[0])