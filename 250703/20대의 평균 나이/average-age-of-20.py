total=0
cnt=0
while True:
    age=int(input())
    if age<20 or age>=30:
        break
    total+=age
    cnt+=1
print(f"{total/cnt:.2f}")