#구구단 함수를 ex03_function.py 에 각각 정의하고
# main에서 1,2 번 선택을 받아 세로형, 가로형을 각각 출력할 수 있도록하시오

from ex03_function import *

run = True
while run:
    num = int(input("숫자를 입력하세요"))
    
    if(num == 1):
        sero()
    elif(num == 2):
        garo()
    else :
        print("종료")
        run = False