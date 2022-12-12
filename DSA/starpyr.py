for i in range(1,11,2):
    for j in range(i):
        print('*',end='')
    print()
#---------------------------Approach 2---------
count=1
print()
for i in range(1,6):
    print('*'*count)
    count+=2