import re

data = []

filename = "2024\day3\input.txt"
with open(filename, "r") as file:
    for line in file:
        data.append(line)

somme = 0

capture = True
for line in data:
    # matches = re.findall(r"mul\((\d{1,3},\d{1,3})\)",line)
    start = 0
    matches = []

    # catch do() and don't() instructions
    for i in range(len(line)-6):
        if line[i:i+7] == "don't()":
            # capture up to "don't()"
            if capture :
                matches += re.findall(r"mul\((\d{1,3},\d{1,3})\)",line[start:i])
            capture = False
        elif line[i:i+4] == "do()":
            # ignore if already in capture mode
            if not capture:
                start = i+4
                capture = True

    # final capture
    if capture:
        matches += re.findall(r"mul\((\d{1,3},\d{1,3})\)", line[start:])
        
    for match in matches:
        x,y = list(map(int,match.split(",")))
        somme += x*y

print(somme)