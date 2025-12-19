arr=list(map(int,input().split()))
n=len(arr)
for i in range(n+1):
    if arr[i]==0:
        arr[n],arr[i]=arr[i],arr[n]
        n-=1
print(arr)