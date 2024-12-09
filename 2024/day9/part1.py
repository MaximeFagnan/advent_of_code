from itertools import combinations

memory_alloc = []
file_no = 0
is_file, is_free_space = True, False

filename = r"2024\day9\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        for col_no, c in enumerate(line):
            k = int(c)
            if is_file:
                memory_alloc += [file_no]*k
                file_no +=1
            elif is_free_space:
                memory_alloc += [None]*k
            is_file, is_free_space = not is_file, not is_free_space

# print(memory_alloc)

i = 0
j = len(memory_alloc) - 1

# explicitely adjust the memory alloc
while i<j :
    # print(f"i: {i},  j: {j}")
    # bring a file from the end
    if memory_alloc[i] is None:
        if memory_alloc[j] is None:
            # decrease j and try again
            j -= 1
        else:
            # swap
            memory_alloc[i], memory_alloc[j] = memory_alloc[j], memory_alloc[i]
            i += 1
            j -= 1
    else:
        # nothing to do in this mem_alloc
        i += 1
somme = 0

i = 0
while not memory_alloc[i] is None:
    somme += memory_alloc[i]*i
    i += 1

print(somme)