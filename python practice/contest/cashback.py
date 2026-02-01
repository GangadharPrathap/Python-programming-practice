# Cashback
# A customer is buying a cake from Chef's store for
# X
# X rupees.

# Chef has a cashback policy, where for any purchase of at least
# 200
# 200 rupees, he returns
# 50
# 50 rupees as a discount.

# What is the effective amount the customer paid for the cake?

# Input Format
# The first and only line contains a single integer
# X
# X - the price of the cake.
# Output Format
# Output the effective amount paid by the customer.

# Constraints
# 100
# ≤
# X
# ≤
# 500
# 100≤X≤500
# Sample 1:
# Input
# Output
# 210
# 160
# Explanation:
# Since the purchase amount is at least
# 200
# 200 rupees, the customer gets a cashback of
# 50
# 50 rupees.

# Sample 2:
# Input
# Output
# 150
# 150
# Explanation:
# Since the purchase amount is not at least
# 200
# 200 rupees, there is no cashback.

# accepted
# Accepted
# 4
# total-Submissions
# Submissions
# 7
# accuracy
# Accuracy
# 57.14
# Did you like the problem statement?
# More Info
# Time limit1 secs
# Memory limit1.5 GB
# Source Limit50000 Bytes

n=int(input())
if n >= 200:
    print(n-50)
else:
    print(n)