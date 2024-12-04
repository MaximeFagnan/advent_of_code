import re

data = []

filename = r"2024\day4\input.txt"
with open(filename, "r") as file:
    for line in file:
        data.append(line.strip())

lines = len(data)
columns = len(data[0])

somme = 0

def count_hor_xmas(data):
    for line in data:
        global somme
        matches_1 = re.findall("XMAS", line)
        matches_2 = re.findall("SAMX",line)
        somme += len(matches_1)
        somme += len(matches_2)

def diagonal_index(line_no, col_no):
    d = line_no - col_no
    positive_shifted_d = d + columns -1
    return positive_shifted_d

def diagonalize_data(data):
    diagonals = [[] for _ in range(lines+columns-1)]
    for line_no, line in enumerate(data):
        for col_no, c in enumerate(line):
            d_i = diagonal_index(line_no,col_no)
            diagonals[d_i].append(c)
    diagonals = list(map("".join,diagonals))
    return diagonals

def rotate_data(data):
    global lines, columns
    vert_data = [[] for _ in range(columns)]
    lines, columns = columns, lines
    for line in data:
        for col_no, c in enumerate(reversed(line)):
            vert_data[col_no].append(c)
    return list(map("".join,vert_data))

count_hor_xmas(data)
count_hor_xmas(diagonalize_data(data))

rotated_data = rotate_data(data)

count_hor_xmas(rotated_data)
count_hor_xmas(diagonalize_data(rotated_data))

print(somme)