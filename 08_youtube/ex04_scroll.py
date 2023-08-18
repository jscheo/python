# selenium 으로 javascript 코드 적용하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()

driver.get("http://www.youtube.com")

# jsvascript로 현재 페이지 높이값 가져오기
# execute_script(): javascript 코드를 실행하는 함수
# javascript 실행값을 파이썬 변수로 받으려면  return을 작성해야함
h = driver.execute_script("return document.documentElement.scrollHeight")
print(h)