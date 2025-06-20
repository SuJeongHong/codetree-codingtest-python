matrix=[list(map(int, input().split())) for _ in range(3)]
new_matrix=[]
for i in range(3):
    for j in range(3):
       print(matrix[i][j]*3,end=" ")
    print()
#         new_matrix.append(matrix[i][j]*3)
# print(matrix)