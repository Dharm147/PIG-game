# Dice Rolling Game
This is a simple dice rolling game implemented in Python where players take turns rolling a six-sided die to accumulate points. The game continues until one player reaches or exceeds a predefined maximum score.

### How the game works:
1. **Objective**: The objective of the game is to reach or exceed a maximum score before the other players.
2. **Number of Players**: The game can be played by 1 to 4 players.
3. **Dice Rolling**: Players take turns rolling a six-sided die.
4. **Scoring**:
+ If a player rolls a 1, their turn ends, and they lose all points accumulated during that turn.
+ If a player rolls any other number (2-6), the number rolled is added to their turn score.
5. **Winning Condition**: The game continues until one player reaches or exceeds a predetermined maximum score. The player with the highest score at that point is declared the winner.
### How the Code Works (Pseudo-Code):
1. **Initialization**:

+ The game starts by prompting the user to input the number of players (1-4).
+ A maximum score is predefined (in this case, 50).
+ An empty scoreboard is initialized to keep track of each player's score.

2. **Game Loop**:

+ The game loop continues until one player reaches or exceeds the maximum score.
+ Inside the game loop, each player takes their turn in order.

3. **Player Turn**:

+ For each player's turn:

    * The player's current score is displayed.
    * The player is prompted to roll the dice.
    * If the player chooses to roll ('y'), a random number between 1 and 6 is generated.
    * If the roll is a 1, the player's turn ends, and their current score resets to 0.
    * If the roll is any other number (2-6), the number rolled is added to the player's current turn score.
    * The player can choose to roll again or end their turn.
    * If the player's total score (including the current turn score) reaches or exceeds the maximum score, the game ends.
    * The player's final score is displayed.

4. **Announcing the Winner**:

+ Once a player reaches or exceeds the maximum score, the game loop ends.
+ The player with the highest score is declared the winner, and their score is displayed.
