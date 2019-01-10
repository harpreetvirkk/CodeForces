#https://codeforces.com/problemset/problem/1030/A
n=int(input())
person=list(input().split())
flag=0
for i in range(n):
    if person[i]=='1':
        flag=1
if flag==1:
    print("HARD")
else:
    print("EASY")