import random

# List of predefined words
words = ["python", "computer", "coding", "program", "keyboard"]

# Randomly select a word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("🎮 Welcome to Hangman Game")
print("=" * 40)

# Game Loop
while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong Guesses Left:", max_wrong_guesses - wrong_guesses)
    print("Guessed Letters:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Result
print("\n" + "=" * 40)

if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word.")
    print("Word:", word)
else:
    print("💀 Game Over!")
    print("The correct word was:", word)

print("=" * 40)
