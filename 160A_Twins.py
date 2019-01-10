#https://codeforces.com/problemset/problem/160/A
n=int(input())
coins=list(input().split())
coins=list(map(int, coins))
coins.sort(reverse=True)
total=0
count=0
for i in range(n):
    rest=sum(coins)
    if total<=rest:
        total=total+coins[i]
        coins[i]=0
        count=count+1
print(count)