import time
import os
import random
import pyfiglet # Generate ascii text 


class Sand:
    def __init__(self, x, y, collision):
        self.x = x
        self.y = y
        self.collision = collision
    
    def check_collision(self, object, matrix, matrix_height, matrix_width):
        if object.y < matrix_height -1 and matrix_width >= object.x > 0 and matrix[object.y + 1][object.x] == ' ':
            matrix[object.y][object.x] = ' '  # Clear the current position
            object.y += 1  # Update the position
            matrix[object.y][object.x] = '▮'  # Update the new position
        else:
             object.collision = True
    
    def check_left(self, object, matrix, matrix_height, matrix_width):
        global index
        if object.y < matrix_height -1 and matrix_width >= object.x > 0 and matrix[object.y + 1][object.x - 1] == ' ':
            matrix[object.y][object.x] = ' '  
            object.y += 1  
            object.x -= 1
            matrix[object.y][object.x] = '▮'  
        else:
             index += 1
             return index
    
    def check_right(self, object, matrix, matrix_height, matrix_width):
        global index
        if object.y < matrix_height -1 and object.x < matrix_width - 1  and matrix[object.y + 1][object.x + 1] == ' ':
            matrix[object.y][object.x] = ' '  
            object.y += 1  
            object.x += 1
            matrix[object.y][object.x] = '▮' 
        else:
            index += 1
            return index
             
    def check_left_down(self, object, matrix, matrix_height, matrix_width):

            if object.y < matrix_height -1 and matrix_width >= object.x > 0 and matrix[object.y + 1][object.x - 1] == ' ':
                matrix[object.y][object.x] = ' ' 
                object.y += 1  
                object.x -= 1
                matrix[object.y][object.x] = '.'  
            elif object.y < matrix_height -1 and object.x < matrix_width - 1  and matrix[object.y + 1][object.x + 1] == ' ':
                matrix[object.y][object.x] = ' '  
                object.y += 1  
                object.x += 1
                matrix[object.y][object.x] = '.'  

    def check_right_down(self, object, matrix, matrix_height, matrix_width):

            if object.x +1 < matrix_width and matrix[object.y][object.x + 1] == ' ':
                matrix[object.y][object.x] = ' '  
                object.x += 1
                matrix[object.y][object.x] = '.' 
            elif object.x - 1 >= 0 and matrix[object.y][object.x - 1] == ' ':
                matrix[object.y][object.x] = ' ' 
                object.x -= 1
                matrix[object.y][object.x] = '.'
class Water (Sand):
    def __init__(self, x, y, collision):
        self.x = x
        self.y = y
        self.collision = collision
    
    def check_collision_water(self, object, matrix, matrix_height, matrix_width):
        if object.y < matrix_height -1 and matrix_width >= object.x > 0 and matrix[object.y + 1][object.x] == ' ':
            matrix[object.y][object.x] = ' '  
            object.y += 1 
            matrix[object.y][object.x] = '.' 
        else:
             object.collision = True

def print_matrix(matrix):
    os.system('clear')
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def create_banner(text):
    banner = pyfiglet.figlet_format(text)
    return banner.split('\n')

def move_banner_horizontally(banner_lines, distance):
    for line in banner_lines:
        padding = ' ' * distance
        print(padding + line)

sand_list = []
water_list = []

matrix_height, matrix_width = 20, 70
matrix = [[' ' for _ in range(matrix_width)] for _ in range(matrix_height)]

index = 0

# Sand generate
for _ in range(400):
    while True:
        random_number = random.randint(0, 2)
        if random_number == 0:
            x = random.randint(15, 23)
        elif random_number == 1:
            x = random.randint(55, 62)
        else:
             x = random.randint(30, 40)

        y = random.randint(0, matrix_height-1)
        coordinates_exist = False
        
        for sand in sand_list:
            if sand.x == x and sand.y == y:
                coordinates_exist = True
                break
        if not coordinates_exist:
            break
    sand = Sand(x, y, False)
    sand_list.append(sand)

# Water generate
def water_gen():
    for _ in range(265):
        while True:
            x = random.randint(20, 34)
            y = random.randint(0, 5)
            coordinates_exist = False
            for sand in sand_list:
                if sand.x == x and sand.y == y:
                    coordinates_exist = True
                    break
            if not coordinates_exist:
                break
        water = Water(x, y, False)
        water_list.append(water)
    for water in water_list:
        matrix[water.y][water.x] = '●'

for sand in sand_list:
    matrix[sand.y][sand.x] = '▮'

run = True
run_water = False

text = "pysand"

while run:    
    time.sleep(0.05)
    print_matrix(matrix)
    banner_lines = create_banner(text)
    move_banner_horizontally(banner_lines, distance=55)
    for sand in sand_list:
        if sand.y < matrix_height:
            sand.check_collision(sand, matrix, matrix_height, matrix_width) 
        if sand.collision:
            sand.check_left(sand, matrix, matrix_height, matrix_width)
            sand.check_right(sand, matrix, matrix_height, matrix_width)
        if index == 2*len(sand_list):
             run = False
             run_water = True
    index = 0

water_gen()

while run_water:
    time.sleep(0.05)
    print_matrix(matrix)
    banner_lines = create_banner(text)
    move_banner_horizontally(banner_lines, distance=55)
    for water in water_list:
        if water.y < matrix_height:
            water.check_collision_water(water, matrix, matrix_height, matrix_width) 

        water.check_left_down(water, matrix, matrix_height, matrix_width)
        water.check_right_down(water, matrix, matrix_height, matrix_width)


