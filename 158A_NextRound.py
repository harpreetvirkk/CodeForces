#https://codeforces.com/problemset/problem/158/A
n,k=input().split()
n=int(n)
k=int(k)
score = []
score = input().split()
count=0
compare = int(score[k-1])
for i in range(n):
    if int(score[i])>0:
        if int(score[i])>=compare:
            count = count+1
print(count)