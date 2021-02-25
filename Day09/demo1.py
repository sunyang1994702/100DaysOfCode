from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


amazon_url = 'http://www.amazon.com'
drag_url = 'https://www.runoob.com/try/try.php?filename=jqueryui-example-droppable'
zhihu_url = 'https://www.zhihu.com/explore'
google_url = 'http://www.google.com'
driver = webdriver.Chrome()
driver.get(google_url)


def demo1():
    """Amazon : Using clear() to clear the input info"""
    input1 = driver.find_element(By.ID, 'twotabsearchtextbox')
    input1.send_keys('Python')
    time.sleep(5)
    input1.clear()
    input1.send_keys('iPhone')
    input1.send_keys(Keys.ENTER)

    time.sleep(100)


def demo2():
    """Amazon : Using refresh() to refresh the web page"""
    input2 = driver.find_element(By.ID, 'twotabsearchtextbox')
    input2.send_keys('Python')
    ## when the page refreshed, it need to find element again.
    driver.refresh()
    input2 = driver.find_element(By.ID, 'twotabsearchtextbox')
    input2.send_keys('iPhone')
    button = driver.find_element_by_id('nav-search-submit-button')
    button.click()

    time.sleep(100)


def demo3():
    """drag and drop"""
    logo = driver.find_element_by_class_name('logo')
    print(logo.text)
    try:
        source = driver.find_element_by_id('draggable')
    except NoSuchElementException:
        print('No Such That Node')

    ## switch to ifrmae. It can not get node info of children-frame from parent-frames.
    driver.switch_to.frame('iframeResult')
    #button = driver.find_element_by_id('submitBTN')
    #button.click()
    #time.sleep(1)
    source = driver.find_element_by_id('draggable')
    target = driver.find_element_by_id('droppable')
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target)
    actions.perform()

    time.sleep(100)


def demo4():
    """execute js code!"""
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    driver.execute_script('alert("To Bottom")')

    time.sleep(100)


def demo5():
    """get node info"""
    ## get node attribute
    logo = driver.find_element_by_class_name('ZhihuLogoLink')
    print(logo)
    print(logo.get_attribute('href'))

    ## get node text
    one_text = driver.find_element_by_class_name('ExploreSpecialCard-contentTitle')
    print(one_text.text)

    ## get node location, tag_name, size.
    button = driver.find_element_by_class_name('Button--primary')
    print(button.location)
    print(button.tag_name)
    print(button.size)

    ## get page cookies
    cookies = driver.get_cookies()
    str_cookie = ""
    for cookie in cookies:
        str_cookie += cookie['name'] + "=" + cookie['value']
    print(str_cookie)

    time.sleep(100)


def demo6():
    """Amazon"""
    wait = WebDriverWait(driver, 10)
    item_list = wait.until(EC.presence_of_element_located((By.ID, 'nav-hamburger-menu')))
    print(item_list)
    item_list = driver.find_element_by_id('nav-hamburger-menu')
    item_list.click()

    time.sleep(2)

    music = driver.find_elements_by_class_name('hmenu-item')[1]
    music.click()


    time.sleep(100)


def demo7():
    """Google"""
    ### open a new sub-window in current page.
    driver.execute_script('window.open()')
    print(driver.window_handles)

    driver.switch_to_window(driver.window_handles[1])
    driver.get(amazon_url)
    time.sleep(1)
    
    driver.switch_to_window(driver.window_handles[0])
    driver.get(zhihu_url)

    time.sleep(100)

if __name__ == '__main__':
    demo7()
