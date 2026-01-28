import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())

    free_dist = 0          # total distance reachable with 0 rollbacks
    best_gain = 0          # maximum net gain per rollback

    for _ in range(n):
        a, b, c = map(int, input().split())

        # free jumps before the first rollback of this type
        free_dist += (b - 1) * a

        # net gain per rollback cycle
        gain = b * a - c
        if gain > best_gain:
            best_gain = gain

    # Case 1: reachable without any rollback
    if free_dist >= x:
        print(0)
        continue

    # Case 2: cannot make progress after free jumps
    if best_gain <= 0:
        print(-1)
        continue

    # Remaining distance after all free jumps
    remaining = x - free_dist

    # Minimum rollbacks needed
    ans = (remaining + best_gain - 1) // best_gain
    print(ans)
