import random

# Display the choices
choices = ['rock', 'paper', 'scissors']

# Game loop
while True:
    print("\nChoose: rock, paper, or scissors (or type 'quit' to exit)")
    user_choice = input("Your choice: ").lower()
    
    if user_choice == 'quit':
        print("Thanks for playing! Goodbye!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
