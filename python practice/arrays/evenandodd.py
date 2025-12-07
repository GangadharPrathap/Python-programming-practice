#Count of Even number and Odd numbers in an array
arr=list(map(int,input('Enter the elements of the array separated by spaces: ').split()))
c=0
d=0
for i in range(len(arr)):
    if arr[i]%2==0:
        c+=1
    else:
        d+=1
print('The total even numbers in the array are: ',c)
print('the total odd numbers in the array are: ',d)