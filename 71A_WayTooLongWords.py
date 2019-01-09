#https://codeforces.com/problemset/problem/71/A
n=int(input())
words =[]
for i in range(n):
    words.append(input())
for i in range(n):
    x=words[i]
    if(len(x)>10):
        mid=len(x.strip())-2
        size=len(x)-1
        print(x[0]+str(mid)+x[size])
    else:
        print(words[i])