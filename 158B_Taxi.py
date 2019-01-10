#https://codeforces.com/problemset/problem/158/B
n=int(input())
groups=list(input().split())
count1=0
count2=0
count3=0
count4=0
taxi=0
for x in groups:
    if x=='1':
        count1=count1+1
    elif x=='2':
        count2=count2+1
    elif x=='3':
        count3=count3+1
    elif x=='4':
        count4=count4+1
taxi=count4
if count3>=count1:
    taxi=taxi+count3
    count1=0
else:
    taxi=taxi+count3
    count1=count1-count3
if count2>0 and count2%2==0:
    taxi=taxi+int(count2/2)
elif count2>0 and count2%2==1:
    taxi=taxi+int(count2/2)+1
    if count1>2:
        count1=count1-2
    else:
        count1=0
if count1>0 and count1<=4:
    taxi=taxi+1
elif count1>4 and count1%4==0:
    taxi=taxi+int(count1/4)
else:
    if count1>0:
        taxi=taxi+int(count1/4)+1
print(taxi)