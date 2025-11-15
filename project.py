from prettytable import PrettyTable
import sys

def login():
    pass

def signup():
    pass

def auth():
    pass

def passwordGenerate():
    pass

def printMenu():
    pass

def main():
    table = PrettyTable()
    table.field_names = ["Command", "Name"]
    table.add_rows(
        [
            ["1", "Log In"],
            ["2", "Sign Up"],
            ["3", "Continue as Guest"],
            ["0", "EXIT"],
        ]
    )
    print(table)
    while True:
        try:
            command = int(input("Command: "))
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
            signup()
        case 3:
            printMenu()
        case 0:
            sys.exit("Exiting successfully... Goodbye!")

if(__name__ == "__main__"):
    main()
