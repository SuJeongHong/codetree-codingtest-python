n=int(input())
st=False
for i in range(2,n):
    if n%i==0:
        st=True
        break
if st==True:
    print("C")
else:
    print("P")