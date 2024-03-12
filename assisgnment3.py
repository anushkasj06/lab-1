year = int(input("enter the birth year of empolyee"))
salary = int(input("enter the salary of the empolyee"))

def calculateAge():
    age = 2024 - year
    print("The age of the empolyee = ",age)

def convertSalary():
    newSal = salary/80
    print("The converted salary =",newSal)

calculateAge()
convertSalary()