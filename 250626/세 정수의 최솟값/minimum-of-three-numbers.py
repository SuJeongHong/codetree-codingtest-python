a,b,c=map(int, input().split())
small=0
if a<=b and a<=c:
    small=a
if b<=a and b<=c:
    small=b
if c<=a and c<=b:
    small=c
    
print(small)