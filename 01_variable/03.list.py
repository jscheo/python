# 나열형 타입: list, tuple, range
# list 타입
# 리스트도 인덱스값을 가지고 있고 인덱스값을 수정하고 싶으면 인덱스번호를 담아서 수정할 값 넣어주면 바로바뀐다.
int_list = [1, 2, 3, 4]
print(int_list)
print(int_list[0])
print(int_list[2])
int_list[3] = 500
print(int_list)

#문자열 리스트
str_list = ["hello", "안녕", "ㅎㅎㅎ"]
print(str_list)
print(str_list[0])
print(str_list[2])

#다양한 자료형이 섞인 리스트(섞여도 상관이 없음 다 따로 처리)
mix_list = [1, "안녕", 10, 30, "hello"]
print(mix_list)
print(mix_list[2])
print(mix_list[4])

#리스트 내에 리스트(리스트 안에 또 [] 를 이용한 리스트(배열) 부여가 가능)
list_in_list = [100, 200, ["내부리스트값", 10], "ㅎㅎㅎ", 1.234]
print(list_in_list)
print(list_in_list[2])
print(list_in_list[4])