import csv
import random

def get_word():
    words = []
    with open("games/hangwords.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            for w in row:
                w = w.strip()
                if w:
                    words.append(w)
    return random.choice(words).lower()

def show_word(word, hide_pos, guessed):
    out = []
    for i in range(len(word)):
        if i in hide_pos and word[i] not in guessed:
            out.append("*")
        else:
            out.append(word[i].upper())
    return " ".join(out)

def hangman():
    print("\n=== HANGMAN GAME ===")
    print("Guess 3 words to win!\n")

    total = 3
    done = 0

    for r in range(1, total + 1):
        print(f"\n--- Round {r}/{total} ---")

        word = get_word()
        ln = len(word)

        to_hide = 3 if ln >= 3 else ln
        hide_pos = set(random.sample(range(ln), to_hide))

        hidden_letters = set(word[i] for i in hide_pos)
        guessed = set()

        wrong = 0
        limit = 6

        while wrong < limit:
            print("\nWord:", show_word(word, hide_pos, guessed))
            found = len(hidden_letters & guessed)
            print(f"Hidden letters found: {found}/{to_hide}")

            if guessed:
                print("Guessed:", ", ".join(sorted(x.upper() for x in guessed)))
            else:
                print("Guessed: None")

            print(f"Wrong left: {limit - wrong}")

            if hidden_letters.issubset(guessed):
                print(f"\nNice! You found the word: {word.upper()}")
                done += 1
                break

            g = input("\nGuess a letter: ").strip().lower()

            if len(g) != 1 or not g.isalpha():
                print("Enter a single letter.")
                continue

            if g in guessed:
                print("Already guessed.")
                continue

            guessed.add(g)

            if g in hidden_letters:
                print("Correct!")
            else:
                wrong += 1
                if g in word:
                    print("Letter exists but not hidden.")
                else:
                    print("Wrong!")

        if wrong == limit:
            print(f"\nYou failed! Word was: {word.upper()}")
            break

    print("\n=== GAME OVER ===")
    print(f"You completed {done}/{total} rounds.")

    return [total, done]
