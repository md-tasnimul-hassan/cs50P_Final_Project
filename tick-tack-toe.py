firtUserMove = True 

def printBoard(board):
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}\n--------------\n  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}\n--------------\n  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}\n")

def checkStatus():
    pass

def userMove():
    if(firtUserMove):
        x,y = input("Input in the following pattern => 1 2\nYour Move: ")
        firtUserMove = False
    else:
        print("Your Move: ")
    
    

def aiMove():
    pass

def main():
    board = [[""]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j] = '';
    
    while True:
        userMarker = input("Choose: 'o' or 'x' ? ")
        if(userMarker in ['o', 'x']):
            break
    
    printBoard(board)


if(__name__ == "__main__"):
    main()