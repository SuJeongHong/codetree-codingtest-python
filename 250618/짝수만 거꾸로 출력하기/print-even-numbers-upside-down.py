N = int(input())
list1=list(map(int, input().split()))
for i in range(len(list1)-1,-1, -1):
    if list1[i]%2==0:
        print(list1[i], end=" ")
    