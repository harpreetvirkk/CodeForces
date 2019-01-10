#https://codeforces.com/problemset/problem/266/A
n=int(input())
stones=input()
count=0
for i in range(n-1):
    if stones[i]==stones[i+1]:
        count = count+1
print(count)
