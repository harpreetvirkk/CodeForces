#https://codeforces.com/problemset/problem/116/A
n=int(input())
max=0
curr=0
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    curr=curr-a
    curr=curr+b
    if curr>max:
        max=curr
print(max)
