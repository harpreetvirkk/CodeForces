#https://codeforces.com/problemset/problem/118/A 
string = input()
string = string.lower()
new = []
for i in range(len(string)):
    if string[i] != 'a' and string[i] !='e' and string[i] !='i' and string[i] != 'o' and string[i] !='u' and string[i] !='y':
        new.append(string[i])
print("."+".".join(new))
a
