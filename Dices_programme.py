# Dices programme in python

import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")   Unicodes for the symbols below
# ● ┌ ─ ┐ │ └ ┘
"┌─────────────┐"
"│             │"
"│             │"
"│             │"
"│             │"
"│             │"
"│             │"
"└─────────────┘"
dice_art = {1:("┌─────────────┐",
               "│             │",
               "│             │",
               "│      ●      │",
               "│             │",
               "│             │",
               "└─────────────┘"),
            2:("┌─────────────┐",
               "│  ●          │",
               "│             │",
               "│             │",
               "│             │",
               "│          ●  │",
               "└─────────────┘"),
            3:("┌─────────────┐",
               "│  ●          │",
               "│             │",
               "│      ●      │",
               "│             │",
               "│           ● │",
               "└─────────────┘"),
            4:("┌─────────────┐",
               "│   ●       ● │",
               "│             │",
               "│             │",
               "│             │",
               "│   ●       ● │",
               "└─────────────┘"),
            5:("┌─────────────┐",
               "│  ●        ● │",
               "│             │",
               "│       ●     │",
               "│             │",
               "│  ●        ● │",
               "└─────────────┘"),
            6:("┌─────────────┐",
               "│   ●       ● │",
               "│             │",
               "│   ●       ● │",
               "│             │",
               "│   ●       ● │",
               "└─────────────┘")}

dices_num = int(input("Enter the Number of Dices: "))
dic = []
total = 0
for dice in range(dices_num):
    dic.append(random.randint(1,6))
print(dic)

''''for i in range(dices_num):
    for dice in dice_art.get(dic[i]):
        print(dice)
'''
#code to print all the dices in single line


for i in range(7):
    for x in dic:
        print(dice_art.get(x)[i], end = " ")

    print()
for i in dic:
    total += i
print(f"The total of dices is {total}")
