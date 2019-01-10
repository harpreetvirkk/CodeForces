#https://codeforces.com/problemset/problem/58/A
word=list(input())
flag=-1
size=len(word)
for i in range(size):
    if word[i]=='h':
        for j in range(i+1, size):
            if word[j]=='e':
                for k in range(j+1, size):
                    if word[k]=='l':
                        for l in range(k+1, size):
                            if word[l]=='l':
                                for m in range(l+1, size):
                                    if word[m]=='o':
                                        flag=1
if flag==1:
    print("YES")
else:
    print("NO")
