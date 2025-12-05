print('Max and Min in the array')
arr=list(map(int,input('enter the array elements: ').split()))
mx=arr[0]
mn=arr[0]
for i in range (1,len(arr)):
    if arr[i]>mx:
        mx=arr[i]
    if arr[i]<mn:
        mn=arr[i]
print('Maximum element is:',mx)
print('Minimum element is:',mn)