L_eye=float(input())
R_eye=float(input())

if L_eye>=1.0 and R_eye>=1.0:
    print("High")
elif L_eye>=0.5 and R_eye>=0.5:
    print("Middle")
else:
    print("Low")