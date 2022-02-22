import random

def game():
    words = ['Giraffe', 'Panda', 'Lion', 'Snake', 'Penguin',]
    secret_word = (random.choice(words))
    if secret_word == "Giraffe":
        hint = ("This animal has a long neck")
    if secret_word == "Panda":
        hint = ("This animal is black and white is popular in China")
    if secret_word == "Lion":
        hint = ("Typically reffered to as king of the jungle")
    if secret_word == "Snake":
        hint = ("This animal is long and has no legs")
    if secret_word == 'Penguin':
        hint = ("This animal lives in Antartica")
    guess = ""
    count = 0
    max_attempts = 3
    game = True
    print(hint)
    while guess != secret_word and game:
        if count < max_attempts:
            guess = input("Enter a word: ")
            count += 1
        else:
            game = False
            print ("You lose!")
            main()
        if guess == secret_word:
            print("You win!")
            main()
def main():
    try:
        play_again = input("Would you like to play? Enter 'y' to play or 'n' to quit: ")
        if play_again == "y":
            game()
        if play_again == "n":
            print("Good-bye!")
    except:
        print("Incorrect response")
        play_again

main()