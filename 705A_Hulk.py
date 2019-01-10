n=int(input())
flag=0
if n==1:
    print("I hate it")
else:
    for i in range(n):
        if flag==0:
            print("I hate "),
            flag=1
        else:
            print("I love "),
            flag=0
        print("that ")
