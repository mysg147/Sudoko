"""board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,8],
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    print("\n")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("___________________")
print("\n")
print_board(board)"""

# A Backtracking program in Python to solve Sudoku problem 


# A Utility Function to print the Grid 
def print_grid(arr): 
	for i in range(9): 
		for j in range(9): 
			print (arr[i][j],end=' ') 
		print ('\n') 

		
# Function to Find the entry in the Grid that is still not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remains, false is returned. 
# 'l' is a list variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
def find_empty_location(arr, l): 
	for row in range(9): 
		for col in range(9): 
			if(arr[row][col]== 0): 
				l[0]= row 
				l[1]= col 
				return True
	return False

# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
def used_in_row(arr, row, num): 
	for i in range(9): 
		if(arr[row][i] == num): 
			return True
	return False

# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def used_in_col(arr, col, num): 
	for i in range(9): 
		if(arr[i][col] == num): 
			return True
	return False

# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr, row, col, num): 
	for i in range(3): 
		for j in range(3): 
			if(arr[i + row][j + col] == num): 
				return True
	return False

# Checks whether it will be legal to assign num to the given row, col 
# Returns a boolean which indicates whether it will be legal to assign 
# num to the given row, col location. 
def check_location_is_safe(arr, row, col, num): 
	
	# Check if 'num' is not already placed in current row, 
	# current column and current 3x3 box 
	return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num) 

# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(arr): 
	
	# 'l' is a list variable that keeps the record of row and col in find_empty_location Function	 
	l =[0, 0] 
	
	# If there is no unassigned location, we are done	 
	if(not find_empty_location(arr, l)): 
		return True
	
	# Assigning list values to row and col that we got from the above Function 
	row = l[0] 
	col = l[1] 
	
	# consider digits 1 to 9 
	for num in range(1, 10): 
		
		# if looks promising 
		if(check_location_is_safe(arr, row, col, num)): 
			
			# make tentative assignment 
			arr[row][col]= num 

			# return, if success, ya ! 
			if(solve_sudoku(arr)): 
				return True

			# failure, unmake & try again 
			arr[row][col] = 0
			
	# this triggers backtracking		 
	return False

# Driver main function to test above functions 
if __name__=="__main__": 
	
	# creating a 2D array for the grid 
	grid =[[0 for x in range(9)]for y in range(9)] 
	
	# assigning values to the grid 
	grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
		[5, 2, 0, 0, 0, 0, 0, 0, 0], 
		[0, 8, 7, 0, 0, 0, 0, 3, 1], 
		[0, 0, 3, 0, 1, 0, 0, 8, 0], 
		[9, 0, 0, 8, 6, 3, 0, 0, 5], 
		[0, 5, 0, 0, 9, 0, 6, 0, 0], 
		[1, 3, 0, 0, 0, 0, 2, 5, 0], 
		[0, 0, 0, 0, 0, 0, 0, 7, 4], 
		[0, 0, 5, 2, 0, 6, 3, 0, 0]] 
	
	# if success print the grid 
	if(solve_sudoku(grid)): 
		print_grid(grid) 
	else: 
		print ("No solution exists")

# The above code has been contributed by Harshit Sidhwa. 
