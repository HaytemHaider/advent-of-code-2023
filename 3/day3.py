def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 

def is_special_character_adjecent(matrix):
    for row in matrix:
        for element in row:
            if element != '.' and not element.isdigit():
                return True
    return False

def extract_submatrix(matrix, top_left, bottom_right):
    start_row, start_col = top_left
    end_row, end_col = bottom_right
    # Extract the submatrix
    submatrix = [row[start_col:end_col + 1] for row in matrix[start_row:end_row + 1]]
    return submatrix

def calculate_coor(rowidx,colidx,length):
    return [(rowidx - 1 ,colidx - length -1) , (rowidx + 1,colidx)]

def find_possible_parts(matrix):
    list_of_possible_parts = []
    foundDigit = ""
    for rowidx, row in enumerate(matrix):
        for colidx, element in enumerate(row): 
            
            if not element.isdigit() and foundDigit != "":
                list_of_possible_parts.append((foundDigit, calculate_coor(rowidx, colidx, len(foundDigit))))
                foundDigit = ""
            elif element.isdigit():
                foundDigit += element
    return list_of_possible_parts

def find_gear_symbol(matrix):
    list_possible_gears = []
    for rowidx, row in enumerate(matrix):
        for colidx, element in enumerate(row):             
            if element == '*':
                list_possible_gears.append(calculate_coor_gear(rowidx, colidx))
    return list_possible_gears

def calculate_coor_gear(rowidx,colidx):
    rowmin = 0
    rowmax = len(matrix) 
    colmin = 0
    colmax = len(matrix[0]) 

    return (clamp(rowidx - 1 , rowmin, rowmax), clamp(colidx - 4, colmin,colmax)), (clamp(rowidx + 1 , rowmin, rowmax), clamp(colidx + 4, colmin,colmax))

def find_possible_gear_parts(matrix):
    list_of_possible_parts = []
    foundDigit = ""
    started = False
    for rowidx, row in enumerate(matrix):
        for colidx, element in enumerate(row):             
            if not element.isdigit():
                if foundDigit != "" and started and colidx != 0:
                    list_of_possible_parts.append(foundDigit)
                foundDigit = ""
                started = False
            elif element.isdigit() and started:
                if colidx == (len(matrix[0]) - 1):
                    foundDigit = ""
                    started = False
                else:
                    foundDigit += element
            elif element.isdigit() and (colidx != 0 and not str(row[colidx-1]).isdigit()):
                foundDigit += element
                started = True

    return list_of_possible_parts

    # Unpack the coordinates
    (x1_min, y1_min), (x1_max, y1_max) = coord1
    (x2_min, y2_min), (x2_max, y2_max) = coord2

    # Check for overlap
    return not (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max)

file_path = '3/input.txt'

with open(file_path, 'r') as file:
    input_strings = [line.strip() for line in file.readlines()]

#region add . frame
matrix = [list(row) for row in input_strings]
matrix.insert(0, ['.' for _ in range(len(matrix[0]))])
matrix.append(['.' for _ in range(len(matrix[0]))])

for row in matrix:
    row.insert(0, '.')
    row.append('.')
#endregion

actual_parts = []

possible_parts = find_possible_parts(matrix)

for partNr in possible_parts:
    if is_special_character_adjecent(extract_submatrix(matrix, partNr[1][0], partNr[1][1])):
        actual_parts.append(int(partNr[0]))

print(sum(actual_parts))

# Part 2

possible_gear = find_gear_symbol(matrix)

ratios = []

for gear in possible_gear:
    possible_gear_parts = find_possible_gear_parts(extract_submatrix(matrix, gear[0], gear[1]))
    if len(possible_gear_parts) > 1:
        ratios.append(int(possible_gear_parts[0]) * int(possible_gear_parts[1]))

print(sum(ratios))
