l1, l2 = [], []

filename = "2024\day1\input.txt"
with open(filename, "r") as file:
    for line in file:
        coord_1, coord_2 = list(map(int,line.split()))
        l1.append(coord_1)
        l2.append(coord_2)

sim_score = 0

for number in l1:
    count = number*l2.count(number)
    sim_score += count

print(sim_score)