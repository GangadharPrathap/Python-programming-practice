# sorting of arrays using sorted() function
# the sorted() function returns a new sorted list from the elements of any iterable.
# the time complexity of sorted() function is O(n log n)
arr = list(map(int , input('enter the array elements: ').split()))
srr=sorted(arr)
print('sorted the array given in the input ', srr)