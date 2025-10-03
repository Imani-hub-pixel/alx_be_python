class BankAccount:
    def __init__(self,account_balance):
        self.account_balance=account_balance

    def deposit(self,amount):
            if amount >0:
                self.account_balance +=amount
                return True
            return False
    
    def withdraw(self,amount):
        if amount>0 and amount<=self.account_balance:
             self.account_balance-=amount
             return True
        return False
    def display_balance(self):
        return self.account_balance
    

            


