#https://codeforces.com/problemset/problem/231/A
n=int(input())
count = 0
for i in range(n):
    p, v, t = input().split()
    p=int(p)
    v=int(v)
    t=int(t)
    if p+v+t>=2:
        count = count+1
print(count)