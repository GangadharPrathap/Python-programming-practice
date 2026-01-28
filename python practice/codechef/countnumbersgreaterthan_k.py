n=int(input("Enter the number to check:"))
arr=list(map(int,input("Enter the array elements").split()))
c=0
for x in arr:
    if x>n:
        c+=1
print(f"The total number of elements greater than {n} are: {c}")