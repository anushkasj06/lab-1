n = int(input("enter the nth number for which you want fibonacci number"))


def fib(n):
    if(n<=1):
        return 1
    else:
        return (fib(n-1) + fib(n-2))


for i in range (n):
    print(fib(i))
       

