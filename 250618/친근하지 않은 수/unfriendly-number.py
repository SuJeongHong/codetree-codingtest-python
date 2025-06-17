N = int(input())
count=N
for i in range(1001):
    if N==0:
        break
    elif N%2==0:
        count-=1
    elif N%3==0:
        count-=1
    elif N%5==0:
        count-=1
    N -=1
print(count)