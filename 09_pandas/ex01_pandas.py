import pandas as pd

# 시리즈 선언
series1 = pd.Series([2,4,6,8,10])
print(series1)

#index를 지정
series2 = pd.Series([2,4,6,8,10], index=[3,1,2,5,4])
print(series2)

#range로 index 지정
series3 = pd.Series([2,4,6,8,10], index=range(1,6))
print(series3)

#index용 리스트
index_value = [10,11,12,13,14]
series4 = pd.Series([2,4,6,8,10], index=index_value)
print(series4)

#데이터, index를 따로 선언 후 활용
data_value = [1, 34, 15, 32, 123]
index_value = [10, 20, 30 ,40 ,50]
series5 = pd.Series(data_value, index=index_value)
print(series5)

