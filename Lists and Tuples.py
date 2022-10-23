#Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
# from a given list of non-empty tuples

l=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(l)
print("Enter 1 for going with the sorting of above list \nEnter anything except 1 for creating your own list of tuples")
choice=input()
if choice!="1":
    n=int(input("Enter number of tuples you want inside the list :"))
    l=[]
    for i in range(1,n+1):
        print("Enter first element inside tuple",i)
        n1=int(input())
        print("Enter second element inside tuple ",i)
        n2=int(input())
        l.insert(i,(n1,n2))
print("List before sorting  :",l)

for i in range(len(l)):
    l[i]=list(l[i])
    l[i].reverse()
    l[i]=tuple(l[i])
l.sort()

for i in range(len(l)):
    l[i]=list(l[i])
    l[i].reverse()
    l[i]=tuple(l[i])
print("List after sorting  :" ,l)
