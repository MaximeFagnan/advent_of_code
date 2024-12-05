rules = dict()
updates = []
update_flag = False

filename = r"2024\day5\input.txt"
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            update_flag = True
        elif not update_flag:
            before, after = map(int,line.split('|'))
            if before not in rules:
                rules[before] = set([after])
            else:
                rules[before].add(after)
        else :
            update =list(map(int,line.split(',')))
            updates.append(update)

def middle_number(update):
    return update[len(update)//2]

# checks if an update is valid to be printed
def is_valid(update):
    for position,number in enumerate(update):
        # if the number has to be before another number
        if number in rules:
            must_precede = rules[number]
            for after in rules[number]:
                # if the index of number is after the index for the number it should precede
                if after in update and position >= update.index(after):
                    return False
    return True

somme = 0

for update in updates:
    if is_valid(update):
        somme += middle_number(update)

print(somme)