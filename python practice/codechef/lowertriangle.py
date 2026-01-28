n=int(input().strip())
mat=[list(map(int,input().split())) for _ in range(n)]
lsum=0
for i in range(n):
    for j in range(i+1):
        lsum += mat[i][j]
print(lsum)