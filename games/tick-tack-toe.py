import re
import random
import time
from prettytable import PrettyTable

global FIRSTUSERMOVE 
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
            if(x not in [1, 2, 3] or y not in [1, 2, 3] or board[x-1][y-1]!=' '):
                raise ValueError
            break
        except:
            print("Invalid input!")
            pass
    board[x-1][y-1] = userMarker 
    
def easyAiMove(board, aiMarker):
    print("AI is thinking",end="")
    for _ in range(3):
        time.sleep(0.7)
        print(".",end="",flush=True)
    print("\r\033[K", end="")

    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = aiMarker
    
    print(f"AI chose: {r+1} {c+1}")

def mediumAiMove(board, aiMarker, playerMarker):
    print("AI is thinking",end="")
    for _ in range(3):
        time.sleep(0.7)
        print(".",end="",flush=True)
    print("\r\033[K", end="")
    
    # try to win
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = aiMarker
                if checkStatus(board)[1] == aiMarker:
                    print(f"AI chose: {r+1} {c+1}")
                    return
                board[r][c] = " "

    # try to block user
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = playerMarker
                if checkStatus(board)[1] == playerMarker:
                    board[r][c] = aiMarker
                    print(f"AI chose: {r+1} {c+1}")
                    return
                board[r][c] = " "

    # otherwise random
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = aiMarker
    print(f"AI chose: {r+1} {c+1}")

def hardAiMove(board, aiMarker, playerMarker):

    print("AI is thinking", end="")
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print("\r\033[K", end="")

    def minimax(bd, isMaximizing):
        status, winner = checkStatus(bd)

        if status:
            if winner == aiMarker:
                return 1
            elif winner == playerMarker:
                return -1
            else:
                return 0

        if isMaximizing:
            best = -float("inf")
            for r in range(3):
                for c in range(3):
                    if bd[r][c] == " ":
                        bd[r][c] = aiMarker
                        score = minimax(bd, False)
                        bd[r][c] = " "
                        best = max(best, score)
            return best
        else:
            best = float("inf")
            for r in range(3):
                for c in range(3):
                    if bd[r][c] == " ":
                        bd[r][c] = playerMarker
                        score = minimax(bd, True)
                        bd[r][c] = " "
                        best = min(best, score)
            return best

    bestScore = -float("inf")
    move = None  # store the chosen move

    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = aiMarker
                score = minimax(board, False)
                board[r][c] = " "
                if score > bestScore:
                    bestScore = score
                    move = (r, c)

    if move:
        r, c = move
        board[r][c] = aiMarker
        print(f"AI chose: {r+1} {c+1}")

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
        "GG! I win, and your ego might need a bandage.",
        "Ouch! That loss must sting... don’t worry, here is some tissues.",
        "You lost! It’s okay, everyone needs practice (except me).",
        "You lost! I’d say 'try harder,' but I already know you will.",
        "I win! Don’t feel bad, human, it happens to the best of us.",
        "Lost? Blame the computer, not your poor choices. HaHa"
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

    mode = PrettyTable()
    mode.field_names = ["Command", "Difficulty"]
    mode.add_rows(
        [
            ["1", "Chilling"],
            ["2", "Serious"],
            ["3", "Bone Cracking"],
        ]
    )
    print(mode)
    while True:
        choice = input("Select a difficulty: ")
        if(choice in ['1','2','3']):
            break
    
    while True:
        userMarker = input("Choose: 'o' or 'x' ? ")
        if(userMarker in ['o', 'x']):
            break
    aiMarker = 'o' if userMarker == 'x' else 'x'

    while (not checkStatus(board)[0]):
        userMove(board, userMarker)
        printBoard(board)
        if(not checkStatus(board)[0]):
            match(choice):
                case '1':
                    easyAiMove(board, aiMarker)
                case '2':
                    mediumAiMove(board, aiMarker, userMarker)
                case '3':
                    hardAiMove(board, aiMarker, userMarker)
            printBoard(board)
        else:
            break
    
    if(checkStatus(board)[1] == userMarker):
        print(random.choice(win_messages))
    elif(checkStatus(board)[1] == aiMarker):
        print(random.choice(lose_messages))
    else:
        print(random.choice(draw_messages))

tickTacToe()

