class Account:

    def __init__(self, title, number, balance):
        self.title = title
        self.number = number
        self._balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
            self.history.append("Deposited: " + str(amount))
            print("Amount deposited.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self._balance:
            print("Not enough balance.")
        else:
            self._balance = self._balance - amount
            self.history.append("Withdrawn: " + str(amount))
            print("Amount withdrawn.")

    def get_balance(self):
        return self._balance

    def show_info(self):
        print("Title:", self.title)
        print("Account Number:", self.number)
        print("Account Type: Account")
        print("Balance:", self._balance)


class SavingsAccount(Account):

    def __init__(self, title, number, balance):
        super().__init__(title, number, balance)


    def show_info(self):
        print("Title:", self.title)
        print("Account Number:", self.number)
        print("Account Type: Savings Account")
        print("Balance:", self._balance)


class CurrentAccount(Account):

    def __init__(self, title, number, balance):
        super().__init__(title, number, balance)
        self.withdrawal_limit = 50000

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.withdrawal_limit:
            print("You can withdraw maximum 50000.")

        elif amount > self._balance:
            print("Not enough balance.")

        else:
            self._balance = self._balance - amount
            self.history.append("Withdrawn: " + str(amount))
            print("Amount withdrawn.")

    def show_info(self):
        print("Title:", self.title)
        print("Account Number:", self.number)
        print("Account Type: Current Account")
        print("Balance:", self._balance)


class Bank:

    def __init__(self):
        self.accounts = []
        self.number = 1000000000

    def find_account(self, number):

        for account in self.accounts:

            if account.number == number:
                return account

        return None

    def open_account(self):

        print("\n--- Open Account ---")

        title = input("Enter account title: ")

        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Enter choice: ")

        balance = input("Enter initial balance: ")

        if balance == "":
            balance = 0
        else:
            balance = float(balance)

        number = str(self.number)
        self.number = self.number + 1

        if choice == "1":

            account = SavingsAccount(title, number, balance)

        elif choice == "2":

            account = CurrentAccount(title, number, balance)

        else:
            print("Wrong choice.")
            return

        self.accounts.append(account)

        print("Account created.")
        print("Your account number is:", number)

    def delete_account(self):

        number = input("Enter account number: ")

        account = self.find_account(number)

        if account == None:
            print("Account not found.")

        elif account.get_balance() > 0:
            print("Account cannot be deleted.")
            print("First make balance zero.")

        else:
            self.accounts.remove(account)
            print("Account deleted.")

    def withdraw_money(self):

        number = input("Enter account number: ")

        account = self.find_account(number)

        if account == None:
            print("Account not found.")
            return

        amount = float(input("Enter amount: "))

        account.withdraw(amount)

    def deposit_money(self):

        number = input("Enter account number: ")

        account = self.find_account(number)

        if account == None:
            print("Account not found.")
            return

        amount = float(input("Enter amount: "))

        account.deposit(amount)

    def display_accounts(self):

        if len(self.accounts) == 0:
            print("No accounts.")

        else:

            print("\n--- All Accounts ---")

            for account in self.accounts:
                print("-------------------")
                account.show_info()

    def transaction_history(self):

        number = input("Enter account number: ")

        account = self.find_account(number)

        if account == None:
            print("Account not found.")
            return

        print("\nTransaction History:")

        if len(account.history) == 0:
            print("No transactions.")

        else:

            for x in account.history:
                print(x)

    def total_withdrawn(self):

        number = input("Enter account number: ")

        account = self.find_account(number)

        if account == None:
            print("Account not found.")
            return

        total = 0

        for x in account.history:

            if "Withdrawn:" in x:
                amount = float(x.split(":")[1])
                total = total + amount

        print("Total Withdrawn:", total)

    def total_deposited(self):

        number = input("Enter account number: ")

        account = self.find_account(number)

        if account == None:
            print("Account not found.")
            return

        total = 0

        for x in account.history:

            if "Deposited:" in x:
                amount = float(x.split(":")[1])
                total = total + amount

        print("Total Deposited:", total)


# Main Program

bank = Bank()

while True:

    print("\n========================")
    print("   BANK MANAGEMENT")
    print("========================")

    print("1. Open an Account")
    print("2. Delete an Account")
    print("3. Withdraw from an Account")
    print("4. Deposit into an Account")
    print("5. Display List of Accounts")
    print("6. View Transaction History")
    print("7. View Total Withdrawn")
    print("8. View Total Deposited")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.open_account()

    elif choice == "2":
        bank.delete_account()

    elif choice == "3":
        bank.withdraw_money()

    elif choice == "4":
        bank.deposit_money()

    elif choice == "5":
        bank.display_accounts()

    elif choice == "6":
        bank.transaction_history()

    elif choice == "7":
        bank.total_withdrawn()

    elif choice == "8":
        bank.total_deposited()

    elif choice == "9":
        print("Program ended.")
        break

    else:
        print("Wrong choice.")