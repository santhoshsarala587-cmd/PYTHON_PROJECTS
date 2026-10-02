print("====================================")
print(" BASIC ATM CALCULATOR")
print(" (Minimum Balance: ₹1000)")
print("====================================")

name = input("Enter your name: ")
balance = 5000
minimum_balance = 1000
choice = 0

print("\nWelcome", name)

while choice != 4:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nYour current balance is: ₹", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Amount Deposited Successfully")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid Amount")

        elif balance - amount < minimum_balance:
            print("Withdrawal Denied!")
            print("Minimum balance of ₹", minimum_balance, "must be maintained")
            print("Current Balance: ₹", balance)

        else:
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining Balance: ₹", balance)

    elif choice == 4:
        print("\nThank you for using ATM")
        print("Have a nice day ")

    else:
        print("Invalid Choice. Try Again")
