from math import log10

LHS = [] # left hand side
RHS = [] # right hand side

filename = r"2024\day7\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        lhs, rhs = line.split(':')
        LHS.append(int(lhs))
        RHS.append(list(map(int,rhs.split())))

def find_all_operator_combinations(n: int):
    operators = []
    if n == 0: yield operators
    if n >= 1:
        for operators in find_all_operator_combinations(n-1):
            yield ["+"] + operators
            yield ["*"] + operators
            yield ["||"] + operators

def operate(rhs, operators):
    assert len(rhs) == len(operators)+1, f"{rhs} {operators}"
    total = rhs[0]
    for i, operator in enumerate(operators):
        # print(f"total: {total}, operator: {operator}, rhs: {rhs}")
        if operator == "+":
            total += rhs[i+1]
        elif operator == "*":
            total *= rhs[i+1]
        elif operator == "||":
            total = total*10**(int(log10(rhs[i+1]))+1) + rhs[i+1]
    return total

somme = 0

eq_no =  0
for lhs, rhs in zip(LHS, RHS):
    eq_no +=1
    print(eq_no)
    for operators in find_all_operator_combinations(len(rhs)-1):
        if lhs == operate(rhs,operators):
            somme += lhs
            break

print(somme)
