total=0
N=int(input())
for i in range(1,N+1):
    if i%2==1 and i%3==0:
        total+=i
print(total)