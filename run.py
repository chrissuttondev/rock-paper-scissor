import random
# Rock, paper, scissors game vs computer
# Rock

choices = ["r", "p", "s"]
cc = "r"

while True:
    # while loop checks if input. Loops is broken when input is r, s or p.
    while True:
        uci = input("make your guess by typing 'r', 'p' or 's':")
        uc = uci.lower()
        if uci not in choices:
            print("Please try again. Enter 'r', 'p' or 's'")
        else:
            break
    print(uc)
    print(cc)

    # if / elif statement to compare uc and cc

    if uc == cc:
        print("Draw")
    elif uc == "r" and cc == "p":
        print("Computer wins")
    elif uc == "r" and cc == "s":
        print("You win")
    elif uc == "p" and cc == "r":
        print("You win")
    elif uc == "p" and cc == "s":
        print("Computer wins")
    elif uc == "s" and cc == "r":
        print("Computer wins")
    elif uc == "s" and cc == "p":
        print("You win")
