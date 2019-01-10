#https://codeforces.com/problemset/problem/236/A
name=list(input())
distinct=0
name=list(dict.fromkeys(name))
distinct=len(name)
if distinct%2==1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")