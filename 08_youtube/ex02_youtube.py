from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
# driver.get("https://www.youtube.com/")
# 검색결과 페이지 접속
driver.get("https://www.youtube.com/results?search_query=크리스폴")
                                            # 태그의 요소에 접근할때 양식
# search = driver.find_element(By.CSS_SELECTOR, 'input#search')

# search.send_keys("농구")

# search_button = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
# search_button.click()

#엔터 치기
# search.send_keys(Keys.RETURN)

time.sleep(3)

#제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
for title in titles:
    print(title.text) # innerHTML 값

time.sleep(3)

# https://www.youtube.com/results?search_query=뉴진스+민지
# https://www.youtube.com/results?search_query=크리스폴
