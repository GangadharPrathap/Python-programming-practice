def check_feel_good(n, s):
  cv=0
  v="aeiou"
  for ch in s:
    if ch in v:
      cv+=1
  if cv>=n//2:
    return "Feel good!"
  else:
    return "Feel bad!"
n=int(input())
s=input()
print(check_feel_good(n, s))