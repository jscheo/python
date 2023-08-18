from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://comic.naver.com/webtoon")

time.sleep(3)

webtoon_title = driver.find_elements(By.CSS_SELECTOR, '[class="text"]')
for title in webtoon_title:
    print(title.text)
print(len(webtoon_title))
