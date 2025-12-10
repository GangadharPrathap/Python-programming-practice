# Scoring
# Alice and Bob were playing a game with points to score. Each player's score is some non-negative integer number of points.
# In the end, Alice won the game by scoring X more points than Bob. Further, it is known that the total number of points scored by both of them was Y
# With this information, your task is to find how many points Alice scored, and how many points Bob scored. It is guaranteed that the input is generated such that there exists a valid solution.
# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    x=(b-a)//2
    y=(b+a)//2
    print(y,x)