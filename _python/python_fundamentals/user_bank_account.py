class User:
    def __init__(self,name,email,int_rate,balance):
        self.name=name
        self.email=email
        self.account = BankAccount(int_rate=.01,balance=0)
        
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        
    def display_user_balance(self):
        print(self.name ,self.account)
    
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        print(self.account.balance)
       
        
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        
class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.balance =balance
        self.int_rate=int_rate
        
    def deposit(self, amount):
        self.balance+=amount
        return self
       

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance-=amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return self       

    
    def display_account_info(self):
        print( f" balance {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance*=self.int_rate
        return self         
    
user1=User("lolo","@gmail.com",.02,5000)
user1.make_deposit(500)
