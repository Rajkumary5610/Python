# Banking programme using python

def show_balance(balance):
    print("#####################################################")
    print(f"     Your account balance is ${balance:.2f}         ")
    print("#####################################################")

def deposit():
    print("######################################################")
    amount = float(input("Enter the amount to deposit: "))
    print("######################################################")
    if amount < 0:
        print("###############################")
        print("        Invalid amount         ")
        print("###############################")
        return 0
    else:
        return amount

def withdraw(balance):
    print("######################################################")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("######################################################")
    if amount > balance:
        print("######################################################")
        print("                 Insufficient funds                   ")
        print("######################################################")
    elif amount < 0:
        print("######################################################")
        print("        Amount can not be less than zero              ")
        print("######################################################")

    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("#############################")
        print("     Banking Programme       ")
        print("#############################")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("#############################")


        choice = input("Enter the choice between (1-4): ")
        print("#############################")


        '''  if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False

        else:
            print("#############################")
            print("       Invalid choice        ")
            print("#############################")
            
'''
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False

            case _:
                print("#############################")
                print("       Invalid choice        ")
                print("#############################")


    print("Thank you for using our services")
    print("Have a good day")


if __name__ == "__main__":
    main()






