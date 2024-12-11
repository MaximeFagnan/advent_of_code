from math import log10, pow

# Notice: about 1/2 of numbers multiplied by 2024 will gain 3 digits, and other half will gain 4 digits.
# Since a lot of rock_ids end up pointing to the same rock_ids eventually, we should stack rock_ids

data = dict()
# rock_id -> number_of_rocks with that id

filename = r"2024\day11\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        for number in line.split():
            number = int(number)
            if number in data:
                data[number] +=1
            else:
                data[number] = 1
 
def number_of_digits(n : int):
    return int(log10(n)) + 1

def first_half(n: int):
    num_digits = number_of_digits(n)
    return int(n//pow(10,num_digits//2))

def second_half(n: int):
    num_digits = number_of_digits(n)
    return int(n - first_half(n)*pow(10,num_digits//2))

def add_n_rocks(rock_id: int, number_of_rocks: int, new_data):
    if rock_id in new_data:
        new_data[rock_id] += number_of_rocks
    else:
        new_data[rock_id] = number_of_rocks

def blink():
    global data
    new_data = dict()
    for rock_id, number_of_rocks in data.items():
        # special rock
        if rock_id == 0:
            add_n_rocks(1, number_of_rocks, new_data)
        # even number of digits
        elif (int(log10(rock_id))+1) % 2 == 0:
            id_1 = first_half(rock_id)
            id_2 = second_half(rock_id)
            for id in [id_1,id_2]:
                add_n_rocks(id, number_of_rocks, new_data)        
        # odd number of digits
        else: 
            id = rock_id*2024
            add_n_rocks(id, number_of_rocks, new_data)

    data = new_data

for i in range(75):
    blink()

print(sum(data.values()))