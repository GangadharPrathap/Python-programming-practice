# Occurance count in an array
arr=list(map(int,input('Enter the elements of the array separated by spaces: ').split()))
target=int(input('Enter the target element to find its occurance count: '))
c=0
for i in range(len(arr)):
    if arr[i]==target:
        c+=1
print('the occurance of the target element in the array is : ',c)