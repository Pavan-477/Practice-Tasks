#provision to try on user defined array
#arr_1=list(map(int,input('Enter numbers sep by space').split()))
def peak(arr):
    if len(arr)<1:
        return ''
    peak_elements=[]
    for i in range(len(arr)):
        if i==0:
            if arr[i]>arr[i+1]:
                peak_elements.append(arr[i])
        elif i==len(arr)-1:
            if arr[i]>arr[i-1]:
                peak_elements.append(arr[i])
        else :
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                peak_elements.append(arr[i])
    return peak_elements

print(peak([5, 10, 20, 15]))
print(peak([10, 20, 15, 2, 23, 90, 67]))
print(peak([10,30,20]))
#print(peak(arr_1)) 