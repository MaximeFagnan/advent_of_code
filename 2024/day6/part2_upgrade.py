# Only consider obstacles placed in the guard's path, considering he only visits about one quarter of the grid

#####################################################################################################################

# Part 1 code to get initial path

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

initial_visited_locations = visited_locations

##################################################################################################################

import itertools
obstacles = set() # coords of obstacles

# This is bad programming, video game arrow directions
current_direction = "w"
possible_directions = ['w','a','s','d']
starting_location= (0,0)
current_location = (0,0)
oriented_visited_locations = set()
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
                starting_location = location
                current_location = location
                oriented_visited_locations.add((line_no,col_no,'w'))
            elif c == '#':
                obstacles.add(location)

width, height = 130, 130 #hard coded
# width, height = 10, 10 #hard coded

def take_a_step():
    global steps_taken, current_location
    current_location = location_in_front()
    steps_taken += 1
    oriented_visited_locations.add((current_location[0],current_location[1],current_direction))
    
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

def can_guard_get_out():
    global steps_taken
    while True:
        if is_exit_in_front():
            steps_taken += 1
            return True
        elif is_obstacle_in_front():
            rotate_90_clockwise()
        elif (location_in_front()[0],location_in_front()[1],current_direction) in oriented_visited_locations :
            # turning in circles
            return False
        else:
            take_a_step()

cyclic_obstacle_placements = 0

for obstacle_verif_count, possible_obstacle in enumerate(itertools.product(range(height),range(width))):
    if obstacle_verif_count%100 == 0:
        print(obstacle_verif_count) # is the program bugged or just calculating
    if possible_obstacle in obstacles or possible_obstacle==starting_location:
        pass # invalid obstacle placement
    # check only obstacles that would modify the path
    elif possible_obstacle in initial_visited_locations:
        # add obstacle, test for cyclicity, reset
        # add obstacle
        obstacles.add(possible_obstacle)
        # test for cyclicity
        if not can_guard_get_out():
            cyclic_obstacle_placements += 1
        # reset
        current_location = starting_location
        oriented_visited_locations = {(starting_location[0],starting_location[1],'w')}
        current_direction = 'w'
        steps_taken = 0
        obstacles.remove(possible_obstacle)

print(cyclic_obstacle_placements)