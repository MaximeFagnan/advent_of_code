import re

data = []

filename = "2024\day3\input.txt"
with open(filename, "r") as file:
    for line in file:
        data.append(line)


somme = 0

for line in data:
    matches = re.findall(r"mul\((\d{1,3},\d{1,3})\)",line)
    for match in matches:
        x,y = list(map(int,match.split(",")))
        somme += x*y

print(somme)