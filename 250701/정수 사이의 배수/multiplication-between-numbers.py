a,b=map(int,input().split())
total,cnt=0,0

for i in range(a,b+1):
    if i%5==0 or i%7==0:
        total+=i
        cnt+=1

print(f"{total} {total/cnt:.1f}")