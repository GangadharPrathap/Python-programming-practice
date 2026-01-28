n,m=map(int,input().split())
image = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    image[i].reverse()
    for j in range(m):
        image[i][j] = 1 - image[i][j]
for row in image:
    print(*row)        