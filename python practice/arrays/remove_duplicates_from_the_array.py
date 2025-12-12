# Remove Duplicates from the array(Optimal Approach) o(n)
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
i=0
n=len(arr)
for j in range(n):
    if arr[i]!=arr[j]:
        arr[i+1]=arr[j]
        i+=1
print(i+1)
# for brute force approach o(nlogn)
# arr=list(map(int,input("Enter the numbers separated by space: ").split()))
# arr=set(arr)
# arr=list(arr)
# arr.sort()
# print(len(arr))
# print(arr)
# print("the array after removing duplicates is :",arr)
# print("the length of the array after removing duplicates is :",len(arr))