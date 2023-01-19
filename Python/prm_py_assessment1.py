# Question 1
 
n = int(input("Enter the number of elements : "))
l = [x for x in input("Enter the elements separated by space : ").split()]
if len(l)==n:
    try:
        sorted_list = sorted(l, key= lambda l: l[-2])
        print(sorted_list)
    except:
        print('Invalid entries please try again !!')
else:
    print('Number of elements entered are not equal to the number of elements specified ')
    print('Please Try again')
