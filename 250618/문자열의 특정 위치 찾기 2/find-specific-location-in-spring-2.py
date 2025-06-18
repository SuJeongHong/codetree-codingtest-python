string=["apple", "banana", "grape", "blueberry", "orange"]
n=input()
cnt=0
for i in string:
    if n==i[2]or n==i[3]:
        print(i)
        cnt+=1
print(cnt)