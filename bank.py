class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []  
        self.undo_stack = []    # stack for undo
        self.redo_stack = []    # stack for redo

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Invalid deposit amount.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        self.undo_stack.append(('deposit', amount))
        self.redo_stack.clear()
        print(f"✅ ₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew ₹{amount}")
        self.undo_stack.append(('withdraw', amount))
        self.redo_stack.clear()
        print(f"✅ ₹{amount} withdrawn successfully.")

    def show_balance(self):
        print(f"\n💰 Current Balance: ₹{self.balance}\n")

    def show_transactions(self):
        if not self.transactions:
            print("📂 No transactions yet.")
        else:
            print("\n📜 Transaction History:")
            for i, t in enumerate(self.transactions, 1):
                print(f"{i}. {t}")

    def undo(self):
        if not self.undo_stack:
            print("⚠️ Nothing to undo.")
            return
        action, amount = self.undo_stack.pop()
        if action == 'deposit':
            self.balance -= amount
            self.transactions.append(f"Undo deposit of ₹{amount}")
            self.redo_stack.append(('deposit', amount))
        elif action == 'withdraw':
            self.balance += amount
            self.transactions.append(f"Undo withdrawal of ₹{amount}")
            self.redo_stack.append(('withdraw', amount))
        print(f"↩️ Undid last action: {action} ₹{amount}")

    def redo(self):
        if not self.redo_stack:
            print("⚠️ Nothing to redo.")
            return
        action, amount = self.redo_stack.pop()
        if action == 'deposit':
            self.deposit(amount)
        elif action == 'withdraw':
            self.withdraw(amount)
        print(f"🔁 Redid last action: {action} ₹{amount}")

# ------------- MAIN PROGRAM -----------------
def main():
    print("=====================================")
    print("🏦 Welcome to the Bank System (Stack)")
    print("=====================================")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n--------- MENU ---------")
        print("1️⃣ Deposit")
        print("2️⃣ Withdraw")
        print("3️⃣ Show Balance")
        print("4️⃣ Show Transactions")
        print("5️⃣ Undo Last Action")
        print("6️⃣ Redo Last Action")
        print("7️⃣ Exit")
        print("-------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            amt = float(input("Enter deposit amount: ₹"))
            account.deposit(amt)

        elif choice == '2':
            amt = float(input("Enter withdrawal amount: ₹"))
            account.withdraw(amt)

        elif choice == '3':
            account.show_balance()

        elif choice == '4':
            account.show_transactions()

        elif choice == '5':
            account.undo()

        elif choice == '6':
            account.redo()

        elif choice == '7':
            print("👋 Thank you for using Bank System!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":

    main()
