a_age,a_gender=input().split()
b_age, b_gender=input().split()
a_age=int(a_age)
b_age=int(b_age)
if (a_age>=19 and a_gender=="M") or (b_age>=19 and b_gender=="M"):
    print(1)
else:
    print(0)