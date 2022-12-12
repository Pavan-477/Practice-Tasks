arr_1=[1,9,3,10,4,20,2]
arr_2=[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
def subseq(arr):
    arr.sort()
    n=len(arr)
    l=[]
    count=1
    for i in range(1,n):
        if arr[i]-arr[i-1]==1:
            count+=1
        else:
            l.append(count)       
            count=1
    print(max(l))
subseq(arr_1)
subseq(arr_2)