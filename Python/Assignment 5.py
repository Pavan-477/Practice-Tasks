#*****************************OOPS ASSIGNMENT(5)*************************

#------------------------------------CHALLENGE-1-------------------------
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def sqSum(self):
        sum_of_sqs= (self.x**2) + (self.y**2) + (self.z**2)
        return(sum_of_sqs)

nums=input("Enter three numbers separated by comma to get their sum of squares : ").split(",")
p=Point(int(nums[0]),int(nums[1]),int(nums[2]))
print(p.sqSum())

#------------------------------------CHALLENGE-2-------------------------
class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum=self.num1+self.num2
        print("Sum of the given numbers is :",sum)
    def subtract(self):
        diff=self.num2-self.num1
        print("The subtraction of 1st number from 2nd number is :",diff)
    def multiply(self):
        prod=self.num1*self.num2
        print("Product of the given numbers is :",prod)
    def divide(self):
        div=self.num2/self.num1
        print("Division of the 2nd number by 1st number is :",div)

print("\n**************** WELCOME TO CALCULATOR *******************\nPress 1 for taking integer numbers as input\nPress 2 for floating point numbers as input\n")
choice=int(input())
if choice==1:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))

elif choice==2:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

else:
    print("Run the code again and enter among the given options ")
    quit()
obj=Calculator(num1,num2)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

#------------------------------------CHALLENGE-3-------------------------
class Student:

    """Not using constructor(initializer) for initializing the properties as its mentioned-
      Do not use initializers to initialize the properties. Use the set methods to do so."""

    __Name=None         
    __RollNumber=None

    def setName(self,Name):
        self.__Name=Name
    def getName(self):
        return self.__Name
    def setRollNumber(self,RollNumber):
        self.__RollNumber=RollNumber
    def getRollNumber(self):
        return self.__RollNumber

nme=input("Enter student's name : ")
rlno=int(input("Enter roll number : "))

s=Student()
s.setName(nme)
print(s.getName())
s.setRollNumber(rlno)
print(s.getRollNumber())

#------------------------------------CHALLENGE-4-------------------------
class Account:

    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance
        

class SavingsAccount(Account):

    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate=interestRate
        print("Welcome ",self.title)
        print("Your account balance is ",self.Balance)
        print("Your current interest rate is ",self.interestRate)


name=input("Enter your name : ")
bal=int(input("Enter your balance : "))
intrst_rate=float(input("Enter interest rate : "))
user=SavingsAccount(name,bal,intrst_rate)

#------------------------------------CHALLENGE-5-------------------------
class Account:

    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance

  
    def deposit(self,amount):
        self.amount=amount
        self.Balance+=amount
          
   
    def withdrawal(self,amount):
        if amount<=self.Balance:
            self.amount=amount
            self.Balance-=amount
        else:
            print("Insufficient funds to process")
         

    def getBalance(self):
         print("Current balance is ",self.Balance)


class SavingsAccount(Account):

    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate=interestRate
        print("Welcome ",self.title)
        print("Your account balance is ",self.Balance)
        print("Your current interest rate is ",self.interestRate)
        print("- -"*15)
    
    def interestAmount(self):
        intAmt= (self.interestRate * self.Balance)/100
        return intAmt

name=input("Enter your name : ")
bal=int(input("Enter your balance : "))
intrst_rate=float(input("Enter interest rate : "))
user=SavingsAccount(name,bal,intrst_rate)
print("- -"*15)
print("Enter 1 for Depositing amount \nEnter 2 for Withdrawl \nEnter 3 for checking interest amount \nEnter 4 for checking balance \n")
choice=int(input())
if choice==1:
    amt=int(input("Enter amount to be deposited :"))
    user.deposit(amt)
    user.getBalance()
elif choice==2:
    amt=int(input("Enter amount to be withdrawn :"))
    user.withdrawal(amt)
    user.getBalance()
elif choice==3:
    print("Interest amount you will be receiving on your balance",user.Balance,"is ",user.interestAmount())
else:
    user.getBalance()
print("*"*50)
print("*"*50)

#----------------------------END OF CODE----------------------------
#====================================================================