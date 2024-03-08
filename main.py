import random

# Rolling the dice..
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# Getting the number of players..
while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Please enter a number between 1 and 4")
    else: 
        print("Please enter a valid number")

# Setting the max score and initializing the score board..   
max_score = 50
players_score = [0 for _ in range(players)]

# Starting the game loop..
while max(players_score) < max_score:

    # Current player loop..
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your score is:", players_score[player_idx], "\n")
        current_score = 0
        
        # Starting a turn..
        while True:
            should_roll = input("Do you want to roll? ('y') ")
            if should_roll.lower() != 'y':
                break

            # Checking the dice roll result..
            value = roll()
            if value == 1:                  # Ending the turn if its one..
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:                           # Increasing the score if its not one..
                current_score += value
                print("You rolled a", value)

            print(f"Your current turn score is {current_score}")
            if players_score[player_idx] + current_score >= max_score:         # Making sure if max score is reached game ends..
                break

        players_score[player_idx] += current_score
        print(f"Your final score is : {players_score[player_idx]}")
        if players_score[player_idx] > max_score:
            break

# Announcing the winner..
winner_score = max(players_score)
winning_idx = players_score.index(winner_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", winner_score)      