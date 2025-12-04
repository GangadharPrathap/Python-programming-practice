import math
def factor_count1(n):
  # Uses O(N) logic
  fc = 0
  for i in range(1, n + 1):
    if n % i == 0:
      fc += 1
  print(f"Number of factors of {n} are {fc}")

def factor_count2(n):
  # Uses O(sqrt(N)) logic
  fc = 0
  for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
      if i == n//i:
        fc += 1
      else:
        fc += 2
  print(f"Number of factors of {n} are {fc}")

factor_count1(100000000)
factor_count2(100000000)