
arr=[1,2,3,4,5]
#Since insertion at any index in arrays is possible , 
#Inserting the last element at the zeroth index would inturn rotate the entire array clockwise by one
arr.insert(0,arr.pop())
print(arr)