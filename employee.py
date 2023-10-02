"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, commissionPay = 0, commissionNum = 0, recievesBonus = False):
        self.name = name
        self.commissionPay = commissionPay
        self.commissionNum = commissionNum
        self.recievesBonus = recievesBonus

    def commissionBonus(self):
        return self.commissionPay * self.commissionNum

    @abstractmethod
    def get_pay(self):
        pass

    def __str__(self):
        return self.name

 #Class for employees with monthly contract   
class MonthlyEmployee(Employee):
    def __init__(self, name,monthPay, commissionPay=0, commissionNum=0, recievesBonus=False):
        super().__init__(name, commissionPay, commissionNum, recievesBonus)
        self.monthPay = monthPay

    def get_pay(self):
        return self.monthPay + super().commissionBonus()
    
    def __str__(self):
      if self.recievesBonus == False and self.commissionPay == 0:
          return f"{self.name} works on a monthly salary of {self.monthPay}. Their total pay is {self.get_pay()}."
      elif self.recievesBonus == False and self.commissionPay > 0:
          return f"{self.name} works on a monthly salary of {self.monthPay} and receives a commission for {self.commissionNum} contract(s) at {self.commissionPay}/contract. Their total pay is {self.get_pay()}."
      else:
          return f"{self.name} works on a monthly salary of {self.monthPay} and receives a bonus commission of {self.commissionPay}. Their total pay is {self.get_pay()}."

#Class for employees with hourly contract
class HourlyEmployee(Employee):
    def __init__(self, name, hourPay, hourNum, commissionPay=0, commissionNum=0, recievesBonus=False):
        super().__init__(name, commissionPay, commissionNum, recievesBonus)
        self.hourPay = hourPay
        self.hourNum = hourNum

    def get_pay(self):
        return (self.hourPay * self.hourNum) + super().commissionBonus()
    
    def __str__(self):
        if self.recievesBonus == False and self.commissionPay == 0:
          return f"{self.name} works on a contract of {self.hourNum} hours at {self.hourPay}/hour. Their total pay is {self.get_pay()}."
        elif self.recievesBonus == False and self.commissionPay > 0:
          return f"{self.name} works on a contract of {self.hourNum} hours at {self.hourPay}/hour and receives a commission for {self.commissionNum} contract(s) at {self.commissionPay}/contract. Their total pay is {self.get_pay()}."
        else:
          return f"{self.name} works on a contract of {self.hourNum} hours at {self.hourPay}/hour and receives a bonus commission of {self.commissionPay}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, 1500, 1, True)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 30, 120, 600, 1, True)

print(billie)
print(charlie)
print(renee)
print(jan)
print(robbie)
print(ariel)