import random
import time

print("Welcome to Rock Paper Scissors!")

while True:
    game_computer = ["rock", "paper", "scissors"]

    computer = random.choice(game_computer)
    player = None

    while player not in game_computer:
        game = str(input("Type rock, paper or scissors to play.")).lower().strip()

        if game == "rock" and computer == "rock":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("This is a draw!")

        elif game == "rock" and computer == "paper":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("Computer wins!")

        elif game == "rock" and computer == "scissors":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("You win!")

        elif game == "paper" and computer == "paper":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("This is a draw!")

        elif game == "paper" and computer == "rock":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("You win!")

        elif game == "paper" and computer == "scissors":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("Computer wins!")

        elif game == "scissors" and computer == "scissors":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("This is a draw!")

        elif game == "scissors" and computer == "rock":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("Computer wins!")
        elif game == "scissors" and computer == "paper":
            print(f"Your choice has been {game}")
            time.sleep(1.5)
            print(f"Computer choice has been {computer}")
            time.sleep(1.5)
            print("You win!")
