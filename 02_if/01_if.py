# num 의 값에 따라 양수, 음수, 0입니다. 출력하기
num=0

if num > 0 : 
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0입니다.")    

# 삼항 연산자:  true일때 / if 조건식 / else 거짓일때
print("양수") if num > 0 else print("음수")