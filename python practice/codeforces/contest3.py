import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    p = [0] * (n + 1)
    used = set()

    # Fix p[n]
    p[n] = 1
    used.add(1)

    # Construct p[i] = 1 XOR i
    for i in range(2, n):
        p[i] = 1 ^ i
        used.add(p[i])

    # Remaining number goes to p[1]
    for x in range(1, n + 1):
        if x not in used:
            p[1] = x
            break

    print(*p[1:])
