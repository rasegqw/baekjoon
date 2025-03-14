xywh=input()

source = xywh.split(" ")
# x = int(source[0])
# y = int(source[1])
# w = int(source[2])
# h = int(source[3])

# 계속 편하다고 C 스타일로 변수 하나하나 설정하지 말고,
# map 제대로 활용하기.
x, y, w, h = map(int, xywh.split(" "))

# def square(a,b,c,d) :
#     if c/2 - a >= 0 and d/2 - b >=0:
#         if a>b:
#             return b   
#         else:
#             return a 
#     elif c/2 - a <= 0 and d/2 - b >=0:
#         if (c-a)>b:
#             return y
#         else:
#             return c-a 
#     elif c/2 - a >= 0 and d/2 - y <=0:
#         if a>(d-y):
#             return d-b
#         else:
#             return a 
#     elif c/2 - a <= 0 and d/2 - b <=0:
#         if (c-a)>(d-b):
#             return d-b
#         else:
#             return c-a 
        
# min( iterable thing ) : 인수로 받은
#                        iterable( 반복이 가능한 데이터 타입 ) 자료형에서 최솟값 반환 함수.
print(f'{min(x, y, w-x, h-y)}')
    
# print(f"{square(x,y,w,h)}")