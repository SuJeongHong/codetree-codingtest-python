N = int(input())

A = list(map(int, input().split()))
reA = [i*i for i in A]
for i in range(N):
    print(reA[i],end = " ")