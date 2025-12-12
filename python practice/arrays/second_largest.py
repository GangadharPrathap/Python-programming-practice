# Find the second largest number in an array(Optimal Approach) o(n)
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
largest=arr[0]
slargest=-1
for i in arr:
    if i> largest:
        slargest=largest
        largest = i
    if i<largest and i>slargest:
        slargest=i
print("The largest number in the array is :",largest)
print("the second largest number in the array is :",slargest)
# second largest number in an array(Brute Force Approach) o(nlogn)
# arr.sort()
# print("the second largest number in the array is :",arr[-2])