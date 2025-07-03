a,b,c=map(int, input().split())
st=False
for i in range(a,b+1):
    if i%c==0:
        st=True
if st==True:
    print("NO")
else:
    print("YES")