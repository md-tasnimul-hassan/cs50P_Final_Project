import re
firtUserMove = True 

def printBoard(board):
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}\n--------------\n  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}\n--------------\n  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}\n")

def checkStatus(board):
    # it checks the current board status. If game ends it returns [True, winnerMarker], if game continues it returns [False, ""] and if game draws, it returns [True, "."]
    pass

def userMove():
    if(firtUserMove):
        print("Input in the following pattern => 1 2")
        firtUserMove = False
    while True:
        try:
            response = input("Your Move: ").strip()
            matches = re.search ("^(\d{1}) (\d{1})$", response)
            x = int(matches.group(1))
            y = int(matches.group(2))
            if(x not in [1, 2, 3] or y not in [1, 2, 3]):
                raise ValueError
            break
        except:
            print("Invalid input!")
            pass
    return [x-1,y-1]
    

def aiMove():
    pass

def tickTacToe():
    board = [[""]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j] = '';
    
    while True:
        userMarker = input("Choose: 'o' or 'x' ? ")
        if(userMarker in ['o', 'x']):
            break
    
    printBoard(board)


tickTacToe()