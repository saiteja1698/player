s=int(input())
result=0
while ((s!=0) and (s<=1000000000000000000)) :
    r=s%10
    result+=pow(r,2)
    s//=10
print(result)
