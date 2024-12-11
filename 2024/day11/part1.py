from math import log10, pow

data = []

filename = r"2024\day11\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        for number in line.split():
            data.append(int(number))
 
def number_of_digits(n : int):
    return int(log10(n)) + 1

def first_half(n: int):
    num_digits = number_of_digits(n)
    return n//pow(10,num_digits//2)

def second_half(n: int):
    num_digits = number_of_digits(n)
    return n - first_half(n)*pow(10,num_digits//2)

def blink():
    global data
    new_data = []
    for n in data:
        # special stone 
        if n==0:
            new_data.append(1)
        # even number of digits
        elif (int(log10(n))+1) % 2 == 0:
            new_data.append(first_half(n))
            new_data.append(second_half(n))
        # odd numbers
        else: 
            new_data.append(n*2024)

    data = new_data

for i in range(25):
    blink()

print(len(data))