#https://codeforces.com/problemset/problem/4/A

weight = int(input())
if weight>2:
    if weight%2==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")