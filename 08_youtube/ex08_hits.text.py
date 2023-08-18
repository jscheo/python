#조회수값 추출하기

aria_label = "난리라는 《오펜하이머》, 조회수 근데 그냥 갔다가 진짜 피똥쌉니다... 제발 그냥 보러가지마세요. 가이드의 가이드 리뷰영상 게시자: DOCLIP :: 두클립 22시간 전 8분 16초 조회수 33,231회"


# rfind(): 매개변수로 전달한 글자가 인덱스 값을 반환 (해당 변수의 제일 마지막에서 시작하여 찾음)
# find() : 해당 변수의 시작지점 부터 찾음

print(aria_label.rfind("조회수"))
print(aria_label.find("조회수"))

#조회수 값의 시작 인덱스 값
print(aria_label.rfind("조회수")+4)
print(aria_label[106]) # 3
#조회수 값의 끝 인덱스 값
print(aria_label.rfind("회"))
print(aria_label[111]) # 1

#조회수 값만 출력하기
print(aria_label[106:112])

start_index= aria_label.rfind("조회수")+4
end_index = aria_label.rfind("회")
hits = aria_label[start_index:end_index]

print(hits)
print(type(hits))

#쉼표 제거 후 정수형으로 변환
# replace(): 바꾸기 기능
hits = int(hits.replace(",",""))
print(hits)
print(type(hits))