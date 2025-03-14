A = input()

A = int(A)

def exam(x):
    if x>=90 and x<=100:
        print("A")
    elif x<90 and x>=80:
        print("B")
    elif x<80 and x>=70:
        print("C")
    elif x<70 and x>=60:
        print("D")
    else:
        print("F")


exam(A)