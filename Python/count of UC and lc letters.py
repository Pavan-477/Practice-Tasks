s='The quick Brow Fox'
print(s)
print("Enter 1 for going with the  above String \nEnter 2 for entering a new string of your choice")
choice=input()
if choice!="1":
    s=input("Enter the string :")
def UpperLower(s):
    counter={"uc":0,"lc":0}
    for i in s:
        if i==" ":
            pass
        elif i.islower():
            counter["lc"]+=1
        elif i.isupper():
            counter["uc"]+=1
    print(s)
    print("Number of uppercase letters in the string are :",counter["uc"])
    print("Number of lowercase letters in the string are :",counter["lc"])
    return ""
UpperLower(s)