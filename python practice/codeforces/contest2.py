import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    both = 0       # numbers usable as both row and column
    row_only = 0  # usable only as row
    col_only = 0  # usable only as column

    for x in a:
        if x <= h and x <= l:
            both += 1
        elif x <= h:
            row_only += 1
        elif x <= l:
            col_only += 1

    # First, pair row-only with col-only
    pairs = min(row_only, col_only)

    # Remaining usable numbers are in `both`
    # Each pair needs two numbers
    pairs += both // 2

    print(pairs)
