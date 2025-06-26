a_cold, a_tmp= input().split()
b_cold, b_tmp=input().split()
c_cold, c_tmp=input().split()

a_tmp=int(a_tmp)
b_tmp=int(b_tmp)
c_tmp=int(c_tmp)
cnt=0
if a_cold=="Y" and a_tmp>=37:
    cnt+=1
if b_cold=="Y" and b_tmp>=37:
    cnt+=1
if c_cold=="Y" and c_tmp>=37:
    cnt+=1

if cnt>=2:
    print("E")
else:
    print("N")