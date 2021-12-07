import random, sys
from art import logo

# Ace card is represented as 11.
# Jack, Queen and King represented as 10.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = random.choice(cards)
dealer_cards = random.choice(cards)

user = []
computer = []
for i in range(0, 2):
    user.append(player_cards)
    computer.append(dealer_cards)

print(logo)
print(f"The dealer's first card is: {computer[0]}.")
print(f"Your cards are: {user[0]} and {user[1]}.")

user_sum = sum(user)
computer_sum = sum(computer)

# First element of cards list is 11, i.e. Ace
ace = cards[0] 

if ace in user:
    if user_sum <= 21:
        ace = 11
    else: 
        ace = 1 

if ace in computer:
    if computer_sum < 21:
        ace = 11
    else: 
        ace = 1

if user_sum > 21:
    print(f"Sorry, you lost. Your cards total is more than 21.")
    sys.exit()
elif computer_sum == 21:
    print(f"The dealer won with cards: {computer[::]}.")
    sys.exit()
elif user_sum == 21:
    print("You won!")
    sys.exit()

answer = print(input("Do you want another card? Type 'y' for yes or 'n' for pass: "))
ans = str(answer)
while user_sum < 21 and computer_sum < 21:
    try:      
        if ans.lower() == 'y':
            user.append(random.choice(cards))
            print(f"You drew a: {user[-1]}. Your new total is: {user_sum}.")
        elif ans.lower() == 'n':
            if computer_sum > user_sum:
                print(f"The dealer won with cards: {computer}.")
                break
            elif user_sum > computer_sum:
                print(f"You won with cards: {user}")
                break
            elif user_sum == computer_sum:
                print("It was a draw!")
                break
    except ValueError:
        print("That was not a valid response.")
        continue
   