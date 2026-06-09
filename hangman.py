import random

words = ["python", "computer", "coding", "laptop", "program"]

word = random.choice(words)

guessed_letters = []
attempts = 6

display_word = ["_"] * len(word)

while attempts > 0 and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)