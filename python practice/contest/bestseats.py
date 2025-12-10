# # Best Seats
# Chef and Chefina are trying to watch a cricket game. They have already decided a row of N seats where they will seat, but they are yet to figure out the exact 2 seats they will buy. The i-th seat in the row costs coins to buy. Obviously, they have to sit next to each other, so they will only buy adjacent seats.
# Can you figure out the minimum cost for them to buy seats such that they are able to sit together?
import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    i = 1
    ans = []
    for _ in range(t):
        n = data[i]; i += 1
        arr = data[i:i+n]; i += n
        best = min(arr[k] + arr[k+1] for k in range(n-1))
        ans.append(str(best))
    print("\n".join(ans))

if __name__ == "__main__":
    solve()