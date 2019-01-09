#https://codeforces.com/problemset/problem/1/A
import math
m,n,a=input().split()
m=int(m)
n=int(n)
a=int(a)
x=math.ceil(m/a)
y=math.ceil(n/a)
print(x*y)