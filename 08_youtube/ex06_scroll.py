# while문을 적용하여 무한스크롤 구현하기
# while문 내부 동작
# 1. 처음 높이값 확인. 
# 2. 높이 만큼 스크롤 내리기
# 3. 높이값 확인
# 4. 높이가 같다면 break로 while문 중단

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()

driver.get("http://www.youtube.com")

def scroll_fun():
    while True:
        h1 = driver.execute_script("return document.documentElement.scrollHeight")
        print("현재높이",h1)
        # 스크롤을 현재높이 만큼 내리기
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        #영상 로딩 시간
        time.sleep(2)

        h2= driver.execute_script("return document.documentElement.scrollHeight")
        print("두번 째 높이:", h2)
        if h1 == h2 :
            print("끝!")
            break
        
    titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    return titles

# 무한스크롤 함수 호출
titles=scroll_fun()
for title in titles:
    print(title.text)
print("영상 갯수:", len(titles))