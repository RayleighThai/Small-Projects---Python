import random # random word of the day

# Initialize the game by first generate keyword of the day
def wotd():
    file = open("words.txt").read().splitlines()
    secret = random.choice(file)
    return secret

# Instructions at the start of the game
def gameinstruction():
    print("""\n\nWelcome to wordle clone - Made by Ray Thai 
          \nYou have 6 chances to guess the special word of the day! The length for this special word is only 5 characters in the US dictionary.
          Once you entered your guess, Each letter will have corresponding of either \u2713, ~, \u2717.
          \u2713 - means you have correct letter in the right spot. Congrats! 
          ~ - means you have correct letter BUT not in correct spot.
          \u2717 - means you do not have correct letter at this spot. 
          """)

# Check for game result and attempt.
def checkgame(kw, attempt, result):
    while attempt > 0:
        guess = input("\nEnter your guess: ")
        if len(guess) == 5:
            if guess == kw:
                result = True
                break
            else:
                attempt = attempt - 1
                print(f"You have {attempt} attempt(s) left.\n")
                for char, word in zip(kw, guess):
                    # print(char + " - " + word)
                    if word in kw and word in char:
                        print(word + " \u2713")
                    elif word in kw:
                        print(word + " ~")
                    else:
                        print(word + " \u2717")
        else:
            print("You entered ", guess, "with the length not equal 5. Try again")
    return result, attempt

def end():
    endgame = input("Would you like to play again? Y / n \t")
    if endgame.lower() == "y":
        main()
    else:
        print("See you later!\n")


def main():
    gameinstruction()
    attempt = 6
    kw = wotd()
    result = False
    result, attempt = checkgame(kw, attempt, result)
    if not result:
        print("You Lose. Word of the day is ", kw)
    else:
        print(f"You got the word of the day with {attempt} attempt(s) left! It is {kw}. Congratulations!")
    end()
        
if __name__ == "__main__":
    main()