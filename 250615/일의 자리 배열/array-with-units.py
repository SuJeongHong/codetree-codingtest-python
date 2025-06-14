A,B = map(int, input().split())
L=[A,B]
for i in range(8):
    next1 = (L[-2]+L[-1])%10
    L.append(next1)
print(*L)