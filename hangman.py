import random

def choose_word():
    """Word list nunchi random ga oka word pick chesthundi bro"""
    words = ["python", "coding", "laptop", "hangman", "program", "intern", "github", "telugu"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    """Guessed letters chupisthundi, migathavi '_' ga chupisthundi bro"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_hangman(tries):
    """Tries thagginattu hangman figure draw avthundi bro"""
    stages = [
        """
           |
           | O
           | \\|/
           | |
           | / \\
           -
        """,
        """
           |
           | O
           | \\|/
           | |
           | / 
           -
        """,
        """
           |
           | O
           | \\|/
           | |
           | 
           -
        """,
        """
           |
           | O
           | \\|
           | |
           | 
           -
        """,
        """
           |
           | O
           | |
           | |
           | 
           -
        """,
        """
           |
           | O
           | 
           | 
           | 
           -
        """,
        """
           |
           | 
           | 
           | 
           | 
           -
        """ # <-- closed this properly
    ]
    return stages[tries]

# Example usage
def play_game():
    word = choose_word()
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman bro!")
    
    while tries > 0:
        print(display_hangman(tries))
        print("Word:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(guessed_letters))
        
        guess = input("Oka letter guess cheyu: ").lower()
        
        if guess in guessed_letters:
            print("Already guess chesav bro!")
            continue
            
        guessed_letters.append(guess)
        
        if guess not in word:
            tries -= 1
            print(f"Wrong bro! {tries} tries migilayi")
        
        if all(letter in guessed_letters for letter in word):
            print("Word:", word)
            print("Super bro, nuvvu gelichesav! 🎉")
            break
    else:
        print(display_hangman(tries))
        print(f"Game over bro. Word enti ante: {word}")

if __name__ == "__main__":
    play_game()