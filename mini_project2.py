import random

while True:
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize the attempt counter
    print("\nNew game started! You have 3 guesses to find the number.")

    while attempts < 3:
        user = input("Enter your guess (or 'q' to quit): ")
        if user == 'q':
            print('You quit the game. Thank you for playing!')
            exit()  # Exit the game completely

        user = int(user)  # Convert the input to an integer
        attempts += 1  # Increment the attempt counter

        if user == number:
            print("Congratulations! You guessed the correct number!")
            break
        elif user < number:
            print("Your guess is too small. Try a larger number.")
        else:
            print("Your guess is too large. Try a smaller number.")

        if attempts == 3:
            print(f"Game over! The correct number was {number}.")
    
    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thank you for playing! Goodbye!")
        break
