N=int(input())
sum_val,cnt=0,0
for _ in range(N):
    num=int(input())
    sum_val+=num
    cnt+=1
print(f"{sum_val} {sum_val/cnt:.1f}")