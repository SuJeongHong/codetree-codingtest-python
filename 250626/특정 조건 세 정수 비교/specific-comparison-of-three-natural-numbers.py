a,b,c=map(int, input().split())
low=0
if a<=b and a<=c:
    low=1
else:
    low=0
same=0
if a==b and b==c:
    same=1
else:
    same=0
print(low, same)