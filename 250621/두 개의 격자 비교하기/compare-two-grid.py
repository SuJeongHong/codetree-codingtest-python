N, M=map(int, input().split())
matrix1=[list(map(int, input().split())) for _ in range(N)]
matrix2=[list(map(int, input().split())) for _ in range(N)]
same_matrix=[]
for i in range(N):
    row=[]
    for j in range(M):
        if matrix1[i][j]==matrix2[i][j]:
            row.append(0)
        else:
            row.append(1)
    same_matrix.append(row)

for i in range(N):
    for j in range(M):
        print(same_matrix[i][j],end=" ")
    print()