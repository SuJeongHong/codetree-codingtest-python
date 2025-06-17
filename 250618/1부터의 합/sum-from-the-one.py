N = int(input())
total=0
for i in range(1,101):
    if total>N:
        break
    else:
        total+=i
if(i<3):
    print(i)
else:
    print(i-1)
