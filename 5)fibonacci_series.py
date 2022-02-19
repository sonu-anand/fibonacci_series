# Write a program to find the fibonacci series.

n = int(input("Enter a number to find fibonacci series : "))
a = 0
b = 1
for i in range(0,n):
    if i<=1:
        next = i
    else:
        next = a+b
        a = b
        b = next

    print(next,end=" ")





