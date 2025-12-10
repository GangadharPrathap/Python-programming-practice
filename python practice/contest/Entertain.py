# Entertainments
# Chef is trying to entertain N children. He has 2 options:
# Buy a single television for all the children to watch. This will cost 1000 rupees.Buy N toys, one for each child. This will cost 200 rupees for each toy.
# What is the minimum cost Chef needs to pay to entertain all the children?
# cook your dish here
n=int(input())
if(n*200>1000):
    print(1000)
else:
    print(n*200)