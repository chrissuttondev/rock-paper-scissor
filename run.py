import random
# Rock, paper, scissors game vs computer
# Rock

cc_score = []
uc_score = []


while True:
    choices = ["r", "p", "s"]
    cc = random.choice(choices)
    # while loop checks if input. Loops is broken when input is r, s or p.
    while True:
        uci = input("make your guess by typing 'r', 'p' or 's':")
        uc = uci.lower()
        if uci not in choices:
            print("Please try again. Enter 'r', 'p' or 's'")
        else:
            break
    # if / elif statement to compare uc and cc

    if uc == cc:
        print("Draw")
    elif uc == "r" and cc == "p":
        print("Computer wins")
        cc_score.append("w")
    elif uc == "r" and cc == "s":
        print("You win")
        uc_score.append("w")
    elif uc == "p" and cc == "r":
        print("You win")
        uc_score.append("w")
    elif uc == "p" and cc == "s":
        print("Computer wins")
        cc_score.append("w")
    elif uc == "s" and cc == "r":
        print("Computer wins")
        cc_score.append("w")
    elif uc == "s" and cc == "p":
        print("You win")
        uc_score.append("w")
    print(f"Computer chose {cc}")
    print(f"You chose {uc}")
    print(f"Computer score {cc_score}")
    print(f"Your score {uc_score}")
    if  len(cc_score) == 3:   
        print("Unlucky, Computer wins the game")
        break
    elif len(uc_score) == 3: 
        print("Well done, you win the game")
        break
        