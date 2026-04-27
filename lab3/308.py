class Account:
    def __init__(self,balance, withdrawal):
        self.balance=balance
        self.withdrawal=withdrawal
    def newb(self):
        if self.balance>=self.withdrawal:
            return(self.balance-self.withdrawal)
        else:
            return("Insufficient Funds")
b,w=map(int,input().split())
newbalance=Account(b,w)
print(newbalance.newb())

