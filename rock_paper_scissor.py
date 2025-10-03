import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice rock, paper, or scissors ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
   
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
 
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"The {winner} wins!")

def play_again():
   
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def main():
 
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors game")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Score - User: {user_score}, Computer: {computer_score}")

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
