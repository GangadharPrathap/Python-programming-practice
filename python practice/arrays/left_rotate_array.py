arr=list(map(int,input("Enter the array elements").split()))
temp=arr[0]
n=len(arr)
for i in (1,n):
    arr[i-1]=arr[i]
arr[n-1]=temp
print(arr)