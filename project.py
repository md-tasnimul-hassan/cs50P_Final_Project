from prettytable import PrettyTable
import sys
import time
import csv
import re

def updateStat(id):
    if(id == None):
        return
    pass

def showStat(id):
    if(id == None):
        print("Login to see your stats.")
        mainMenu()
    else:
        pass

def login():
    db = []
    # load the database
    with open("stat/db.csv", "r") as f:
        lines = csv.DictReader(f)
        for line in lines: 
            db.append(line)
    
    # getting user email as id and name
    Found = False
    print("*** Try to use a valid email. You need this to login later :)")
    while True:
        try:
            id = input("Enter your email: ").lower().strip()
            if(not re.search(r"^\w+@\w+\.\w+$" ,id)):
                raise ValueError
            # check if user already exists
            for line in db:
                if(line["id"] == id):
                    Found = True 
                    break
            # Get name for new user
            if not Found:
                name = input("Enter your name: ").strip().title()
                if(not re.search(r"\w+", name)):
                    raise ValueError
            break
        except:
            print("Invalid Email address or name.")

    if Found:
        for line in db:
            if(line["id"] == id):
                name = line["name"]
                break
        print(f"\nWelcome again, {name}. Enjoy!\n")
    else:
        with open("stat/db.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([id, name, 0, 0, 0])
        print("\nAccount created successfully!")
        print(f"\nWelcome, {name}. Enjoy!\n")
    mainMenu(name, id)

def mainMenu(name="Guest", id=None):
    while True:
        table = PrettyTable()
        table.field_names = ["Option", "Name"]
        table.add_rows(
            [
                ["1", "Play Tick-Tac-Toe"],
                ["2", "Play Hangman"],
                ["3", "Play Little Professor"],
                ["4", "Show My Statistics"],
                ["0", "EXIT"],
            ]
        )
        print(table)
        while True:
            try:
                response = input("Option: ")
                if response in ['1', '2', '3', '4', '0']:
                    break
            except:
                print("Invalid input!")
        
        match(response):
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass 
            case '4':
                showStat(id)
            case '0':
                print("Exiting successfully",end="")
                for _ in range(3):
                    time.sleep(0.5)
                    print(".",end='',flush=True)
                sys.exit(f"\nGood Bye, {name}!")

def about():
    table = PrettyTable()
    table.field_names = ["Name", "Link"]
    table.add_rows(
        [
            ["Website", "sites.google.com/view/md-tasnimul-hassan"],
            ["LinkedIn", "linkedin.com/in/md-tasnimul-hassan"],
            ["GitHub", "github.com/md-tasnimul-hassan"],
        ]
    )
    print("\n")
    print(table)
    input("\nPress enter to go back.")
    main()
    

def main():
    table = PrettyTable()
    table.field_names = ["Option", "Name"]
    table.add_rows(
        [
            ["1", "Log In / Sign up"],
            ["2", "Continue as Guest"],
            ["3", "About the Author"],
            ["0", "EXIT"],
        ]
    )
    print(table)
    while True:
        try:
            command = int(input("Option: "))
            validOptions = [1,2,3,0]
            if(command not in validOptions):
                raise ValueError
            break
        except:
            print("Invalid input! Please see the table above mentioned.")
    match (command):
        case 1:
            login()
        case 2:
            mainMenu()
        case 3:
            about()
        case 0:
            print("Exiting successfully",end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".",end='',flush=True)
            sys.exit("\nGood Bye!")

if(__name__ == "__main__"):
    main()
