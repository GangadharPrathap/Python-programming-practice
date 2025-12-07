# Average of elements in an array
arr=list(map(int,input('Enter the elements of the array separated by spaces: ').split()))
t=0
for i in range(len(arr)):
    t=t+arr[i]
avg=t/len(arr)
print('the average of the array is : ', avg)