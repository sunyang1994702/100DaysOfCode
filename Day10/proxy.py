import base64

def response(flow):

    """
    if 'webdriver' in flow.response.text:
        print('*' * 100)
        print('find web_driver key')
        flow.response.text = flow.response.text.replace("webdriver", "fuck_that_1")
    if 'Webdriver' in flow.response.text:
        print('*' * 100)
        print('find web_driver key')
        flow.response.text = flow.response.text.replace("Webdriver", "fuck_that_2")
    if 'WEBDRIVER' in flow.response.text:
        print('*' * 100)
        print('find web_driver key')
        flow.response.text = flow.response.text.replace("WEBDRIVER", "fuck_that_3")
    print(flow.response.text)
    """

    detectList = ['webdriver', '__driver_evaluate', '__webdriver_evaluate', '__selenium_evaluate', '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_unwrapped', '__selenium_unwrapped', '__fxdriver_unwrapped', '_Selenium_IDE_Recorder', '_selenium', 'calledSelenium', '_WEBDRIVER_ELEM_CACHE', 'ChromeDriverw', 'driver-evaluate', 'webdriver-evaluate', 'selenium-evaluate', 'webdriverCommand', 'webdriver-evaluate-response', '__webdriverFunc', '__webdriver_script_fn', '__$webdriverAsyncExecutor', '__lastWatirAlert', '__lastWatirConfirm', '__lastWatirPrompt', '$chrome_asyncScriptInfo', '$cdc_asdjflasutopfhvcZLmcfl_']

    for i in range(len(detectList)):
        detectList.append(str(base64.b64encode(bytes(detectList[i], 'utf8')), 'utf8'))

    if '.js' in flow.request.url:
        for webdriver_key in detectList:
            flow.response.text=flow.response.text.replace('"{}"'.format(webdriver_key),'"fuck_that_1"')
            flow.response.text=flow.response.text.replace('t.webdriver','false')
            flow.response.text=flow.response.text.replace('ChromeDriver','')
            print("{} was replaced!!!!".format(webdriver_key))