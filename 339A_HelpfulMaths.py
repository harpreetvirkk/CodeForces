#https://codeforces.com/problemset/problem/339/A
line=input()
count_1=0
count_2=0
count_3=0
size = len(line)
for i in range(size):
    if line[i]=='1':
        count_1=count_1+1
    elif line[i]=='2':
        count_2=count_2+1
    elif line[i]=='3':
        count_3=count_3+1
    else:
        continue
newln = []
for i in range(count_1):
    newln.append("1")
    newln.append("+")
for i in range(count_2):
    newln.append("2")
    newln.append("+")
for i in range(count_3):
    newln.append("3")
    newln.append("+")
newln.pop(size)
print("".join(newln))