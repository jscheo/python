from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from ex06_scroll import scroll_fun()

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

# 크롬 브라우저 실행
driver = webdriver.Chrome()

driver.get("https://www.youtube.com")
time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR, 'input#search')
search.send_keys("조준상")
search.send_keys(Keys.RETURN)

time.sleep(2)

filter = driver.find_element(By.XPATH, '//*[@id="filter-button"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
filter.click()

time.sleep(2)
# 조회수 클릭 fullxpath로 지정
select_filter= driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string')
select_filter.click()

time.sleep(2)

#무한 스크롤 해서 제목출력
scroll_fun()
             
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    print(title.text)
print(len(titles))

time.sleep(3)

