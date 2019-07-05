n=int(input())
l=input()
t=l[::-1]
for i in t :
    if ((i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u') or (i=='A') or (i=='E') or (i=='I') or (i=='O') or (i=='U')) :
        continue
    else :
        print(i,end='')
