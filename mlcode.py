# name = raw_input()                # Reading input from STDIN
# print 'Hi, %s.' % name           # Writing output to STDOUT
n=int(input())
a=n-1
b=49-n
if(a==b):
  print("Go Anywhere")
else:
  if(a<b):
    print("RK Beach")
  else:
    print("RU Beach")