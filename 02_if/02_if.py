# 자바의 scanner처럼 실행 후 콘솔에서 입력받아
# 홀수, 짝수를 판별하여 출력하는 코드를 작성하시오.
# input결과물은 str이다 필요한 타입으로 형변환 필요
number = int(input("숫자를 입력하세요:"))

print("입력숫자:", number)

if number % 2 ==0 :
    print ("짝수")
elif number % 2 ==1 :
    print("홀수")

print("짝수") if number % 2==0 else print("홀수")
   
    