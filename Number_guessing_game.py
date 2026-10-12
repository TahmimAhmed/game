import random

while True:
    number = random.randint(1, 100)
    attempts = 0
    print("\nNew game started! You have 3 guesses.")
    print("Guess a number between 1 and 100.")

    while attempts < 3:
        user = input("Enter your guess (or 'q' to quit): ").strip()

        if user.lower() == 'q':
            print("Thank you for playing! Goodbye!")
            raise SystemExit

        # Check whether the input is a whole number
        try:
            guess = int(user)
        except ValueError:
            print("Please enter a number between 1 and 100.")
            continue

        # Check whether the number is within the allowed range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        # Only valid guesses count as attempts
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the correct number!")
            break

        if attempts == 3:
            print(f"Game over! The correct number was {number}.")
        elif guess < number:
            print("Your guess is too small. Try a larger number.")
        else:
            print("Your guess is too large. Try a smaller number.")

    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()

    if play_again != 'y':
        print("Thank you for playing! Goodbye!")
        break
