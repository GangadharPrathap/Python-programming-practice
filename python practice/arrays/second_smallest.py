# Find the second smallest number in an array(Optimal Approach) o(n)
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
smallest=arr[0]
secsmallest=-1
for i in arr:
    if i<smallest:
        secsmallest=smallest
        smallest=i
    if i>smallest and i<secsmallest:
        secsmallest=i
print("The smallest number in the array is :",smallest)
print("The second smallest number in the array is :",secsmallest)
# second smallest number in an array(Brute Force Approach) o(nlogn)
# arr.sort()
# print("the second smallest number in the array is :",arr[1])