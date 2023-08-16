# 실행하면 콘솔에서 1또는 2를 입력받고 1은 세로형 구구단, 2는 가로형 구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의

def garo ():
    for x in range(2,10):
        for y in range(1,10):
            print(x, 'X', y, '=', x * y)
        print()   

def sero ():
    for x in range(2,10):
        for y in range(1,10):
            print(x, 'X', y, '=', x * y, "/", end= "    ")
        print()  

while True :
    num = int(input("1 or 2 를 입력하세요: "))

    if num == 1 :
        garo()
    elif num == 2 :
        sero()
    else :
        print("제대로 입력하세요")       

