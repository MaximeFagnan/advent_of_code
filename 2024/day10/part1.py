"""
Approche dynamique:

Pour chaque n en coordonnée (x,y) on peut se rendre aux mêmes endroits que les voisins de (x,y) contenant n+1.
Pour chaque location contenant n, on veut donc remplir de façon dynamique, de manière décroissante,
les coordonées des 9 où l'on peut se rendre en montant la colline de manière graduelle.
"""

data = []
locations = dict()  # 0 <= n <= 9, {n : set of coords where n can be found}
can_go_to = dict()  # {location: set of locations containing a 9 you can go to by even, gradual uphill slope from location}

filename = r"2024\day10\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        data.append([])
        for col_no, c in enumerate(line):
            n = int(c)
            location = (line_no, col_no)
            data[line_no].append(n)
            if n in locations:
                locations[n].append(location)
            else:
                locations[n] = [location]
            if n == 9:
                can_go_to[location] = {location}

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

# ordering to program dynamically
for n in range(8,-1,-1):
    # for every location containing n, you can go to where your neighbours containing n+1 can go to.
    for location in locations[n]:
        can_go_to[location] = set()
        for neighbour in neighbours(location):
            line_no, col_no = neighbour
            if data[line_no][col_no] == n+1:
                can_go_to[location].update(can_go_to[neighbour])

somme = 0

for possible_trailhead in locations[0]:
    somme += len(can_go_to[possible_trailhead])

print(somme)