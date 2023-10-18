import random
# Rock, paper, scissors game vs computer
# Rock

while True:
    choices = ["r", "p", "s"]
    cc = "r"
    cc_score = []
    target_length = 3
    uc_score = []
    target_length = 3

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
