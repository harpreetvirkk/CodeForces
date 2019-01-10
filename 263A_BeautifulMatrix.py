row1=list(input().split())
row2=list(input().split())
row3=list(input().split())
row4=list(input().split())
row5=list(input().split())
count=0
r=-1
j=-1
for i in range(5):
    if row1[i]=='1':
        r=0
        j=i
    if row2[i]=='1':
        r=1
        j=i
    if row3[i]=='1':
        r=2
        j=i
    if row4[i]=='1':
        r=3
        j=i
    if row5[i]=='1':
        r=4
        j=i
if r==0 or r==4:
    count=count+2
elif r==1 or r==3:
    count=count+1
if j==0 or j==4:
    count=count+2
elif j==1 or j==3:
    count=count+1
print(count)
