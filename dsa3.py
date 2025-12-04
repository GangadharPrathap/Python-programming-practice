def get_reverse(n: int) -> int:
  rev = 0
  while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
  return rev

n = int(input("enter the number to be reversed"))
print(get_reverse(n))
print(n)

m = int(input())
lst = list(map(int, input().split()))

for i in range(m): # 0, n - 1
  print(lst[i] * lst[i])