def reverser():
    arr=list(map(int,input().split()))
    i,j=0,len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    print(" ".join(map(str,arr)))
if __name__ == "__main__":
    reverser()
#  Array Reversal
# Given an array of integers, reverse the array without using any inbuilt functions.