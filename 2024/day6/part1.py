obstacles = set() # coords of obstacles

# This is bad programming, video game arrow directions
current_direction = "w"
possible_directions = ['w','a','s','d']
current_location = (0,0)
visited_locations = set()
steps_taken = 0

filename = r"2024\day6\input.txt"
with open(filename, "r") as file:
    for line_no, line in enumerate(file):
        line = line.strip()
        for col_no, c in enumerate(line):
            location = (line_no, col_no)
            if c == '.':
                pass
            elif c == '^':
                current_location = location
                visited_locations.add(location)
            elif c == '#':
                obstacles.add(location)

width, height = 130, 130 #hard coded
# width, height = 10, 10 #hard coded

def take_a_step():
    global steps_taken, current_location
    current_location = location_in_front()
    steps_taken += 1
    visited_locations.add(current_location)
    
def rotate_90_clockwise():
    global current_direction
    if current_direction == 'w':
        current_direction = 'd'
    elif current_direction == 'a':
        current_direction = 'w'
    elif current_direction == 's':
        current_direction = 'a'
    elif current_direction == 'd':
        current_direction = 's'

def location_in_front():
    line_no, col_no = current_location
    if current_direction == 'w':
        line_no -= 1
    elif current_direction == 'a':
        col_no -= 1
    elif current_direction == 's':
        line_no += 1
    elif current_direction == 'd':
        col_no += 1
    return (line_no,col_no)
    
def is_obstacle_in_front():
    if location_in_front() in obstacles:
        return True
    else:
        return False
    
def is_exit_in_front():
    line_no, col_no = location_in_front()
    if line_no<0 or col_no<0 or line_no>=height or col_no>= width:
        return True
    else:
        return False

while True:
    if is_exit_in_front():
        steps_taken += 1
        break
    elif is_obstacle_in_front():
        rotate_90_clockwise()
    else:
        take_a_step()

print(len(visited_locations))