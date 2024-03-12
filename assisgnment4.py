n=int(input("enter the number you want to reverse"))
newnum = 0
while(n!=0):
    temp = n%10
    newnum = newnum * 10 + temp
    n = n//10
print("the reverese number is = ", newnum)    

