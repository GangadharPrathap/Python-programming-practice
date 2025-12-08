# Linear search in an array
def linear_search(arr,t):
    for i in range(len(arr)):
        if arr[i]==t:
            return i
    return -1
arr=list(map(int,input('Enter the elements of the array separated by spaces: ').split()))
t=int(input('Enter the target element to search: '))
res=linear_search(arr,t)
if res!=-1:
    print('Element found at index: ',res)
else:
    print('Element not found in the array')