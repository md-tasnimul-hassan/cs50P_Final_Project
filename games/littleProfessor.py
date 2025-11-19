import random
from prettytable import PrettyTable

def generateNumbers(difficulty):
    if difficulty == "easy":
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return [x, y]
    elif difficulty == "medium":
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return [x, y]
    else:
        x = random.randint(1000, 9999)
        y = random.randint(1000, 9999)
        return [x, y]

def littleProfessor():
    table = PrettyTable()
    table.field_names = ["Option", "Difficulty"]
    table.add_rows(
        [
            ["1", "Easy"],
            ["2", "Medium"],
            ["3", "Hard"],
        ]
    )
    print(table)
    while True:
        try:
            response = input("Option: ")
            if response not in ['1', '2', '3']:
                raise ValueError
            break
        except:
            print("Invalid input")
    match(response):
        case '1':
            difficulty = "easy"
        case '2':
            difficulty = "medium"
        case '3':
            difficulty = "hard"
    totalGame = 0
    totalWin = 0
    i = 0
    while (i<5):
        [x, y] = generateNumbers(difficulty)
        mode = ['p', 'm']
        choice = random.choice(mode)
        userTry = 0
        success = False
        if choice == 'p':
            while userTry < 3:
                try:
                    response = int(input(f"{x} + {y} = "))
                    if response == (x+y):
                        success = True
                        print("Correct !")
                        totalWin += 1
                        break
                    else:
                        userTry += 1
                        print(f"Opps wrong! You have {3-userTry} tries left.")
                except:
                    print("Please enter a number.")
            
            if not success:
                print(f"Correct Answer: {x} + {y} = {x+y}")
        else:
            while userTry < 3:
                try:
                    response = int(input(f"{max(x,y)} - {min(x,y)} = "))
                    if response == (max(x,y)-min(x,y)):
                        success = True
                        print("Correct !")
                        totalWin += 1
                        break
                    else:
                        userTry += 1
                        print(f"Opps wrong! You have {3-userTry} tries left.")
                except:
                    print("Please enter a number.")
            
            if not success:
                print(f"Correct Answer: {x} + {y} = {max(x,y)-min(x,y)}")
        i += 1
        if(i == 5):
            state = input("Enter 'q' to quit the game. Press anyother key or just enter to continue ")
            if(state != 'q'):
                i = 0
    return [totalGame, totalWin]
