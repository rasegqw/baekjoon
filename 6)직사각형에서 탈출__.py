xywh=input()

source = xywh.split(" ")
x = int(source[0])
y = int(source[1])
w = int(source[2])
h = int(source[3])



def square(a,b,c,d) :
    if c/2 - a >= 0 and d/2 - b >=0:
        if a>b:
            return b   
        else:
            return a 
    elif c/2 - a <= 0 and d/2 - b >=0:
        if (c-a)>b:
            return y
        else:
            return c-a 
    elif c/2 - a >= 0 and d/2 - y <=0:
        if a>(d-y):
            return d-b
        else:
            return a 
    elif c/2 - a <= 0 and d/2 - b <=0:
        if (c-a)>(d-b):
            return d-b
        else:
            return c-a 
    
print(f"{square(x,y,w,h)}")