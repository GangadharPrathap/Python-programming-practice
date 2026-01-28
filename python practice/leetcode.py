class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr=[n]
        for i in range(n):
            if(i%3 == 0 or i%5 == 0):
                if(i%3==0):
                    arr[i]="Fizz"
                if(i%5 == 0):
                    arr[i]="Buzz"
            else:
                arr[i]=i
        return arr

if __name__ == "__main__":
    n = 15  # change as needed
    sol = Solution()
    result = sol.fizzBuzz(n)
    print(result)