'''
import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT) // setting up the pin to be output)

GPIO.cleanup()

'''
'''
Goal - get to cell [7][7]
'''
#Pretend that there are no walls what so ever
maze = [0]*16
for i in range(16):
    maze[i] = [0] * 16

for i in range(16):
    for j in range(16):
        maze[i][j] = i+j # append
    
#print maze 

#walls assign each cell 4 information about each side of the cell:
#None if there is no information, 0 for no wall and 1if there is a wall
#[a,b,c,d] a:north b:east c:south d:west
walls = [0]*16
for i in range(16):
    walls[i] = [0]*16
for i in range(16):
    for j in range(16):
        walls[i][j] = [None]*4

#print walls

'''
constant values needed later in the program
directions: +-1 in rows or columns indication north south east west move
'''



'''
picking the best course algorythm
'''
def find_shortest_path(maze, walls, position):
    '''
    maze: list with values of each cell of a maze
    walls: list with information about the walls around each cell
    returns: shortest path - list of cells, in order, to get to the center
             False if it fails to find a way to the center
    '''
    shortest_path = [[7,7]]
    current_location = [7,7]
    while shortest_path[len(shortest_path)-1] != position:
        best = None
        direction = None
        #check north
        try:
            if walls[current_location[0]][current_location[1]][0] == 0:
                best = maze[current_location[0]+1][current_location[1]]
                direction = [1,0]
        except IndexError:
            pass
        #check east
        try:
            if walls[current_location[0]][current_location[1]][1] == 0:
                if best == None or maze[current_location[0]][current_location[1]+1] <= best[0]:
                    best = maze[current_location[0]][current_location[1]+1]
                    direction = [0,1]
        except IndexError:
            pass
        #check south
        try:
            if walls[current_location[0]][current_location[1]][2] == 0:
                if best == None or maze[current_location[0]-1][current_location[1]] <= best[0]:
                    best = maze[current_location[0]-1][current_location[1]]
                    direction = [-1,0]
        except IndexError:
            pass
        #check west
        try:
            if walls[current_location[0]][current_location[1]][3] == 0:
                if best == None or maze[current_location[0]][current_location[1]-1] <= best[0]:
                    best = maze[current_location[0]][current_location[1]-1]
                    direction = [0,-1]
        except IndexError:
            pass
                
        #make updates to local variables
        current_location = [current_location[0]+direction[0], current_location[1]+direction[1]]
        shortest_path.append(current_location)
    return shortest_path
    
    
def update_maze(position, orientation, walls):
    '''
    position: a coordinate x,y that determines the cell in which the robot took the reading
    orientation: a number which determines the robot orientation o the maze relative to starting orientation
    reading: list of 3 elements that determine the walls
    returns: flooded maze
    '''
    
    
    
    
def update_walls(wall_reading, position, orientation):
    '''
    wall_reading: list of 3 values 0/1 indication the existance of a wall
    to the left,top and right of a cell
    position: a coordinate x,y that determines the cell in which the robot took the reading
    orientation: a number which determines the robot orientation o the maze relative to starting orientation
    returns: updated walls list
    example:
        update_walls([1,1,0], [4,6], 1)
        can be interpret as: cell [4,6] has walls [north=1, east=1, south=0, west=None]
        because robot is facing east (orientation = 1), there is wall in the north (left = 1) etc
    '''
    if wall_reading[0] == 1:
        walls[position[0]][position[1]][(3+orientation)%4] = 1
        walls[][][(5+orientation)%4]
    if wall_reading[1] == 1:
        walls[position[0]][position[1]][(0+orientation)%4] = 1
    if wall_reading[2] == 1:
        walls[position[0]][position[1]][(1+orientation)%4] = 1
    
    return walls
    
#def reverse_path(path):

def next_wall(position, orientation, sensor):
    if sensor == 0: #left
        
def take_readings():
    '''
    Takes readings from 3 proximity sensors
    and stores them in a list [left, front, right]
    returns: list with the distances from the walls
    '''
    read = []
    #code to read from pins
    return read

def wall_check(reading):
    '''
    Reading: list of 3 distances form the wall
    returns: list of 0/1 indicationg if there is a wall
    0 - no wall, 1 - wall
    [left, top right]
    '''
    wall_left = 0
    wall_top = 0
    wall_right = 0
    if reading[0] < distance+1 and reading[0] > distance-1:
        wall_left = 1
    if reading[1] < distance+1 and reading[1] > distance-1:
        wall_top = 1
    if reading[2] < distance+1 and reading[2] > distance-1:
        wall_right = 1
          
    return [wall_left, wall_top, wall_right]
        

def initiate()
'''
Check what is at the start
check the system
clean the memory
fill frist maze (no walls)
tunr on the 1st LED
'''

#def move_to_cell(cell)
'''
// We need: the distance the wheel travels doing one revolution. How many revolutions to go to the next cell
revolve by the distance


'''
#def correct_course()
''' w = lenght of 1 wall
check the wall in front (d). Check what is the modulo of (d-0.5w)%w
'''


#def return_home()
'''
following the shortest path to [0][0]
'''

#def turn(direction)
'''
diection: left, right, back
check if in the middle, spin 90 degrees in correct diretion or 180 to go back
go forward one cell (use function move_to_cell)
'''


#def junction_decition()
'''
at the junction recalculate the shortest path to the center and try it.
pick the shortest path from the cell it is in. (pick_shortest_path)
create the list of comands
'''
#code
#testing code








# Actual Code:

'''TD'''initiate()
position = [0][0]
orientation = 0
initial_reading = '''TD'''take_readings()
walls = '''TD'''update_walls(initial_reading, position, orientation)
maze_flooded = '''TD'''update_maze(position, orientation, walls)
x = [initial_reading, position, orientation] #We have to keep track of x[1] & x[2] all the time

while(1):
    while(1):
        #LED - looking for the mid point
        L = find_shortest_path(maze_flooded, walls, x[1])
        x = '''TD'''follow_the_path(L, x[1], x[2]) #return: reading, position, orientation 
        #stop_motors()
        
        if x[1] == [8,8]:
            #Light LED - way wack
            L = '''TD'''find_way_back()
            x = follow_the_path(L, x[1], x[2])
            if x[1] == [0][0]:
                break
            else:
                #wait for restart - button, light LED - "need help :D"
            
        
        walls = update_walls(x[0], x[1], x[2])
        maze_flooded = update_maze(x[1], x[2], walls)
        
    
    #the following part needs to be checked
    if x[1] != [0][0]:
        continue
    else:    
        '''TD'''spin_around()
        x[2] = (x[2]+2)%4
        '''TD'''start_again() # I guess the program should wait for the push of a button or just wait few seconds
    
    








