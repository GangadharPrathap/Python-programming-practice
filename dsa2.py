def get_sum(n:int)-> int:
    s=0

    while n>0:
        r=n%10
        s+=r
        n=n//10
        return s
n=int(input())
print(get_sum(n))
