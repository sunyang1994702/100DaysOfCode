from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import random




agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'

option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
option.add_argument('user-agent={}'.format(agent))
#option.add_argument("--disable-blink-features=AutomationControlled")
#option.add_experimental_option('useAutomationExtension', False)
PROXY = "127.0.0.1:8080"
option.add_argument('--proxy-server={}'.format(PROXY))
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(chrome_options=option)


def main(url):
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    box = wait.until(EC.presence_of_element_located((By.ID, 'yodaBox')))
    # 获取bar的长，宽
    bar = browser.find_element_by_id('yodaBox')
    bar_sliding = bar.size
    # 获取整个div的长，宽
    box_div = browser.find_element_by_id('yodaBoxWrapper').size
    
    # 滑动的距离
    sliding_distance = box_div.get('width') - bar_sliding.get('width')
    print(sliding_distance)

    actions = ActionChains(browser)
    actions.click_and_hold(bar).perform()
    for i in [40, 50, 70, 40, 10, 40, 60, 60]:
        actions.move_by_offset(xoffset=i, yoffset=0).perform()
        time.sleep(0.5)
        print("======================")
    actions.release().perform()


    time.sleep(100)





if __name__ == '__main__':
    url = 'http://m.maoyan.com/mmdb/comments/movie/1299372.json'
    main(url)
