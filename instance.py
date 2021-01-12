###instance method###
# ex - 1
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.total = marks

    def display(self):
        print('Hi ', self.name)

stud1 = Student('hari',450)
stud1.display() 
print("          ")#space

# ex - 2


class Office:
    noOfHolidays = 10
    @classmethod
    def checkHolidays(cls,noOfHolidays):
        print("This year we have  ", cls.noOfHolidays)

Office.checkHolidays(15) 
print("          ")#space

# ex - 3

class Office:
    noOfHolidays = 10
    @classmethod
    def checkHolidays(cls,branch):
        print('This year our ', branch, ' has ', cls.noOfHolidays)

Office.checkHolidays('Chennai') 
Office.checkHolidays('bengaluru') 
print("          ")#space

# ex - 4

class Calculator:

    @staticmethod
    def add(no1,no2):
        print('Result is ', no1+no2)


Calculator.add(100,200) 

print("          ")#space






