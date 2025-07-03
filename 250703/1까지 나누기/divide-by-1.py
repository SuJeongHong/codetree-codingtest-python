n=int(input())
re=n
cnt=0
for i in range(1,n):
    if re<=1:
        break
    re=re//i
    cnt+=1
print(cnt)