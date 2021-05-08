class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account_balance = 0
        
    def make_withdrawal(self, amount):
        self.account_balance-=amount
        
    def display_user_balance(self):
        print(self.name ,self.account_balance)
    
    def make_deposit(self, amount):	
    	self.account_balance += amount    
        
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        
             
        
        
user1=User("ameera","@gmail.com")

user1.make_deposit(1000)
user1.display_user_balance()

user1.make_deposit(1000)
user1.make_deposit(1000)
user1.make_withdrawal(500)
user1.display_user_balance()


user2=User("hanin","hanin@gmail.com")
user2.make_deposit(2000)
user2.make_deposit(4000)
user2.make_withdrawal(500)
user2.make_withdrawal(500)
user2.display_user_balance()

user3=User("yasmin","yasmin@gmail.com")
user3.make_deposit(2000)
user3.make_withdrawal(500)
user3.make_withdrawal(500)
user3.make_withdrawal(500)
user3.display_user_balance() 


user1.transfer_money( user3, 500) 

user1.display_user_balance()
user3.display_user_balance()     