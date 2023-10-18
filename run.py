import random
# Rock, paper, scissors game vs computer

choices = ["r", "p", "s"]
cc = "r"
# Input validation need. If uci not r,p or s

while True:
    uci = input("make your guess by typing 'r', 'p' or 's':")
    uc = uci.lower()
    if uci not in choices:
        print("Please try again. Enter 'r', 'p' or 's'")
    else:
        break

print(uc)
