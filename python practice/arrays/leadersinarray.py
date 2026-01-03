arr=list(map(int,input("Enter the elements of array separated by space: ").split()))
n=len(arr)
leaders=[]
for i in range(n):
    max=arr[n-i]
    if arr[n-i-1]>max:
        leaders.append(arr[n-i-1])
        max=arr[n-2]