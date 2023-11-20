# https://codeforces.com/problemset/problem/579/A
import math

# Time complexity: O(Log(N)) Logarithmic runtime
# Space complexity: O(1) Constant space
x = int(input())

c = 0
while x > 1:
    _log = int(math.log(x)/math.log(2))
    x -= 2**_log
    c += 1

print(c + x)
