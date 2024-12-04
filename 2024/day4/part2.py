data = []

filename = r"2024\day4\input.txt"
with open(filename, "r") as file:
    for line in file:
        data.append(line.strip())

lines = len(data)
columns = len(data[0])

data_table = [[] for _ in range(lines)]

for i, line in enumerate(data):
    for c in line:
        data_table[i].append(c)

somme = 0

# count all X-mas by checking all 'A' and their neighbours
for row_no, line in enumerate(data_table):
    for col_no, c in enumerate(line):
        # if c=='A' and not on the edge
        if c == "A" and row_no > 0 and col_no > 0 and row_no < lines-1 and col_no < columns-1:
            #check to see if it is surrounded with appropriate neighbours
            neighbours = [
                data_table[row_no-1][col_no-1],
                data_table[row_no-1][col_no+1],
                data_table[row_no+1][col_no+1],
                data_table[row_no+1][col_no-1],
            ]
            neighbour_word = "".join(neighbours)
            #rotating clockwise arount the neighbours should give the following pattern
            if neighbour_word == "MMSS" or neighbour_word == "MSSM" or neighbour_word == "SSMM" or neighbour_word == "SMMS":
                somme+=1

print(somme)