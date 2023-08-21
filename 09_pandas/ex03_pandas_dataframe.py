import pandas as pd

score = pd.DataFrame(
    [
        [96,78,28,67,84],
        [88,75,97,29,17],
        [30,48,67,87,25]
    ]
)
print(score)

scores = pd.DataFrame(
    [
        [96,78,28,67,84],
        [88,75,97,29,17],
        [30,48,67,87,25]
    ],
    # 인덱스는 꼭 숫자일 필요는 없다.
    index=["java", "python", "js"]
)
print(scores)

student_number = [1,2,3,4,5]
scores = pd.DataFrame(
    [
        [96,80,75],
        [58,85,24],
        [81,45,37],
        [87,52,78],
        [100,87,22]
    ],
    index=student_number
)
print(scores)

scores = pd.DataFrame(
    {   
        "학생이름":["김파이", "이파이", "초파이", "팍파이", "조파이"],
        "java":[96,78,28,67,84],
        "python":[88,75,97,29,17],
        "js":[30,48,67,87,25]
    },
    # 인덱스는 꼭 숫자일 필요는 없다.
    index=student_number
)
print(scores)

# 딕셔너리 데이터를 DataFrame 으로 변환
scores_dict = {
    "java":[96,78,28,67,84],
    "python":[88,75,97,29,17],
    "js":[30,48,67,87,25]
}
scores = pd.DataFrame(scores_dict)
print(scores)

scores = pd.DataFrame(
    {   
        "java":[96,78,28,67,84],
        "python":[88,75,97,29,17],
        "js":[30,48,67,87,25]
    },
    # 인덱스는 꼭 숫자일 필요는 없다.
    index=student_number
)
print(scores)

scores["이름"] = ["김파이", "이파이", "박파이", "최파이", "조파이"]
print(scores)

#데이터 추가
scores.loc[6] = [80, 80, 80, "구파이"]
print(scores)

student_number = [1,2,3,4,5,6]
#학번, 이름, 성적을 모두 포함한 DataFrame 선언

scores = pd.DataFrame(
    {
        "이름": ["김파이", "이파이", "박파이", "최파이", "조파이", "구파이"],
        "java":[96,78,28,67,84,80],
        "python":[88,75,97,29,17,76],
        "js":[30,48,67,87,25,57]
    },
    index = student_number
    #행과 열을 바꾸는 함수
)# .transepose()

print(scores)

# index 기준 정렬
print(scores.sort_index())
# index 기준 내림차순 정렬
print(scores.sort_index(ascending=False))
# "이름" 열 기준 오름차순 정렬
print(scores.sort_values(by="이름", ascending=True))
print(scores.sort_values(by="이름", ascending=False))
print(scores.sort_values(by="python", ascending=False))

# 첫 2줄만 조회
print(scores.head(2))
print(scores.tail(2))

#DataFrame을 csv로 내보내기
scores.to_csv("./scores.csv", encoding="utf-8-sig")

