#https://codeforces.com/problemset/problem/546/A
k, n, w = input().split()
k=int(k)
n=int(n)
w=int(w)
cost=0
for i in range(w):
    cost=cost+(k*(i+1))
if cost>n:
    borrow=cost-n
else:
    borrow=0
print(borrow)