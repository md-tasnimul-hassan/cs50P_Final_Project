import re
import random

FIRSTUSERMOVE = True 
WIN_LINES = [
    [(0,0), (0,1), (0,2)],  # rows
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],

    [(0,0), (1,0), (2,0)],  # columns
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],

    [(0,0), (1,1), (2,2)],  # diagonals
    [(0,2), (1,1), (2,0)]
]

def printBoard(board):
    print(f"\n  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}\n-----------------\n  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}\n-----------------\n  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}\n")

def checkStatus(board):
    # it checks the current board status. If game ends it returns [True, winnerMarker], if game continues it returns [False, ""] and if game draws, it returns [True, "."]
    # first lets check win or lose condition

    global WIN_LINES
    for line in WIN_LINES:
        (r1, c1), (r2, c2), (r3, c3) = line

        m1 = board[r1][c1]
        m2 = board[r2][c2]
        m3 = board[r3][c3]

        # If markers are equal and not empty we got winner
        if m1 != " " and m1 == m2 == m3:
            return [True, m1]   
    
    # then check whether game is running or drawed

    for i in range(3):
        for j in range(3):
            if(board[i][j] == " "):
                return [False, ""]

    return [True, "."]


def userMove(board, userMarker):
    global FIRSTUSERMOVE
    if(FIRSTUSERMOVE):
        print("Input in the following pattern => 1 2")
        FIRSTUSERMOVE = False
    while True:
        try:
            response = input("Your Move: ").strip()
            matches = re.search (r"^(\d{1}) (\d{1})$", response)
            x = int(matches.group(1))
            y = int(matches.group(2))
            if(x not in [1, 2, 3] or y not in [1, 2, 3]):
                raise ValueError
            break
        except:
            print("Invalid input!")
            pass
    board[x-1][y-1] = userMarker 
    

def aiMove(board, aiMarker):
    pass

def tickTacToe():
    win_messages = [
        "You won! I have no idea how, but congrats anyway!",
        "Victory is yours! Your skills—or luck—were impressive.",
        "You actually beat me! Time to celebrate in your chair.",
        "Wow, you won! I guess I underestimated human genius.",
        "You did it! I’ll pretend it was your skill and not my mercy.",
        "Well done! That win was suspiciously impressive.",
        "You crushed the computer! Or maybe I just let it happen.",
        "You beat me fair and square! I’m shocked... and mildly impressed."
    ]

    lose_messages = [
        "You lost! Don’t worry, the computer doesn’t hold grudges (usually).",
        "GG! I win again, and your ego might need a bandage.",
        "Ouch! That loss must sting... don’t worry, here is some tissues.",
        "You lost! It’s okay, everyone needs practice (except me).",
        "You lost! I’d say 'try harder,' but I already know you will.",
        "I win! Don’t feel bad, human, it happens to the best of us.",
        "Lost again? Blame the computer, not your poor choices."
    ]

    draw_messages = [
        "It’s a draw! We are equally mediocre... for now.",
        "Tie game! Neither of us was skilled enough to win.",
        "A draw! Clearly, we are perfectly matched.",
        "It’s a tie! I think we both tried… kind of.",
        "A draw! Nobody wins, but at least nobody loses badly.",
        "Tie game! Mutual respect for mediocrity achieved.",
        "It’s a tie! Let’s pretend we planned this dramatic ending."
    ]

    board = [[" "]*3 for _ in range(3)]
    
    while True:
        userMarker = input("Choose: 'o' or 'x' ? ")
        if(userMarker in ['o', 'x']):
            break
    aiMarker = 'o' if userMarker == 'x' else 'x'

    while (not checkStatus(board)[0]):
        userMove(board, userMarker)
        printBoard(board)
    
    if(checkStatus(board)[1] == userMarker):
        print(random.choice(win_messages))
    elif(checkStatus(board)[1] == aiMarker):
        print(random.choice(lose_messages))
    else:
        print(random.choice(draw_messages))

tickTacToe()