#튜플: () 로 만든다. 재할당할수 없다 수정x
int_tuple = (1, 2, 3, 4)
print(int_tuple)
print(int_tuple[1])
print(int_tuple[2])
int_tuple[2] = 10
print(int_tuple[2])

str_tuple = ("hello", "안녕하세요", "ㅎㅎㅎ")

mix_tuple = (10 , 20, "ggg", "python")
print(mix_tuple)


tuple_in_tuple = ("hi", (1, 20, "ggg"), "hello")