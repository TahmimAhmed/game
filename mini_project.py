
import random
number= random.randint(1,100)

while True:
    user=(input("enter the number:"))
    if user=='q':
        break
    user=int(user)         #i can't understand this line
    if user== number:
        print('successfully correct guess')
        break
    elif user<number:
        print('your number is small so you should take big number')
    else:
        print('your number is big so you should take small numberr')
print('game over')    












import random

number = random.randint(1, 10)

while True:
    attempts = 0  # Initialize the attempt counter
    while attempts < 3:
        user = input("Enter the number (or 'q' to quit): ")
        if user == 'q':
            print('You quit the game.')
            break

        user = int(user)  # Convert the input to an integer

        if user == number:
            print('Successfully correct guess!')
            break
        elif user < number:
            print('Your number is small, so you should try a bigger number.')
        else:
            print('Your number is big, so you should try a smaller number.')

        attempts += 1  # Increment the attempt counter

    if attempts == 3:
        print('Game Over! You have used all 3 attempts.')

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print('Thank you for playing!')
        break

