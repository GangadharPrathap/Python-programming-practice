# name = raw_input()                # Reading input from STDIN
# print 'Hi, %s.' % name           # Writing output to STDOUT
n=int(input())
m=int(input())

if(n>5*m or n>2*m or n>=m):
  if(n>5*m):
    print("Dairy Milk")
  if(n>2*m and n<=5*m):
    print("Shots")
  if(n>m and n<=2*m):
    print("Eclairs")
else:
  print("No Chocolates")