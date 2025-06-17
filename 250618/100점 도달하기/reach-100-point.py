score= int(input())
for i in range(100):
    if score==100:
        print("A")
        break
    elif score>=90:
        print("A",end=" ")
    elif score>=80:
        print("B",end=" ")
    elif score>=70:
        print("C",end=" ")
    elif score>=60:
        print("D",end=" ")
    elif score<60:
        print("F", end=" ")
    score=score+1
