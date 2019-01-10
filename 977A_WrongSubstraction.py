#https://codeforces.com/problemset/problem/977/A
n, k=input().split()
n=int(n)
k=int(k)
for i in range(k):
    if n%10!=0:
        n=n-1
    else:
        n=int(n/10)
print(n)
