n = int(input())
d=0
for i in range(0,n):
    for j in range(1,n+1):
        print(2*j+(9+d),end=" ")
    d+=2
    print() 
