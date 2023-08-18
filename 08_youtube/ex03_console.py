from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

search = input("검색어를 입력하세요: ")

# 크롬 브라우저 실행
driver = webdriver.Chrome()

driver.get("http://www.youtube.com/results?search_query="+ search)

time.sleep(3)

# search_title = driver.find_element(By.CSS_SELECTOR, 'input#search')
# search_title.send_keys(search)
# search_title.send_keys(Keys.RETURN)

# time.sleep(3)

titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
for title in titles:
    print(title.text) # innerHTML 값

time.sleep(3)


