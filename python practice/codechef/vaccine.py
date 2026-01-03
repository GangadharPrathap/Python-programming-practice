# cook your dish here
n=int(input())
for i in range(n):
    a,s,d=map(int,input().split())
    if(s<=a<d):
        print("Take second dose now")
    if(s<a>=d):
        print("Too Late")
    if(a<s):
        print("Too Early")