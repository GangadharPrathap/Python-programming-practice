n = int(input().strip())
mat = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    mat[i][i],mat[i][n-i-1] = mat[i][n-i-1],mat[i][i]
for row in mat:
    print(*row)