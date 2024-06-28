class Bank:
    def __init__ (self, balance = 0.00):
        self.balance = balance

    def transition_log( self, transition_string):
        with open("bank_transition_log.txt", "a") as file:
            file.write(f"{transition_string} \t\t\t\t\t Balance: {self.balance}\n")

    def deposit(self, amount):
        try:
            amount = float(amount)
       
        except:
            print("Invalid input. Please try again")
        if amount:
            self.balance = self.balance + amount
            self.transition_log(f"deposited {amount}")
        

    def withdraw(self, amount):
        try:
            amount = float(amount)
            
        except:
            print("Invalid input. Please try again")
        
        if amount:
            self.balance = self.balance - amount
            self.transition_log(f"Withdrew {amount}")

account = Bank()

while True:
    try:
        action = input("Enter the action you want to perform: ")
        action.lower()
        
    except KeyboardInterrupt:
        print("\nThank you, visit again!")
        break

    if action == "deposit":
        amount = input("Enter the amount you want to deposit: ")
        account.deposit(amount)
        
    
    elif action == "withdraw":
        amount = input("Enter the amount you want to withdraw: ")
        account.withdraw(amount)
    

    
    else:
        print("Invalid input.(Please enter: withdraw/deposit)")

    print(f"current balance:{account.balance}")

