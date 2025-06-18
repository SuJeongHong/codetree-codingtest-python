A, B =map(int, input().split())
n=A
while B>=n:
    print(n,end=" ")
    if n%2==0:
        n=n+3
    else:
        n=n*2
