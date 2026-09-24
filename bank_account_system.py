class bank:
    def __init__(self,acc,balance):
        self.account_no=acc
        self.balance=balance

    def credit(self,amount):
        self.amount=amount
        self.balance +=amount
        print(f"amount of rs.{amount} is credited\nremaining balace is rs.{self.balance}")
    
    def debit(self,amount):
        self.amount=amount
        self.balance -=amount
        print(f"amount of rs.{amount} is debited\nremaining balace is rs.{self.balance}")

    def get_balance(self):
        return self.balance 

acc1=bank(1234556,1000)
acc1.credit(9500)
acc1.debit(500)