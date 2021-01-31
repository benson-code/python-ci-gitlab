import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
# 1. 之後存款1000元, 確認帳戶總金額為1100元
# 2. 接續提款500元, 確認帳戶總金額為600元
# 3. 之後提款700元, 會出現 RuntimeError
#
##########################################################################################
     def __init__(self, number, name):
        self.number = number
        self.name = name
        self.blance = 0

     def deposit(self, amount):  #存款動作: amount為存入金額
         if amount <=0:
            raise ValueError('must be postive')
         self.blance += amount

     def withdraw(self, amount): #取款動作: amount為存入金額
         if amount <= self.blance:
             self.blance -= amount
         else:
             raise RuntimeError('RuntimeError')

acct1 = Account('123-4567', 'Test User') #開一個帳戶
acct1.deposit(100) #開戶先存100元
acct1.deposit(1000) #存款1000元
acct1.withdraw(500) #提款500元
acct1.withdraw(700) #提款700元
Print(acct1.blance) #餘額














