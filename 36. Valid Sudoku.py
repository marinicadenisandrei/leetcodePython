# good board example
board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# bad board example
# board = [
# ["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]
# ]

lista_numere = []
counter = 0
flag = []

# verificare pe linii
for i in range(len(board)):
    for j in range(len(board[i])):
        for k in range(len(board[i])):
            if board[i][k] != ".": 
                if board[i][j] == board[i][k]:
                    counter += 1
        
        if counter > 1:
            flag.append(True)
            break
        else:
            counter = 0


counter = 0
for i in range(len(board)):
    for j in range(len(board)):
        for k in range(len(board[j])):
            if board[j][k] != "." and board[j][i] != ".":
                if  board[j][k] == board[j][i] != ".":
                    counter += 1
        if counter > 1:
            flag.append(True)
            break
        else:
            counter = 0
    break

line = 0
index = 0
offset = 0
lista_square = [[] for i in range(len(board))]

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
            lista_square[j+offset].extend(board[i][index:index+3]) 
            index += 3

counter_square = 0
flag_square = False
       
for i in range(len(lista_square)):
    for j in range(len(lista_square[i])):
        for k in range(len(lista_square[i])):
            # print(lista_square[i][j], lista_square[i][k])
            if lista_square[i][j] == lista_square[i][k] and lista_square[i][j] != "." and lista_square[i][k] != ".":
                counter_square += 1
            if counter_square == 2:
                flag_square = True
                flag.append(True)
            # print("counter = ",counter_square)
            
        counter_square = 0   
    counter_square = 0


if len(flag) == 0:
    print(True)
else:
    print(False)



  