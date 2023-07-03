board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

board_vertical = [[] for i in range(9)]

for i in range(len(board)):
    for j in range(len(board)):
        board_vertical[i].append(board[j][i])
        
index = 0
offset = 0
board_squares = [[] for i in range(len(board))]
for i in range(len(board)):
    if i < 3:
        offset = 0
        index = 0
    elif i > 2 and i < 6:
        offset = 3
        index = 0
    elif i > 5:
        offset = 6
        index = 0
        
    for j in range(3):
            board_squares[j+offset].extend(board[i][index:index+3]) 
            index += 3

list_of_numbers = [1,2,3,4,5,6,7,8,9]


############################### lines
print("###############################")
print("orizontal board \n")
for i in board:
    print(i)

print("\nvertical board \n")
for i in board_vertical:
    print(i)
    
print("\nsquares board \n")
for i in board_squares:
    print(i)

print("###############################\n")
###############################


for i in board:
    for j in board_vertical:
        for k in board_squares:
            print(i,j,k)
            break
        break
    break
print("\n#######################################\n")

big_list = []
offset = 0
potential_numbers = []

counter_test = 0
last = [0]

for square in board_squares:
    for index in range(len(square)):
        if square[index] == ".":
            big_list.extend(square)
            
            if index < 3:
                big_list.extend(board_vertical[index + offset])
                big_list.extend(board[0])
                
            if index >= 3 and index < 6:
                big_list.extend(board_vertical[index + offset - 3])
                big_list.extend(board[1])
                
            if index >= 6 and index < 9:
                big_list.extend(board_vertical[index + offset - 6])
                big_list.extend(board[2])
            
            for sudoku_nr in range(10):
                if not str(sudoku_nr) in big_list:
                    print("sudocu number ",sudoku_nr)
                    potential_numbers.append(str(sudoku_nr))
                    # square[index] = sudoku_nr
                    # break
                    
            if last[-1] == 9 and "1" in potential_numbers:
                square[index] = "1"
                last.append(1)
                potential_numbers[-1] = "1"
            else:
                square[index] = potential_numbers[-1]
                last.append(int(potential_numbers[-1]))
                
            
            # square[index] = potential_numbers[-1]
            
            if offset == 0:
                if index < 3:
                    board_vertical[index + offset][index-2] = potential_numbers[-1]
                    board[0][index] = potential_numbers[-1]
                    
                if index >= 3 and index < 6:
                    board_vertical[index + offset - 3][index-3] = potential_numbers[-1]
                    board[1][index-3] = potential_numbers[-1]
                    
                    
                if index >= 6 and index < 9:
                    board_vertical[index + offset - 6][index-4] = potential_numbers[-1]
                    # print(board_vertical[index + offset - 6][index-4], "vert")
                    board[2][index-6] = potential_numbers[-1]
            
            elif offset == 3:
                if index < 3:
                    board_vertical[index + offset][index] = potential_numbers[-1]
                    board[0][index + offset] = potential_numbers[-1]
                    
                if index >= 3 and index < 6:
                    board_vertical[index - 3][index-3] = potential_numbers[-1]
                    board[1][index + offset - 3] = potential_numbers[-1]
                    
                    
                if index >= 6 and index < 9:
                    # board_vertical[index - 6][index-4] = potential_numbers[-1]
                    print(board_vertical[index + offset - 6], "vert")
                    board[2][index + offset - 6] = potential_numbers[-1]
            
            elif offset == 6:
                if index < 3:
                    board_vertical[index + offset][index] = potential_numbers[-1]
                    board[0][index + offset] = potential_numbers[-1]
                    
                if index >= 3 and index < 6:
                    board_vertical[index - 3][index-3] = potential_numbers[-1]
                    board[1][index + offset - 3] = potential_numbers[-1]
                    
                    
                if index >= 6 and index < 9:
                    board_vertical[index + offset - 2][index-4] = potential_numbers[-1]
                    # print(board_vertical[index + offset - 6][index-4], "vert")
                    board[2][index + offset - 6] = potential_numbers[-1]
                
            
            
            
            potential_numbers = []
            
            
        
            print("\nbig: ", big_list, index, "\n\n\n")
            big_list = []
            
    
        
    counter_test += 1
    offset += 3
    print("#####################################################################################################################")
    
    if counter_test == 3:
        break
    
# for i in board_squares:
#     print(i)
    



board_enable = 1
if board_enable == 1:
    print("\n\n\n\n\n\n\n\n\n\n")
    ############################### lines
    print("###############################")
    print("orizontal board \n")
    for i in board:
        print(i)

    print("\nvertical board \n")
    for i in board_vertical:
        print(i)
        
    print("\nsquares board \n")
    for i in board_squares:
        print(i)

    print("###############################\n")
    ###############################

