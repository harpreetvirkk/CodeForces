pos=[]
pos=input()
size=len(pos)
danger=0
for i in range(size-6):
    if pos[i]==pos[i+1]:
        if pos[i]==pos[i+2]:
            if pos[i]==pos[i+3]:
                if pos[i]==pos[i+4]:
                    if pos[i]==pos[i+5]:
                        if pos[i]==pos[i+6]:
                            danger=1
if danger==1:
    print("YES")
else:
    print("NO")