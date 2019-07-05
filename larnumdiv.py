c,d=map(int,(input().split()))
s=0
for x in range(2,d):
        if(c%x==0 and d%x==0):
            s=x
print(s)
