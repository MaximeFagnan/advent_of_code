from itertools import combinations

data = []
towers = dict()
antinodes_to_tower_types = dict()  # (x,y) -> [A,B,C] means (x,y) has antinode for all these frequencies

filename = r"2024\day8\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        data.append([])
        for col_no, c in enumerate(line):
            coords = (line_no, col_no)
            data[line_no].append(c)
            if c != ".":
                if c in towers:
                    towers[c].append(coords)
                else:
                    towers[c] = [coords]

height = len(data)
width = len(data[0])

def is_in_bounds(coords):
    line_no, col_no = coords
    if (0 <= line_no < height) and (0 <= col_no < width):
        return True
    else:
        return False
    
def add_antinode(coords, tower_type):    
    if coords in antinodes_to_tower_types:
        antinodes_to_tower_types[coords].append(tower_type)
    else:
        antinodes_to_tower_types[coords] = [tower_type]

#for every kind of frequency, take the coords of the towers
for tower_type, coords in towers.items():
    #for every pair of tower coords
    for coord_1, coord_2 in combinations(coords,2):
        line_1, col_1 = coord_1
        line_2, col_2 = coord_2
        delta_line = line_2 - line_1
        delta_col = col_2 - col_1

        antinode = coord_2
        while(is_in_bounds(antinode)):
            add_antinode(antinode, tower_type)
            line_no, col_no = antinode
            antinode = (line_no + delta_line, col_no + delta_col)
        antinode = coord_1
        while is_in_bounds(antinode):
            add_antinode(antinode, tower_type)
            line_no, col_no = antinode
            antinode = (line_no - delta_line, col_no - delta_col)

print(len(antinodes_to_tower_types))