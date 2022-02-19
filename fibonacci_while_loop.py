# Write a program to find fibonacci series using while loop.

n = int(input("Enter how many fib series you want : "))
a = 0
b = 1
if n<=1:
    print(a,b)
else:
    print(a,b,end=" ")
    while(n>2):
        sum = a+b
        a = b
        b = sum
        n = n-1
        print(sum,end = " ")