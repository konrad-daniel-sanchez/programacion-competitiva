# https://codeforces.com/contest/1807/problem/C

# Time complexity: O(N) Linear runtime
# Space complexity: O(N) Linear space
def solve(s):
    d = {}
    for i, e in enumerate(s):
        if e not in d:
            d[e] = i % 2
        elif d[e] != i % 2:
            return 'NO'
    return 'YES'
        

t = int(input())


for i in range(t):
    n = int(input())
    s = input()
    print(solve(s))
