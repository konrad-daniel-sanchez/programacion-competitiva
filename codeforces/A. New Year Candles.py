# https://codeforces.com/problemset/problem/379/A

a, b = [int(x) for x in input().split()]

h = a
while a >= b:
    div, mod = divmod(a, b)
    a = div + mod
    h += div

print(h)
