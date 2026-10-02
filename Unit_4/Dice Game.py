import random
import time


dice_faces = {
    1: ("-----",
        "|   |",
        "| o |",
        "|   |",
        "-----"),
    2: ("-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----"),
    3: ("-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----"),
    4: ("-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----"),
    5: ("-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----"),
    6: ("-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----")
}

def roll_animation():
    print("\nRolling", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print()

def show_dice(n):
    for line in dice_faces[n]:
        print(line)

def play_round(round_no):
    print(f"\n🎯 ROUND {round_no}")

    input("Press ENTER to roll your dice 🎲")
    roll_animation()
    player = random.randint(1, 6)

    print("\nYour Dice:")
    show_dice(player)

    roll_animation()
    computer = random.randint(1, 6)

    print("\nComputer Dice:")
    show_dice(computer)

    return player, computer

def game():
    print("🎲 DICE GAME - BEST OF 5 🎲")
    print("First to win 3 rounds wins the game!\n")

    player_score = 0
    comp_score = 0
    round_no = 1

    while player_score < 3 and comp_score < 3:
        player, comp = play_round(round_no)

        if player > comp:
            print("\n🔥 You win this round!")
            player_score += 1
        elif comp > player:
            print("\n💻 Computer wins this round!")
            comp_score += 1
        else:
            print("\n🤝 It's a tie! (No points)")

        print(f"\nScore -> You: {player_score} | Computer: {comp_score}")
        round_no += 1

    print("\n🏁 FINAL RESULT 🏁")
    if player_score == 3:
        print("🏆 YOU WON THE MATCH!")
    else:
        print("💻 COMPUTER WON THE MATCH!")

    # Replay option
    choice = input("\nPlay again? (y/n): ").lower()
    if choice == 'y':
        game()
    else:
        print("Thanks for playing 🎲")


if __name__ == "__main__":
    game()