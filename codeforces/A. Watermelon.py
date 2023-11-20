# https://codeforces.com/problemset/problem/4/A

# Time complexity: O(1) Constant runtime
# Space complexity: O(1) Constant space
n = int(input())
if n < 3:
    print('NO')
elif n % 2 == 0:
    print('YES')
else:
    print('NO')
