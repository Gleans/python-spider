from selenium import webdriver

browser = webdriver.Chrome('./../chromedriver.exe')
browser.maximize_window()
browser.get('https://www.baidu.com/')  # 打开网页

a = browser.find_element_by_xpath('//*[@id="bottom_layer"]/div[1]/p[7]/a')
browser.execute_script("arguments[0].setAttribute('class','diy_class')", a)