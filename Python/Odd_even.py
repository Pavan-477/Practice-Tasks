#Write a Python program to count the number of even and odd numbers from a series of numbers.

even,odd=0,0
n= int(input("Enter the length of  the series :"))
for i in range(1,n+1):
    print("Enter element number",i)
    m = int(input())
    
    if m%2==0:
        even+=1
    else :
        odd+=1
print("Number of even numbers in the series :",even)
print("Number of odd numbers in the series :",odd)