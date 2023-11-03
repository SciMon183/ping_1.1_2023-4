#  dziala na 80%

def play_hangman(word):
    word = list(word)
    guessed_word = ["." for _ in word]
    chances = 7

    print("".join(guessed_word), chances)

    while chances > 0:
        letter = input().strip().upper()
        
        if letter in guessed_word:
            print("".join(guessed_word), chances)
        elif letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
            if "".join(guessed_word) == "".join(word):
                print("".join(guessed_word))
                print("WYGRANA")
                return
            else:
                print("".join(guessed_word), chances)
        else:
            chances -= 1
            if chances == 0:
                print("".join(word))
                print("PRZEGRANA")
            else:
                print("".join(guessed_word), chances)

if __name__ == "__main__":
    word = input().strip()
    play_hangman(word)