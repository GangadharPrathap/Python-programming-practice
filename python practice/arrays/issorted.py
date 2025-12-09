def issorted(arr):
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            return 1
        else:
            return 0
arr=list(map(int,input('Enter the earray of elements to check them: ').split()))
res=issorted(arr)
if res==1:
    print('the array is sorted')
else:
    print('the array is not sorted')