reports = []

filename = "2024\day2\input.txt"
with open(filename, "r") as file:
    for line in file:
        reports.append(list(map(int,line.split())))

def is_strictly_increasing(liste):
    for i,val in enumerate(liste[:-1]):
        if val >= liste[i+1]: return False
    return True

def is_strictly_decreasing(liste):
    return is_strictly_increasing(list(reversed(liste)))

def has_max_step_size(liste, max_step_size):
    for i,val in enumerate(liste[:-1]):
        if abs(val - liste[i+1]) > max_step_size: return False
    return True

safe_reports = 0
for report in reports:
    if is_strictly_increasing(report) or is_strictly_decreasing(report):
        if has_max_step_size(report, 3):
            safe_reports +=1

print(safe_reports)