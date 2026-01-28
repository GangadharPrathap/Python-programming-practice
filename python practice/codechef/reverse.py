arr=list(map(int,input().split()))
n=len(arr)
rev=[]
for x in range(n-1,-1,-1):
    rev.append(arr[x])
print(rev)