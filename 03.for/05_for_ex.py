# 중첩 for 문을 이용하여 구구단을 세로형, 가로형으로 각각 만들어봅시다.

for x in range(2, 10):
    for y in range(1, 10):
        print(x, '*', y, '=', x * y )
    print("------------")

# for x in range(2, 10):
#     # 다른타입끼리 연결할 때는 , 같은거는 +가능
#     print(x, "단")
#     for y in range(1, 10):
#         # 문자 연결할 때 , 사용 + 아님
#         print(x, '*', y, '=', x * y, '/', end=" ")
#         if(y==9):
#             print()

list = range(1,10) 
list1 = range(2,10)

for i in list1:
    for j in list:
        print(i, '*', j, '=', i * j)
        if(j== 9):
            print("---------------")

for i in list1:
    print("----------[", i ,"단]--------")
    for j in list:
        print(i, '*', j, '=', i * j, end ="\t")
        if(j== 9):
            print()
            
a= int(input("몇 단을 출력하시겠습니까?:"))

for y in range(1, 10):
    print(a, '*', y, '=', a*y)
     
