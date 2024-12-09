from itertools import combinations

files, free_spaces = [], []
file_no = 0
is_file, is_free_space = True, False

class memory_alloc:
    def __init__(self, start_index: int, length: int, file_no = None):
        self.start_index = start_index
        self.length = length
        self.file_no = file_no

    def move(self, new_index: int):
        self.start_index = new_index

    def use_free_space(self, qty: int):
        self.start_index += qty
        self.length -= qty

    def __str__(self):
        return f"start_index: {self.start_index}\nlength: {self.length}\nfile_no: {self.file_no}\n"

filename = r"2024\day9\input.txt"
with open(filename, "r") as file:
    i=0
    for line_no, line in enumerate(file):
        line = line.strip()
        for col_no, c in enumerate(line):
            k = int(c)
            if is_file:
                fichier = memory_alloc(i, k, file_no)
                files.append(fichier)
                file_no +=1
            elif is_free_space:
                free_space = memory_alloc(i,k)
                free_spaces.append(free_space)
            i += k
            is_file, is_free_space = not is_file, not is_free_space

# for file in files: print(file)

for file in reversed(files):
    for free_space in free_spaces:
        if free_space.length >= file.length and file.start_index > free_space.start_index:
            file.move(free_space.start_index)
            free_space.use_free_space(file.length)
            continue

# for file in files: print(file)

somme = 0

for file in files:
    l = file.length
    i = file.start_index
    j = i+l-1
    file_no = file.file_no
    somme_indexes = l*(i + j)//2 # formule somme de i à j
    somme += file_no * somme_indexes

print(somme)