matrix1=[list(map(int, input().split())) for _ in range(3)]
input()
matrix2=[list(map(int, input().split())) for _ in range(3)]

mul_matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(matrix1[i][j]* matrix2[i][j])
    mul_matrix.append(row)

for i in range(3):
    for j in range(3):
        print(mul_matrix[i][j], end =" ")
    print()