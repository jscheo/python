from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.naver.com/")
# 검색창에 접근
search_element = driver.find_element(By.XPATH, '//*[@id="query"]')
# 검색어 입력
search_element.send_keys("오늘 날씨")
# 검색버튼을 클릭
search_button = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
search_button.click()


time.sleep(10)
