N = int(input())
total=0
for i in range(1,102):
    if total>=N:
        break
    else:
        total+=i
print(i-1)