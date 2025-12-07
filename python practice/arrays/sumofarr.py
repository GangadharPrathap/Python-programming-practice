# Sum of elements in an array
arr=list(map(int,input('Enter the elements of the array:').split()))
t=0
for i in range(len(arr)):
    t=t+arr[i]
print('Sum of elements in the array is:', t)