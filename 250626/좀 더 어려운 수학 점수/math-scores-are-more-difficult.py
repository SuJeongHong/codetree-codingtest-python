a_m, a_e=map(int, input().split())
b_m, b_e=map(int, input().split())
if a_m>b_m:
    print("A")
elif b_m>a_m:
    print("B")
elif a_m==b_m:
    if a_e>b_e:
        print("A")
    elif b_e>a_e:
        print("B")