#사용하려는 함수가있는 파일명을 임포트하고 as 로 약어처리가능
# import ex02_function as fu2

#hello1만 쓸때 이때는 함수명만 가져와서 사용가능
from ex02_function import hello1 

hello1()
# fu2.hello2()

#함수를 모두 import 하는 방법
from ex02_function import *

hello1()
hello2()