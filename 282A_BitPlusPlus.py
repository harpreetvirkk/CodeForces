#https://codeforces.com/problemset/problem/282/A
n = int(input())
x=0
for i in range(n):
    statement = input()
    if statement == 'X++' or statement == '++X':
        x=x+1
    else:
        x=x-1
print(x)