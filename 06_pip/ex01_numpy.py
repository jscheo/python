# numpy import
import numpy as np
# numpy 쓰는 이유는 수학적 계산을 하기 위해서 쓴다.
# numpy 배열 선언
arr = np.array([2, 1, 4, 3, 5, 7, 8, 9, 6])
print(arr)

# 정렬
arr = np.sort(arr)
print(arr)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
# 두개의 배열을 합칠 때 사용
arr3 = np.concatenate((arr1, arr2))
print(arr3)

#배열 연산
arr11 = arr1 + 10
print("arr11", arr11)
arr12 = arr1 - arr2
print("arr12", arr12)

# 배열 슬라이싱(특정 인덱스 범위 접근하기)
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr4[:2]) # 0~1번 인덱스
print(arr4[1:2]) # 1~1번 인덱스
print(arr4[3:8]) # 3~7번 인덱스
print(arr4[6:]) #6번인덱스부터 끝까지 인덱스