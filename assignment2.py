n=int(input("enter the number"))
if(n<10 and n>0):
    print("square is = ",n*n)
elif(n>9 and n<100 ):
    print("squareroot is = ",n**0.5)
elif(n>99 and n<1000):
    print("cube root = ",n**(1/3))
else:
    print("no valid input")
