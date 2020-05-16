import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common import action_chains

mk_title = '测试推送'
mk_types = '后端笔记'
is_markdown = True
content_md_cc = '''
    ## 标题
     jason今天去李宁了
    > NICE
    - BBC
    - 川普
'''


# 定义一个函数，给他一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)


# locator参数是定位方式，如("id", "kw"),把两个参数合并为一个,*号是把两个参数分开传值
def find_element(driver, locator):
    element = WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_element_by_xpath(locator))
    return element


def find_elements(driver, locator):
    element = WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_elements_by_xpath(locator))
    return element


# 判断元素是否存在
def is_exists(driver, locator):
    try:
        WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_element_by_xpath(locator))
        return True
    except Exception as e:
        print(e)
        return False


# # github授权登录 def github(driver, timeout): # 判断是否需要登录 try: login = driver.find_element_by_xpath("// *[ @ id =
# 'login'] /form/div[3]/input[9]") if login: username = driver.find_element_by_xpath("// *[@id= 'login_field']")
# username.send_keys("") pwd = driver.find_element_by_xpath("//*[@id='password']") pwd.send_keys(
# "S") login.click() time.sleep(2) except Exception as e: print(e) finally: login_btn =
# WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="js-oauth-authorize-btn"]'))
# login_btn.click()


def open_browser():
    uri = "https://www.oschina.net/home/login"
    # 打开浏览器
    browser = webdriver.Chrome('./../chromedriver.exe')
    browser.maximize_window()
    browser.get(uri)  # 打开网页
    # link = browser.find_element_by_xpath("/html/body/section/div/div[2]/div[2]/div/div[2]/a[3]")
    # link.click()
    # github(browser, 30000)
    username = browser.find_element_by_xpath("//*[@id='userMail']")
    username.send_keys("你的账号")
    pwd = browser.find_element_by_xpath("//*[@id='userPassword']")
    pwd.send_keys("你的密码")
    # 登录
    logbtn = browser.find_element_by_xpath('//*[@id="account_login"]/form/div/div[5]/button')
    logbtn.click()
    time.sleep(2)
    user_info = browser.find_element_by_xpath('//*[@id="headerNavMenu"]/div[3]/a[2]')
    user_info.click()
    # 点击写博客
    write_blog = find_element(browser, '//*[@id="userSidebar"]/a[3]')
    write_blog.click()
    # 标题
    title = find_element(browser, '//*[@id="writeArticleWrapper"]/div/div/form/div[1]/div[1]/input')
    title.send_keys(mk_title)

    # 获取文章分类
    type_xpath = '//*[@id="writeArticleWrapper"]/div/div/form/div[1]/div[2]/div/div[2]/div[text()="' + mk_types + '"]'
    types = find_elements(browser, '//*[@id="writeArticleWrapper"]/div/div/form/div[1]/div[2]/div/div[2]/div')
    type_exist = is_exists(browser, type_xpath)
    time.sleep(2)
    print("----> 判断文章分类是否存在：" + str(type_exist))
    if type_exist:
        for typet in types:
            browser.execute_script("arguments[0].setAttribute('class','item')", typet)
        cur_type = browser.find_element_by_xpath(type_xpath)
        browser.execute_script("arguments[0].setAttribute('class','item active selected')", cur_type)
    else:
        #  新增分类
        add_type = browser.find_element_by_xpath('//*[@id="writeArticleWrapper"]/div/div/form/div[1]/div[2]/label/span')
        add_type.click()
        type_name = browser.find_element_by_xpath('/html/body/div[6]/div/div[2]/form/div[1]/input')
        type_name.send_keys(mk_types)
        add_btn = browser.find_element_by_xpath('/html/body/div[6]/div/div[3]/div[2]')
        time.sleep(1)
        add_btn.click()
    # 是否是markdown格式
    text_edit_types = find_elements(browser, '//*[@id="editorTabList"]/a')
    for text_type in text_edit_types:
        if text_type.text == 'Markdown' and is_markdown:
            text_type.click()
            break
    # if is_markdown:
    #     rich_text = browser.find_element_by_xpath('//*[@id="editorTabList"]/a[2]')
    #     rich_text.click()
    # else:
    #     rich_text = browser.find_element_by_xpath('//*[@id="editorTabList"]/a[1]')
    #     rich_text.click()
    # 文章内容
    time.sleep(2)
    e = browser.find_element_by_css_selector(".CodeMirror textarea")  #

    # 找到所在输入的行对象
    p = browser.find_element_by_css_selector("pre.CodeMirror-line")

    # 对做所在行进行点击操作，激活文本框
    p.click()
    # 在文本框中输入内容
    e.send_keys(content_md_cc)
    # 系统分类
    s1 = find_elements(browser, '//*[@name="classification"]')[0]
    browser.execute_script("arguments[0].options[3].selected=true", s1)

    yrih = browser.find_element_by_xpath('//*[@id="writeArticleWrapper"]/div/div/form/div[4]/div[2]/div')
    browser.execute_script("arguments[0].setAttribute('class','ui checkbox checked')", yrih)
    time.sleep(2)

    submit = browser.find_element_by_xpath('//*[@id="writeArticleWrapper"]/div/div/form/div[8]/div[1]')
    submit.click()

    title_success = WebDriverWait(browser, 10000).until(lambda d:
                                                        d.find_element_by_xpath(
                                                            '//*[@id="mainScreen"]/div/div[1]/div/div[2]/div['
                                                            '1]/div[2]/h2'))
    print(title_success.text + '发布成功')


if __name__ == "__main__":
    open_browser()
