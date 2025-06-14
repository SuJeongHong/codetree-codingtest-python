N = int(input())
List= list(map(int, input().split(" ")))
reList = [List*List for i in List]
print(reList)