l1, l2 = [], []

filename = "2024\day1\input.txt"
with open(filename, "r") as file:
    for line in file:
        coord_1, coord_2 = list(map(int,line.split()))
        l1.append(coord_1)
        l2.append(coord_2)

l1.sort()
l2.sort()

sum = 0
for i in range(len(l1)):
    sum += abs(l1[i]-l2[i])

print(sum)