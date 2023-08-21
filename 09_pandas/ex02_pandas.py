import pandas as pd

# series 끼리 연산할 때는 순서는 상관없고 인덱스 끼리 같은 인덱스를 자동으로 찾아서 연산한다.
# 그래도 맞춰서 해라^^
#성적 다루는 간단한 예제
# 학번 정보
student_number = [1,2,3,4,5]

score_java = pd.Series([98, 29, 49, 50, 94], index=student_number)
score_python = pd.Series([88, 95, 20, 67, 40], index=student_number)

print(score_java)
print(score_python)

#java, python 시리즈 합계
total = score_java + score_python
print(total)

score_js = pd.Series([30, 20 , 10, 40, 50], index=[3,2,4,5,1])
print(score_js)
#index 값 기준으로 정렬하여 출력
# sort는 디폴트가 오름차순
# print(score_js.sort_index())

#java, python, js 총 합계
total = score_java + score_python + score_js
print(total)

# index 기준 내림차순 정리(큰게 먼저)
print(total.sort_index(ascending=False))
# 값 기준 오름차순 정렬(작은게 먼저/ 가다나/abc)
print(total.sort_values())
print(total.sort_values(ascending=False))

