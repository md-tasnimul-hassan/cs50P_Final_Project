from prettytable import PrettyTable
import sys
import time
import csv
import re
from games.tickTackToe import tickTacToe
from games.hangman import hangman
from games.littleProfessor import littleProfessor

def validate_email(email):
    """Validate email format - returns True if valid, False otherwise"""
    if not email or not isinstance(email, str):
        return False
    return bool(re.search(r"^\w+@\w+\.\w+$", email.strip().lower()))

def validate_name(name):
    """Validate name format - returns True if valid, False otherwise"""
    if not name or not isinstance(name, str):
        return False
    return bool(re.search(r"\w+", name.strip()))

def calculate_win_rate(wins, total_games):
    """Calculate win rate percentage - returns float"""
    if total_games <= 0:
        return 0.0
    return round((wins / total_games) * 100, 1)

def updateStat(id, gameName, total, win, lose, draw=0):
    """Update user statistics in the database after playing a game"""
    if id == None:
        return
    
    # Read current database
    db = []
    with open("stat/db.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            db.append(line)
    
    # Map game names to CSV column prefixes
    game_prefixes = {
        "t": "ttt",   # Tic-Tac-Toe
        "h": "hm",    # Hangman
        "l": "lp"     # Little Professor
    }
    
    if gameName not in game_prefixes:
        return
    
    prefix = game_prefixes[gameName]
    
    # Find and update user's stats
    for user in db:
        if user["id"] == id:
            # Update games, wins, losses (and draws for ttt)
            user[f"{prefix}_games"] = str(int(user[f"{prefix}_games"]) + total)
            user[f"{prefix}_wins"] = str(int(user[f"{prefix}_wins"]) + win)
            user[f"{prefix}_losses"] = str(int(user[f"{prefix}_losses"]) + lose)
            if prefix == "ttt":  # Only Tic-Tac-Toe has draws
                user[f"{prefix}_draws"] = str(int(user[f"{prefix}_draws"]) + draw)
            break
    
    # Write updated database back
    with open("stat/db.csv", "w", newline='') as f:
        fieldnames = ["id", "name", "ttt_games", "ttt_wins", "ttt_losses", "ttt_draws", 
                     "hm_games", "hm_wins", "hm_losses", "lp_games", "lp_wins", "lp_losses"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(db)

def showStat(id):
    """Display user statistics from all games"""
    if id == None:
        print("\nLogin to see your stats.\n")
        return
    
    # Read database
    db = []
    with open("stat/db.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            db.append(line)
    
    # Find the user
    user_data = None
    for user in db:
        if user["id"] == id:
            user_data = user
            break
    
    if not user_data:
        print("\nUser not found in database.\n")
        return
    
    # Display statistics
    print(f"\n=== Statistics for {user_data['name']} ===\n")
    
    # Tic-Tac-Toe stats (with draws)
    ttt_games = int(user_data["ttt_games"])
    ttt_wins = int(user_data["ttt_wins"])
    ttt_losses = int(user_data["ttt_losses"])
    ttt_draws = int(user_data["ttt_draws"])
    ttt_winrate = calculate_win_rate(ttt_wins, ttt_games)
    
    # Hangman stats
    hm_games = int(user_data["hm_games"])
    hm_wins = int(user_data["hm_wins"])
    hm_losses = int(user_data["hm_losses"])
    hm_winrate = calculate_win_rate(hm_wins, hm_games)
    
    # Little Professor stats
    lp_games = int(user_data["lp_games"])
    lp_wins = int(user_data["lp_wins"])
    lp_losses = int(user_data["lp_losses"])
    lp_winrate = calculate_win_rate(lp_wins, lp_games)
    
    # Create detailed stats table
    table = PrettyTable()
    table.field_names = ["Game", "Games", "Wins", "Losses", "Draws", "Win Rate"]
    table.add_rows([
        ["Tic-Tac-Toe", ttt_games, ttt_wins, ttt_losses, ttt_draws, f"{ttt_winrate:.1f}%"],
        ["Hangman", hm_games, hm_wins, hm_losses, "-", f"{hm_winrate:.1f}%"],
        ["Little Professor", lp_games, lp_wins, lp_losses, "-", f"{lp_winrate:.1f}%"]
    ])
    print(table)
    
    # Overall stats
    total_games = ttt_games + hm_games + lp_games
    total_wins = ttt_wins + hm_wins + lp_wins
    overall_winrate = calculate_win_rate(total_wins, total_games)
    
    print(f"\nTotal Games Played: {total_games}")
    print(f"Total Wins: {total_wins}")
    print(f"Overall Win Rate: {overall_winrate:.1f}%\n")
    
    input("Press enter to go back to menu...")

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
            if not validate_email(id):
                raise ValueError
            # check if user already exists
            for line in db:
                if(line["id"] == id):
                    Found = True 
                    break
            # Get name for new user
            if not Found:
                name = input("Enter your name: ").strip().title()
                if not validate_name(name):
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
            # Write new user with all stat columns: id, name, ttt(3), hm(3), lp(3) = 12 columns
            writer.writerow([id, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
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
                [totalGames, totalWins, totalLoses, totalDraws] = tickTacToe()
                updateStat(id, "t", totalGames, totalWins, totalLoses, totalDraws)
            case '2':
                [total, done] = hangman()
                updateStat(id, "h", total, done, total-done)
            case '3':
                [totalGame, totalWin] = littleProfessor()
                updateStat(id, "l", totalGame, totalWin, totalGame-totalWin) 
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
