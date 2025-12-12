# Find the largest number in an array(Optimal Apporach) o(n)
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("the largest number in the array is :",largest)
# Brute Force Approach o(nlogn)
# arr.sort()
# print("the largest number in the array is :",arr[-1])