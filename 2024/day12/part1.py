from itertools import product

data = []
locations = dict()  # {plant_type : set of coords where n can be found}

filename = r"2024\day12\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        data.append([])
        for col_no, plant_type in enumerate(line):
            location = (line_no, col_no)
            data[line_no].append(plant_type)
            if plant_type in locations:
                locations[plant_type].add(location)
            else:
                locations[plant_type] = {location}

height = len(data)
width = len(data[0])

# boundary conditions for grid problems
def is_in_bounds(coord):
    line_no, col_no = coord
    if (0 <= line_no < height) and (0 <= col_no < width):
        return True
    else:
        return False

# neighbours to a given position in a grid problem    
def neighbours(coord):
    line_no, col_no = coord
    potential_neighbours = [
        (line_no-1, col_no),
        (line_no+1, col_no),
        (line_no, col_no-1),
        (line_no, col_no+1)
    ]
    for potential_neighbour in potential_neighbours:
        if is_in_bounds(potential_neighbour):
            yield potential_neighbour

somme = 0

visited = set()

def dfs(coord: tuple[int,int]) -> tuple[int,int] : 
    # returns (area,distance) recursively
    global visited
    if coord in visited:
        return (0,0)
    visited.add(coord)
    line_no, col_no = coord
    plant_type = data[line_no][col_no]
    area = 1
    perimeter = 4
    for neighbour in neighbours(coord):
        if neighbour in locations[plant_type]:
            perimeter -= 1
            if neighbour not in visited:
                dfs_area, dfs_perimeter = dfs(neighbour)
                area += dfs_area
                perimeter += dfs_perimeter
    return (area, perimeter)

somme = 0

for coord in product(range(width), range(height)):
    area, perimeter = dfs(coord)
    somme += area*perimeter

print(somme)