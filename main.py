import random
def play_game():
    n=random.randint(1,50)
    a=-1
    guesses=0
    print("Welcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 50. Can you guess it?")
    
    while(a!=n):
        try:
            a = int(input("Guess the Number (between 1 and 50): "))
            if a<1 or a>50:
                print("Please enter a number within the range 1 to 50.")
                continue   
            
            guesses += 1
            
            if a > n:
                print("Lower Number Please :(")
            elif a < n:
                print("Higher Number Please :(")
        except ValueError:
            print(print("Invalid input! Please enter a valid integer."))

    print(f"Congratulations! You guessed the correct number {n} in {guesses} attempts.")
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing! Goodbye")
        
play_game()
    
    