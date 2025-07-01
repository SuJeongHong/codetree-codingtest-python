n=int(input())
cnt=0
for i in range(1,1001):
    if cnt>=n:
        print(i-1)
        break
    else:
        cnt+=i