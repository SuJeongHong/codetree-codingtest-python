n= int(input())
#1,3,5,7,8,10,12 :31
#2:28
#4,6,9,11:28
if (n%2==1 and n<=7)or n==8 or n==10 or n==12:
    print("31")
elif n==2:
    print(28)
else:
    print(30)