#https://codeforces.com/problemset/problem/705/A
n=int(input())
flag=0
sentence=[]
if n==1:
    sentence.append("I hate it")
else:
    for i in range(n):
        if flag==0:
            sentence.append("I hate that ")
            flag=1
        else:
            sentence.append("I love that ")
            flag=0
    if flag==1:
        sentence.pop(n-1)
        sentence.append("I hate it")
    else:
        sentence.pop(n-1)
        sentence.append("I love it")
print("".join(sentence))
