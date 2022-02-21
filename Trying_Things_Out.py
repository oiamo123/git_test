
def game():
    secret_word = "Giraffe"
    guess = ""
    count = 0
    max_attempts = 3
    game = True
    print("Guess the animal: This animal has a long neck")
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
    play_again = input("Would you like to play?: ")
    if play_again == "yes":
        game()
    else:
        print("Good-bye!")

main()