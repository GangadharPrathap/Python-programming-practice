
arr = list(map(int,input("Enter the array of numbers").split()))


'''
----------------------Bubble Sort----------------------
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.
Time Complexity: O(n^2) in the worst and average case, O(n) in the best case (when the array is already sorted).
Space Complexity: O(1) (in-place sorting algorithm).



def BubbleSort(arr):
    n=len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
                flag = True
BubbleSort(arr)
print("Sorted array is: ",arr)
'''


'''
-----------------------Insertion Sort----------------------
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it has several advantages, such as simple implementation, efficient for small data sets, and adaptive (efficient for data sets that are already substantially sorted).
Time Complexity: O(n^2) in the worst and average case, O(n) in the best case (when the array is already sorted).
Space Complexity: O(1) (in-place sorting algorithm).


def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]> arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break
InsertionSort(arr)
print("Sorted array is: ",arr)'''



