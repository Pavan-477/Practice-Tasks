#Write a Python program to get the Fibonacci series between 0 to 50     0, 1, 1, 2, 3, 5, 8, 13, 21, ....
n=int(input("Enter a positive number upto which you want the fibonacci series : "))
if n>0:
    a=0
    b=1
    print("Fibonacci series upto ",n,"is :")
    print(a,end=' ')
    print(b,end=' ')
    for i  in range(n+1):
        c=a+b
        if c<n:
            a=b
            b=c
            print(c,end=' ')
else:
    print("Please enter a positive number to generate fibonacci series ")