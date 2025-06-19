N = int(input())
for _ in range(N):
    cnt=0
    a,b = map(int, input().split())
    if a%2==1:
        a=a+1
    if b%2==0:
        b=b+1
    for i in range(a,b,2):
        cnt+=i
    print(cnt)