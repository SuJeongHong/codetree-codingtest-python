N = int(input())
for i in range(1,N+1):
    a=i
    b=N+1-i
    for j in range(N):
        if j%2==0:
            print(a, end="")
        else:
            print(b, end="")
    print()