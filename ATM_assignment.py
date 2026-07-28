# ATM Program
balance = 0.0   # ya jo bhi starting balance o, jaise 1000
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")

        elif amount > balance:
            print("Insufficient balance. Transaction rejected.")

        else:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance is Rs.", balance)

    elif choice == "3":
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")

        else:
            balance += amount
            print("Deposit successful.")
            print("Updated balance is Rs.", balance)

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid option. Please try again.")