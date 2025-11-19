# GameZone - Gamify with Python
#### Video Demo: <URL HERE>
#### Description:

## Overview
GameZone is an interactive Python-based gaming platform that brings together three classic games: Tic-Tac-Toe, Hangman, and Little Professor. This project was developed as the final project for CS50's Introduction to Programming with Python (CS50P). The application features a complete user authentication system, comprehensive statistics tracking, and an intuitive menu-driven interface that provides an engaging gaming experience.

## Project Structure

The project is organized into the following directory structure:

```
cs50P_Final_Project/
│
├── project.py              # Main application file with core functions
├── test_project.py         # Pytest test suite for core functions
├── requirements.txt        # Python package dependencies
├── README.md              # Project documentation
│
├── games/                 # Game modules directory
│   ├── tickTackToe.py    # Tic-Tac-Toe game implementation
│   ├── hangman.py        # Hangman game implementation
│   ├── hangwords.csv     # Word database for Hangman
│   └── littleProfessor.py # Little Professor math game
│
└── stat/                  # Statistics database directory
    └── db.csv            # User statistics database
```

## Features

### 1. User Authentication System
- **Sign Up/Login**: Users can create accounts with email validation using regex patterns
- **Guest Mode**: Play without registration, but statistics won't be saved
- **Email Format Validation**: Ensures proper email format (user@domain.com)
- **Name Validation**: Validates user names contain alphanumeric characters
- **Persistent Storage**: User data stored in CSV format for persistence across sessions

### 2. Three Classic Games

#### Tic-Tac-Toe
- Three difficulty levels:
  - **Chilling (Easy)**: AI makes random moves
  - **Serious (Medium)**: AI blocks user wins and attempts to win
  - **Bone Cracking (Hard)**: AI uses minimax algorithm for optimal play
- Choose your marker ('X' or 'O')
- Visual board display with clean formatting
- Win, loss, and draw detection
- Humorous custom messages for each game outcome
- Real-time game statistics tracking

#### Hangman
- Three-round game format
- 6 wrong guesses allowed per round
- Randomly hides exactly 3 positions in each word
- Large word database (1000+ words) from CSV file
- Visual word display with spaces between letters
- Shows guessed letters in uppercase
- Tracks hidden letters remaining
- Round-by-round scoring system

#### Little Professor
- Educational math game for practicing arithmetic
- Multiple difficulty levels
- Question generation with instant feedback
- Score tracking and performance statistics
- Designed to help improve mental math skills

### 3. Comprehensive Statistics Tracking

The application maintains detailed statistics for each user:

- **Per-Game Statistics**:
  - Total games played
  - Total wins
  - Total losses
  - Total draws (for Tic-Tac-Toe only)
  - Win rate percentage

- **Overall Statistics**:
  - Combined games across all three games
  - Overall win count
  - Overall win rate percentage

Statistics are displayed in a formatted table using PrettyTable library, making it easy to view performance at a glance.

### 4. Database Management

User data is stored in a CSV file (`stat/db.csv`) with the following structure:
- User ID (email)
- User name
- Tic-Tac-Toe: games, wins, losses, draws
- Hangman: games, wins, losses
- Little Professor: games, wins, losses

The database supports:
- Reading existing user data
- Creating new user accounts
- Updating statistics after each game
- Maintaining data integrity with proper CSV formatting

## Core Functions

### Main Application Functions (project.py)

1. **`main()`**
   - Entry point of the application
   - Displays main menu with login/signup options
   - Handles guest mode and author information
   - Coordinates overall program flow

2. **`login()`**
   - Manages user authentication
   - Handles both new user registration and returning user login
   - Validates email and name formats
   - Creates new database entries for first-time users
   - Redirects to main game menu after successful login

3. **`mainMenu(name, id)`**
   - Primary game selection interface
   - Provides access to all three games
   - Displays statistics option
   - Handles game return values and updates statistics
   - Implements graceful exit with goodbye message

4. **`updateStat(id, gameName, total, win, lose, draw=0)`**
   - Updates user statistics in the database
   - Maps game codes to CSV columns ('t', 'h', 'l')
   - Handles draws for Tic-Tac-Toe
   - Reads entire database, updates specific user, writes back
   - Maintains data consistency across updates

5. **`showStat(id)`**
   - Displays comprehensive user statistics
   - Calculates win rates for each game
   - Shows overall performance metrics
   - Formats data in an attractive table layout
   - Handles guest users appropriately

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/md-tasnimul-hassan/cs50P_Final_Project.git
   cd cs50P_Final_Project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python project.py
   ```

## Dependencies

- **prettytable**: For formatted table displays (menus and statistics)
- **pytest**: For running test suite (development only)

## Design Decisions

### Why CSV for Database?
I chose CSV format for the database because:
- Simple and human-readable
- No external database server required
- Built-in Python csv module provides robust handling

### AI Difficulty Implementation
The Tic-Tac-Toe AI uses three different strategies:
- **Easy**: Random moves to allow beginners to win
- **Medium**: Defensive and offensive tactics without lookahead
- **Hard**: Minimax algorithm for perfect play, providing maximum challenge


## Author Information

**Md Tasnimul Hassan**
- Website: [sites.google.com/view/md-tasnimul-hassan](https://sites.google.com/view/md-tasnimul-hassan)
- LinkedIn: [linkedin.com/in/md-tasnimul-hassan](https://linkedin.com/in/md-tasnimul-hassan)
- GitHub: [github.com/md-tasnimul-hassan](https://github.com/md-tasnimul-hassan)

## Acknowledgments

This project was created as the final project for CS50's Introduction to Programming with Python (CS50P). Special thanks to Professor David J. Malan and the entire CS50 team for their excellent course and inspiration.

## License

This project is open source and available under the MIT License.
