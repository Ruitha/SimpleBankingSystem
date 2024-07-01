# Python Banking Program

def show_balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("*******************")
        print("That's not a valid amount")
        print("*******************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("*******************")
        print("Insufficient funds")
        print("*******************")

    elif amount < 0:
        print("*******************")
        print("Amount must be more than 0")
        print("*******************")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("********************")
        print("Banking Program")
        print("********************")

        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*******************")

        choice = input("Enter you choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*******************")
            print("That is not a valid choice")
            print("*******************")

    print("Thank you! Have a nice day.")

if __name__ == '__main__':
    main()