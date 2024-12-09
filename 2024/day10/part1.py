
# data format for day 8
data = []
filename = r"2024\day10\test_input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        data.append([])
        for col_no, c in enumerate(line):
            data[line_no].append(c)


height = len(data)
width = len(data[0])

# boundary conditions for grid problems
def is_in_bounds(coords):
    line_no, col_no = coords
    if (0 <= line_no < height) and (0 <= col_no < width):
        return True
    else:
        return False

