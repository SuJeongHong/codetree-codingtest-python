matrix=[list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    cnt=0
    for j in range(4):
        cnt+=matrix[i][j]
    print(cnt)
    