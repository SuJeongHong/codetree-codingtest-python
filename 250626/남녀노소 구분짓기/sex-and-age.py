gender=int(input())
age=int(input())
if age<19:
    if gender==0:
        print("BOY")
    elif gender==1:
        print("GIRL")
else:
    if gender==0:
        print("MAN")
    elif gender==1:
        print("WOMAN")