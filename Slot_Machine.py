# Slot Machine promgramme in python

import random
def spin_row():
    symbols = ["🍒",  "🍎",  "💖", "🔔", "⭐"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    print(" | ".join(row))
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")



def payout_amount(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍎":
            return bet * 6
        elif row[0] == "💖":
            return bet * 9
        elif row[0] == "🔔":
            return bet * 12
        elif row[0] == "⭐":
            return bet * 15
    return 0



def main():
    balance = 100
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Slot Machine programme in python")
    print("Symbols: 🍒 🍎 💖 🔔 ⭐")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    while balance > 0:
        print("**********************************")
        print(f"The balance amount is {balance}")
        print("**********************************")


        bet = input("Place the bet to play the slot machine: ")

        if not bet.isdigit():
            print("😁😁😁😁😁😁😁")
            print("Invalid Input")
            print("😁😁😁😁😁😁😁")
            continue
        bet = int(bet)

        if bet <= 0:
            print("///////////////////////////")
            print("bet must be greater than 0")
            print("///////////////////////////")
            continue

        if bet > balance:
            print("--------------------")
            print("Insufficient funds")
            print("--------------------")
            continue
        balance -= bet
        row = spin_row()

        print_row(row)
        payout = payout_amount(row, bet)
        balance += payout
        if payout > 0:
            print("💵💵💵💵💵💵💵💵💵💵💵")
            print(f"You have won ${payout}")
            print("💵💵💵💵💵💵💵💵💵💵💵")

        else:
            print("👎👎👎👎👎👎👎👎👎👎👎👎👎👎")
            print("You have lost the bet sorry!")
            print("👎👎👎👎👎👎👎👎👎👎👎👎👎👎")
            print("😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊")
        play_again = input("Do you want to play again (y/n)").upper()
        print("😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊")
        if play_again != "Y":
            print("🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘")
            print(f"Game over your balance is ${balance} ")
            print("🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘🤘")
            break






if __name__ == "__main__":
    main()













