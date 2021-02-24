from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


"""Chromeの｢自動テストソフトソフトウェアによって制御されています｣を消す"""
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


driver = webdriver.Chrome()
try:
    driver.get("https://www.google.com")
    input = driver.find_element_by_name("q")
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)

    print("URL: {}".format(driver.current_url))
    print("Cookies : {}".format(driver.get_cookies()))

    ## 加入time sleep防止浏览器闪退！！！, 如果是在终端就不用加time sleep
    time.sleep(100)
except Exception as e:
    print(e)






