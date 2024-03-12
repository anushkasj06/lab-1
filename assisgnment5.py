s1 = int(input("enter the marks of sub 1 = "))
s2 = int(input("enter the marks of sub 2 = "))
s3 = int(input("enter the marks of sub 3 = "))
s4 = int(input("enter the marks of sub 4 = "))
s5 = int(input("enter the marks of sub 5 = "))

total = (s1 +s2+ s3+s4+s5)*20

if(total>=75):
    print("Distinction")
elif(total >=60 and total <75):
    print("First Class")
elif(total>=50 and total<60):
    print("Second Class")
elif(total>=40 and total<50):
    print("Third Class")
else:
    print("fail")
