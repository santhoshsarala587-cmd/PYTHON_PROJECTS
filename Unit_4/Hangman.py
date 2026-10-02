import random

class HangmanGame:
    def __init__(self):
        self.words = {
            "python": "Programming language",
            "oxygen": "Essential gas for life",
            "galaxy": "Collection of stars",
            "pyramid": "Ancient structure",
            "laptop": "Portable computer",
            "algorithm": "Step-by-step solution"
        }
        self.word, self.hint = random.choice(list(self.words.items()))
        self.guessed = set()
        self.lives = 6

    def display_word(self):
        return " ".join([ch if ch in self.guessed else "_" for ch in self.word])

    def play(self):
        print("\n🎮 Welcome to Hangman Game!")
        print(f"💡 Hint: {self.hint}")

        while self.lives > 0:
            print("\nWord:", self.display_word())
            print("Used Letters:", " ".join(sorted(self.guessed)))
            print(f"Lives Left: {self.lives}")

            guess = input("Enter a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("❌ Enter a single valid letter.")
                continue

            if guess in self.guessed:
                print("⚠️ Already guessed!")
                continue

            self.guessed.add(guess)

            if guess in self.word:
                print("✅ Good guess!")
            else:
                print("❌ Wrong guess!")
                self.lives -= 1

            if all(ch in self.guessed for ch in self.word):
                print("\n🎉 You WON! The word was:", self.word)
                return

        print("\n💀 You LOST! The word was:", self.word)



def main():
    while True:
        game = HangmanGame()
        game.play()

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()