# Check if the array is sorted or not(Optimal Approach) o(n)
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
c=0
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        c=1
    else:
        c=0
if c==1:
    print("The array is sorted")
else: print("The array is not sorted")
# Alternative Approach o(nlogn)
# ss = arr.sort()
# if(arr == ss): print("the array is sorted")
# else: print("the array is not sorted")