import random

print("Welcome to Rock Paper Scissors")
print("------------------------------")

def winner(player, computer):
    if player == computer:
        print("It's a tie, Play Again!")
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win :)")
        return "player"
    else:
        print("You lose :(")
        return "computer"

def play_game():
    cpuscore = 0
    playerscore = 0
    tiescore = 0
    hands = ["rock", "paper", "scissors"]

    while True:
        while True:
            player = input("Enter your choice: rock, paper, scissors: ").lower()
            if player in hands:
                break
            else:
                print("Invalid Input. Try Again")

        computer = random.choice(hands)

        print("Your Choice : ", player)
        print("Computer's Choice : ", computer)
        result = winner(player, computer)
        if result == "player":
            playerscore += 1
        elif result == "computer":
            cpuscore += 1
        else:
            tiescore += 1
        
        print("Your Score : ", playerscore)
        print("Computer's Score : ", cpuscore)
        print("Tie's : ", tiescore)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again!= "yes":
            break

    print("Thank You For Playing, The Game Is Over Now!")

play_game()