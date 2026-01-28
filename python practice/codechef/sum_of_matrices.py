n,m=map(int,input().split())
res = [list(map(int,input().split()))for _ in range(n)]
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        res[i][j]+=row[j]
for row in res:
    print(*row)        