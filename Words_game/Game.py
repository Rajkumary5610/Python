from words import word
import random

human_art = {0: ("     ",
                 "     ",
                 "     "),
             1: ("  O  ",
                 "     ",
                 "     "),
             2: ("  O  ",
                 "  |  ",
                 "     "),
             3: ("  O  ",
                 " /|  ",
                 "     "),
             4: ("  O  ",
                 " /|\ ",
                 "     "),
             5: ("  O   ",
                 " /|\  ",
                 " /    "),
             6: ("  O   ",
                 " /|\  ",
                 " / \  ")}


def display_man(wrong_guess):
    for man in human_art[wrong_guess]:
        print(man)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(word)
    hint = ["_"] * len(answer)
    is_running = True


    wrong_guess = 0
    print(word)
    while is_running:
        display_man(wrong_guess)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print("You win")
            is_running = False
        elif wrong_guess >= len(human_art) - 1:
            display_man(wrong_guess)
            display_answer(answer)
            print("You Loss")
            is_running = False


if __name__ == "__main__":
    main()




